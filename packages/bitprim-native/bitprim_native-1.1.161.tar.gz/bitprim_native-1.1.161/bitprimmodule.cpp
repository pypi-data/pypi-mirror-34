/**
 * Copyright (c) 2017 Bitprim developers (see AUTHORS)
 *
 * This file is part of Bitprim.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

//TODO: migrate to the new API for Extension Modules
//          https://docs.python.org/3/howto/cporting.html

#include <Python.h>
#include "bitprimmodule.h"
#include "binary.h"
#include "utils.h"
#include "chain/point.h"
#include "chain/history.h"
#include "chain/chain.h"
#include "chain/block.h"
#include "chain/header.h"
#include "chain/merkle_block.h"
#include "chain/word_list.h"
#include "chain/transaction.h"
#include "chain/output.h"
#include "chain/output_list.h"
#include "chain/input.h"
#include "chain/input_list.h"
#include "chain/script.h"
#include "chain/output_point.h"
#include "chain/compact_block.h"
#include "chain/payment_address.h"
#include "chain/block_list.h"
#include "chain/transaction_list.h"
#include "chain/stealth_compact.h"
#include "chain/stealth_compact_list.h"

#include "p2p/p2p.h"

#include <bitprim/nodecint.h>

#include <iostream>

// ---------------------------------------------------------

#ifdef __cplusplus
extern "C" {  
#endif  


PyObject* bitprim_native_executor_construct(PyObject* self, PyObject* args) {
    char const* path;
    PyObject* py_out;
    PyObject* py_err;


    if ( ! PyArg_ParseTuple(args, "sOO", &path, &py_out, &py_err))
        return NULL;

#if PY_MAJOR_VERSION >= 3
    int sout_fd = py_out == Py_None ? -1 : PyObject_AsFileDescriptor(py_out);
    int serr_fd = py_err == Py_None ? -1 : PyObject_AsFileDescriptor(py_err);

    executor_t exec = executor_construct_fd(path, sout_fd, serr_fd);
    return PyCapsule_New(exec, NULL, NULL);

#else /* PY_MAJOR_VERSION >= 3 */
    FILE* sout = py_out == Py_None ? NULL : PyFile_AsFile(py_out);
    FILE* serr = py_err == Py_None ? NULL : PyFile_AsFile(py_err);
//    PyFile_IncUseCount(p);
///* ... */
//    Py_BEGIN_ALLOW_THREADS
//        do_something(fp);
//    Py_END_ALLOW_THREADS
///* ... */
//        PyFile_DecUseCount(p);

    executor_t exec = executor_construct(path, sout, serr);
    return PyCObject_FromVoidPtr(exec, NULL);

#endif /* PY_MAJOR_VERSION >= 3 */

}


// ---------------------------------------------------------

PyObject* bitprim_native_executor_destruct(PyObject* self, PyObject* args) {
    PyObject* py_exec;

    // PyGILState_STATE gstate;
    // gstate = PyGILState_Ensure();

    if ( ! PyArg_ParseTuple(args, "O", &py_exec))
        return NULL;

    executor_t exec = cast_executor(py_exec);

    executor_destruct(exec);
    // PyGILState_Release(gstate);
    Py_RETURN_NONE;
}

// ---------------------------------------------------------

PyObject* bitprim_native_executor_initchain(PyObject* self, PyObject* args) {

    PyObject* py_exec;

    if ( ! PyArg_ParseTuple(args, "O", &py_exec)) {
        return NULL;
    }

    executor_t exec = cast_executor(py_exec);

    int res = executor_initchain(exec);

    return Py_BuildValue("i", res);
}

// ---------------------------------------------------------

void executor_run_handler(executor_t exec, void* ctx, int error) {
 
    PyObject* py_callback = (PyObject*)ctx;

    PyObject* arglist = Py_BuildValue("(i)", error);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);
    Py_XDECREF(py_callback);  // Dispose of the call
}


PyObject* bitprim_native_executor_run(PyObject* self, PyObject* args) {
    PyObject* py_exec;
    PyObject* py_callback;

    if ( ! PyArg_ParseTuple(args, "OO:set_callback", &py_exec, &py_callback)) {
        return NULL;
    }

    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }    

    executor_t exec = cast_executor(py_exec);
    Py_XINCREF(py_callback);         // Add a reference to new callback
    executor_run(exec, py_callback, executor_run_handler);
    Py_RETURN_NONE;
}


// ---------------------------------------------------------

PyObject* bitprim_native_executor_run_wait(PyObject* self, PyObject* args) {
    PyObject* py_exec;

    if ( ! PyArg_ParseTuple(args, "O", &py_exec))
        return NULL;

    executor_t exec = cast_executor(py_exec);

    int res = executor_run_wait(exec);
    return Py_BuildValue("i", res);
}

// ---------------------------------------------------------

PyObject* bitprim_native_executor_stopped(PyObject* self, PyObject* args) {
    PyObject* py_exec;

    if ( ! PyArg_ParseTuple(args, "O", &py_exec))
        return NULL;

    executor_t exec = cast_executor(py_exec);

    int res = executor_stopped(exec);
    return Py_BuildValue("i", res);
}


// ---------------------------------------------------------

PyObject* bitprim_native_executor_stop(PyObject* self, PyObject* args) {
    PyObject* py_exec;

    // PyGILState_STATE gstate;
    // gstate = PyGILState_Ensure();
    
    if ( ! PyArg_ParseTuple(args, "O", &py_exec))
        return NULL;

    executor_t exec = cast_executor(py_exec);

    executor_stop(exec);

    // PyGILState_Release(gstate);
    Py_RETURN_NONE;
}


PyObject* bitprim_native_executor_get_chain(PyObject* self, PyObject* args) {
    PyObject* py_exec;
    if ( ! PyArg_ParseTuple(args, "O", &py_exec))
        return NULL;

    executor_t exec = cast_executor(py_exec);
    chain_t chain = executor_get_chain(exec);

    PyObject* py_chain = to_py_obj(chain);
    return Py_BuildValue("O", py_chain);
}

PyObject* bitprim_native_executor_get_p2p(PyObject* self, PyObject* args) {
    PyObject* py_exec;
    if ( ! PyArg_ParseTuple(args, "O", &py_exec))
        return NULL;

    executor_t exec = cast_executor(py_exec);
    p2p_t p2p = executor_get_p2p(exec);

    PyObject* py_p2p = to_py_obj(p2p);
    return Py_BuildValue("O", py_p2p);
}

// -------------------------------------------------------------------

// long_hash_t wallet_mnemonics_to_seed(word_list_t mnemonics){
//     auto hash_cpp = libbitcoin::wallet::decode_mnemonic(*static_cast<const std::vector<std::string>*>(mnemonics));
//     return hash_cpp.data();
// }

PyObject* bitprim_native_wallet_mnemonics_to_seed(PyObject* self, PyObject* args) {
    PyObject* py_wl;

    if ( ! PyArg_ParseTuple(args, "O", &py_wl)) {
        return NULL;
    }

    word_list_t wl = (word_list_t)get_ptr(py_wl);
    
    long_hash_t res = wallet_mnemonics_to_seed(wl);

#if PY_MAJOR_VERSION >= 3
    return Py_BuildValue("y#", res.hash, 64);    //TODO: warning, hardcoded hash size!
#else
    return Py_BuildValue("s#", res.hash, 64);    //TODO: warning, hardcoded hash size!
#endif
}

PyObject* bitprim_native_wallet_ec_new(PyObject* self, PyObject* args) {
    uint8_t* py_seed;
    int py_n;

#if PY_MAJOR_VERSION >= 3
    if ( ! PyArg_ParseTuple(args, "y#", &py_seed, &py_n)) {
#else
    if ( ! PyArg_ParseTuple(args, "s#", &py_seed, &py_n)) {
#endif
        return NULL;
    }
    
    ec_secret_t res = wallet_ec_new(py_seed, py_n);
    // return to_py_obj(res);

#if PY_MAJOR_VERSION >= 3
    return Py_BuildValue("y#", res.data, 32);    //TODO: warning, hardcoded hash size!
#else
    return Py_BuildValue("s#", res.data, 32);    //TODO: warning, hardcoded hash size!
#endif

}

PyObject* bitprim_native_wallet_ec_to_public(PyObject* self, PyObject* args) {
    PyObject* py_secret;
    int py_size;
    int py_uncompressed;

#if PY_MAJOR_VERSION >= 3
    if ( ! PyArg_ParseTuple(args, "y#i", &py_secret, &py_size, &py_uncompressed)) {
#else
    if ( ! PyArg_ParseTuple(args, "s#i", &py_secret, &py_size, &py_uncompressed)) {
#endif
        return NULL;
    }

    ec_secret_t secret;
    memcpy(secret.data, py_secret, 32);

    ec_public_t res = wallet_ec_to_public(secret, py_uncompressed);
    return to_py_obj(res);
}

PyObject* bitprim_native_wallet_ec_to_address(PyObject* self, PyObject* args) {
    PyObject* py_point;
    uint32_t py_version;

    if ( ! PyArg_ParseTuple(args, "OI", &py_point, &py_version)) {
        return NULL;
    }

    ec_public_t point = (ec_public_t)get_ptr(py_point);
    payment_address_t res = wallet_ec_to_address(point, py_version);
    return to_py_obj(res);
}


// BITPRIM_EXPORT
// hd_private_t wallet_hd_new(uint8_t* seed, uint64_t n, uint32_t version /* = 76066276*/);

PyObject* bitprim_native_wallet_hd_new(PyObject* self, PyObject* args) {
    // uint8_t* py_seed;
    char* py_seed;
    int py_n;
    uint32_t py_version;

#if PY_MAJOR_VERSION >= 3
    if ( ! PyArg_ParseTuple(args, "y#I", &py_seed, &py_n, &py_version)) {
#else
    if ( ! PyArg_ParseTuple(args, "s#I", &py_seed, &py_n, &py_version)) {
#endif
        return NULL;
    }
    
    hd_private_t res = wallet_hd_new((uint8_t*)py_seed, py_n, py_version);
    return to_py_obj(res);
}

// BITPRIM_EXPORT
// ec_secret_t wallet_hd_private_to_ec(hd_private_t key);

PyObject* bitprim_native_wallet_hd_private_to_ec(PyObject* self, PyObject* args) {
    PyObject* py_key;

    if ( ! PyArg_ParseTuple(args, "O", &py_key)) {
        return NULL;
    }

    hd_private_t key = (hd_private_t)get_ptr(py_key);

    ec_secret_t res = wallet_hd_private_to_ec(key);

#if PY_MAJOR_VERSION >= 3
    return Py_BuildValue("y#", res.data, 32);    //TODO: warning, hardcoded hash size!
#else
    return Py_BuildValue("s#", res.data, 32);    //TODO: warning, hardcoded hash size!
#endif
}


/*
PyObject* bitprim_native_long_hash_t_to_str(PyObject* self, PyObject* args) {
    PyObject* py_lh;

    if ( ! PyArg_ParseTuple(args, "O", &py_lh)) {
        return NULL;
    }

    // long_hash_t lh = (long_hash_t)PyCObject_AsVoidPtr(py_lh);
    long_hash_t lh = (long_hash_t)PyCapsule_GetPointer(py_lh, NULL);

    return Py_BuildValue("y#", lh, 32 * 2);    //TODO: warning, hardcoded long hash size!
}


PyObject* bitprim_native_long_hash_t_free(PyObject* self, PyObject* args) {
    PyObject* py_lh;

    if ( ! PyArg_ParseTuple(args, "O", &py_lh)) {
        return NULL;
    }

    // long_hash_t lh = (long_hash_t)PyCObject_AsVoidPtr(py_lh);
    long_hash_t lh = (long_hash_t)PyCapsule_GetPointer(py_lh, NULL);
    
    // free(lh);
    long_hash_destroy(lh);

    Py_RETURN_NONE;
}*/



static
PyMethodDef BitprimNativeMethods[] = {

    {"construct",  bitprim_native_executor_construct, METH_VARARGS, "Construct the executor object."},
    // {"construct_devnull",  bitprim_native_executor_construct_devnull, METH_VARARGS, "Construct the executor object."},
    {"destruct",  bitprim_native_executor_destruct, METH_VARARGS, "Destruct the executor object."},
    {"initchain",  bitprim_native_executor_initchain, METH_VARARGS, "Directory Initialization."},
    {"run",  bitprim_native_executor_run, METH_VARARGS, "Node run."},
    {"run_wait",  bitprim_native_executor_run_wait, METH_VARARGS, "Node run."},
    {"stop",  bitprim_native_executor_stop, METH_VARARGS, "Node stop."},
    {"stopped",  bitprim_native_executor_stopped, METH_VARARGS, "Know if the Node stopped."},
    {"get_chain",  bitprim_native_executor_get_chain, METH_VARARGS, "Get Blockchain API."},
    {"get_p2p",  bitprim_native_executor_get_p2p, METH_VARARGS, "Get P2P Networking API."},
    
    {"p2p_address_count",  bitprim_native_p2p_address_count, METH_VARARGS, "..."},
    {"p2p_stop",  bitprim_native_p2p_stop, METH_VARARGS, "..."},
    {"p2p_close",  bitprim_native_p2p_close, METH_VARARGS, "..."},
    {"p2p_stopped",  bitprim_native_p2p_stopped, METH_VARARGS, "..."},



    {"chain_fetch_last_height",  bitprim_native_chain_fetch_last_height, METH_VARARGS, "..."},
    {"chain_fetch_history",  bitprim_native_chain_fetch_history, METH_VARARGS, "..."},
    {"chain_fetch_stealth",  bitprim_native_chain_fetch_stealth, METH_VARARGS, "..."},
    {"chain_fetch_block_height",  bitprim_native_chain_fetch_block_height, METH_VARARGS, "..."},
    {"chain_fetch_block_header_by_height",  bitprim_native_chain_fetch_block_header_by_height, METH_VARARGS, "..."},
    {"chain_fetch_block_header_by_hash",  bitprim_native_chain_fetch_block_header_by_hash, METH_VARARGS, "..."},
    {"chain_fetch_block_by_height",  bitprim_native_chain_fetch_block_by_height, METH_VARARGS, "..."},
    {"chain_fetch_block_by_hash",  bitprim_native_chain_fetch_block_by_hash, METH_VARARGS, "..."},
    {"chain_fetch_merkle_block_by_height",  bitprim_native_chain_fetch_merkle_block_by_height, METH_VARARGS, "..."},
    {"chain_fetch_merkle_block_by_hash",  bitprim_native_chain_fetch_merkle_block_by_hash, METH_VARARGS, "..."},
    {"chain_fetch_transaction",  bitprim_native_chain_fetch_transaction, METH_VARARGS, "..."},
    
    // Note: Removed on 3.3.0
    // {"chain_fetch_output",  bitprim_native_chain_fetch_output, METH_VARARGS, "..."},

    {"chain_fetch_transaction_position",  bitprim_native_chain_fetch_transaction_position, METH_VARARGS, "..."},
    {"chain_organize_block",  bitprim_native_chain_organize_block, METH_VARARGS, "..."},
    {"chain_organize_transaction",  bitprim_native_chain_organize_transaction, METH_VARARGS, "..."},
    {"chain_validate_tx",  bitprim_native_chain_validate_tx, METH_VARARGS, "..."},
    {"chain_fetch_compact_block_by_height",  bitprim_native_chain_fetch_compact_block_by_height, METH_VARARGS, "..."},
    {"chain_fetch_compact_block_by_hash",  bitprim_native_chain_fetch_compact_block_by_hash, METH_VARARGS, "..."},
    {"chain_fetch_spend",  bitprim_native_chain_fetch_spend, METH_VARARGS, "..."},
    {"chain_subscribe_blockchain",  bitprim_native_chain_subscribe_blockchain, METH_VARARGS, "..."},
    {"chain_subscribe_transaction",  bitprim_native_chain_subscribe_transaction, METH_VARARGS, "..."},
    {"chain_unsubscribe",  bitprim_native_chain_unsubscribe, METH_VARARGS, "..."},
    

    {"transaction_factory_from_data",  bitprim_native_chain_transaction_factory_from_data, METH_VARARGS, "..."},
    {"transaction_version",  bitprim_native_chain_transaction_version, METH_VARARGS, "..."},
    {"transaction_set_version",  bitprim_native_chain_transaction_set_version, METH_VARARGS, "..."},
    {"transaction_hash",  bitprim_native_chain_transaction_hash, METH_VARARGS, "..."},
    {"transaction_hash_sighash_type",  bitprim_native_chain_transaction_hash_sighash_type, METH_VARARGS, "..."},
    {"transaction_locktime",  bitprim_native_chain_transaction_locktime, METH_VARARGS, "..."},
    {"transaction_serialized_size",  bitprim_native_chain_transaction_serialized_size, METH_VARARGS, "..."},
    {"transaction_fees",  bitprim_native_chain_transaction_fees, METH_VARARGS, "..."},
    {"transaction_signature_operations",  bitprim_native_chain_transaction_signature_operations, METH_VARARGS, "..."},
    {"transaction_signature_operations_bip16_active",  bitprim_native_chain_transaction_signature_operations_bip16_active, METH_VARARGS, "..."},
    {"transaction_total_input_value",  bitprim_native_chain_transaction_total_input_value, METH_VARARGS, "..."},
    {"transaction_total_output_value",  bitprim_native_chain_transaction_total_output_value, METH_VARARGS, "..."},
    {"transaction_is_coinbase",  bitprim_native_chain_transaction_is_coinbase, METH_VARARGS, "..."},
    {"transaction_is_null_non_coinbase",  bitprim_native_chain_transaction_is_null_non_coinbase, METH_VARARGS, "..."},
    {"transaction_is_oversized_coinbase",  bitprim_native_chain_transaction_is_oversized_coinbase, METH_VARARGS, "..."},
    {"transaction_is_mature",  bitprim_native_chain_transaction_is_mature, METH_VARARGS, "..."},
    {"transaction_is_overspent",  bitprim_native_chain_transaction_is_overspent, METH_VARARGS, "..."},
    {"transaction_is_double_spend",  bitprim_native_chain_transaction_is_double_spend, METH_VARARGS, "..."},
    {"transaction_is_missing_previous_outputs",  bitprim_native_chain_transaction_is_missing_previous_outputs, METH_VARARGS, "..."},
    {"transaction_is_final",  bitprim_native_chain_transaction_is_final, METH_VARARGS, "..."},
    {"transaction_is_locktime_conflict",  bitprim_native_chain_transaction_is_locktime_conflict, METH_VARARGS, "..."},
    {"transaction_outputs",  bitprim_native_chain_transaction_outputs, METH_VARARGS, "..."},
    {"transaction_inputs",  bitprim_native_chain_transaction_inputs, METH_VARARGS, "..."},
    {"transaction_to_data",  bitprim_native_chain_transaction_to_data, METH_VARARGS, "..."},

    {"input_is_valid",  bitprim_native_chain_input_is_valid, METH_VARARGS, "..."},
    {"input_is_final",  bitprim_native_chain_input_is_final, METH_VARARGS, "..."},    
    {"input_serialized_size",  bitprim_native_chain_input_serialized_size, METH_VARARGS, "..."},
    {"input_sequence",  bitprim_native_chain_input_sequence, METH_VARARGS, "..."},    
    {"input_signature_operations",  bitprim_native_chain_input_signature_operations, METH_VARARGS, "..."},
    {"input_script",  bitprim_native_chain_input_script, METH_VARARGS, "..."},
    {"input_previous_output",  bitprim_native_chain_input_previous_output, METH_VARARGS, "..."},
    //{"input_get_hash",  bitprim_native_chain_input_get_hash, METH_VARARGS, "..."},
    //{"input_get_index",  bitprim_native_chain_input_get_index, METH_VARARGS, "..."},
    {"input_to_data",  bitprim_native_chain_input_to_data, METH_VARARGS, "..."},



    {"input_list_push_back",  bitprim_native_input_list_push_back, METH_VARARGS, "..."},
    {"input_list_count",  bitprim_native_input_list_count, METH_VARARGS, "..."},
    {"input_list_nth",  bitprim_native_input_list_nth, METH_VARARGS, "..."},

    {"output_is_valid",  bitprim_native_chain_output_is_valid, METH_VARARGS, "..."},
    {"output_serialized_size",  bitprim_native_chain_output_serialized_size, METH_VARARGS, "..."},
    {"output_value",  bitprim_native_chain_output_value, METH_VARARGS, "..."},
    {"output_signature_operations",  bitprim_native_chain_output_signature_operations, METH_VARARGS, "..."},
    {"output_script",  bitprim_native_chain_output_script, METH_VARARGS, "..."},
    //{"output_get_hash",  bitprim_native_chain_output_get_hash, METH_VARARGS, "..."},
    //{"output_get_index",  bitprim_native_chain_output_get_index, METH_VARARGS, "..."},
    {"output_to_data",  bitprim_native_chain_output_to_data, METH_VARARGS, "..."},

    {"output_list_push_back",  bitprim_native_output_list_push_back, METH_VARARGS, "..."},
    {"output_list_count",  bitprim_native_output_list_count, METH_VARARGS, "..."},
    {"output_list_nth",  bitprim_native_output_list_nth, METH_VARARGS, "..."},

    {"binary_construct",  bitprim_native_binary_construct, METH_VARARGS, "..."},
    {"binary_construct_string",  bitprim_native_binary_construct_string, METH_VARARGS, "..."},
    {"binary_construct_blocks",  bitprim_native_binary_construct_blocks, METH_VARARGS, "..."},
    {"binary_blocks",  bitprim_native_binary_blocks, METH_VARARGS, "..."},
    {"binary_encoded",  bitprim_native_binary_encoded, METH_VARARGS, "..."},

    {"merkle_block_get_header",  bitprim_native_chain_merkle_block_get_header, METH_VARARGS, "..."},
    {"merkle_block_is_valid",  bitprim_native_chain_merkle_block_is_valid, METH_VARARGS, "..."},
    {"merkle_block_hash_count",  bitprim_native_chain_merkle_block_hash_count, METH_VARARGS, "..."},
    {"merkle_block_serialized_size",  bitprim_native_chain_merkle_block_serialized_size, METH_VARARGS, "..."},
    {"merkle_block_total_transaction_count",  bitprim_native_chain_merkle_block_total_transaction_count, METH_VARARGS, "..."},
    {"merkle_block_reset",  bitprim_native_chain_merkle_block_reset, METH_VARARGS, "..."},

    {"block_get_header",  bitprim_native_chain_block_get_header, METH_VARARGS, "..."},
    {"block_hash",  bitprim_native_chain_block_hash, METH_VARARGS, "..."},
    {"block_transaction_count",  bitprim_native_chain_block_transaction_count, METH_VARARGS, "..."},
    {"block_serialized_size",  bitprim_native_chain_block_serialized_size, METH_VARARGS, "..."},
    {"block_fees",  bitprim_native_chain_block_fees, METH_VARARGS, "..."},
    {"block_claim",  bitprim_native_chain_block_claim, METH_VARARGS, "..."},
    {"block_reward",  bitprim_native_chain_block_reward, METH_VARARGS, "..."},
    {"block_generate_merkle_root",  bitprim_native_chain_block_generate_merkle_root, METH_VARARGS, "..."},

    {"block_is_valid",  bitprim_native_chain_block_is_valid, METH_VARARGS, "..."},
    {"block_transaction_nth",  bitprim_native_chain_block_transaction_nth, METH_VARARGS, "..."},
    {"block_signature_operations",  bitprim_native_chain_block_signature_operations, METH_VARARGS, "..."},
    {"block_signature_operations_bip16_active",  bitprim_native_chain_block_signature_operations_bip16_active, METH_VARARGS, "..."},
    {"block_total_inputs",  bitprim_native_chain_block_total_inputs, METH_VARARGS, "..."},
    {"block_is_extra_coinbases",  bitprim_native_chain_block_is_extra_coinbases, METH_VARARGS, "..."},
    {"block_is_final",  bitprim_native_chain_block_is_final, METH_VARARGS, "..."},
    {"block_is_distinct_transaction_set",  bitprim_native_chain_block_is_distinct_transaction_set, METH_VARARGS, "..."},
    {"block_is_valid_coinbase_claim",  bitprim_native_chain_block_is_valid_coinbase_claim, METH_VARARGS, "..."},
    {"block_is_valid_coinbase_script",  bitprim_native_chain_block_is_valid_coinbase_script, METH_VARARGS, "..."},
    {"block_is_internal_double_spend",  bitprim_native_chain_block_is_internal_double_spend, METH_VARARGS, "..."},
    {"block_is_valid_merkle_root",  bitprim_native_chain_block_is_valid_merkle_root, METH_VARARGS, "..."},

    {"header_get_version",  bitprim_native_chain_header_get_version, METH_VARARGS, "..."},
    {"header_set_version",  bitprim_native_chain_header_set_version, METH_VARARGS, "..."},
    {"header_get_previous_block_hash",  bitprim_native_chain_header_get_previous_block_hash, METH_VARARGS, "..."},
    //{"header_set_previous_block_hash",  bitprim_native_chain_header_set_previous_block_hash, METH_VARARGS, "..."},
    {"header_get_merkle",  bitprim_native_chain_header_get_merkle, METH_VARARGS, "..."},
    //{"header_set_merkle",  bitprim_native_chain_header_set_merkle, METH_VARARGS, "..."},
    {"header_get_hash",  bitprim_native_chain_header_get_hash, METH_VARARGS, "..."},
    {"header_get_timestamp",  bitprim_native_chain_header_get_timestamp, METH_VARARGS, "..."},
    {"header_set_timestamp",  bitprim_native_chain_header_set_timestamp, METH_VARARGS, "..."},
    {"header_get_bits",  bitprim_native_chain_header_get_bits, METH_VARARGS, "..."},
    {"header_set_bits",  bitprim_native_chain_header_set_bits, METH_VARARGS, "..."},
    {"header_get_nonce",  bitprim_native_chain_header_get_nonce, METH_VARARGS, "..."},
    {"header_set_nonce",  bitprim_native_chain_header_set_nonce, METH_VARARGS, "..."},

    {"history_compact_list_destruct",  bitprim_native_history_compact_list_destruct, METH_VARARGS, "..."},
    {"history_compact_list_count",  bitprim_native_history_compact_list_count, METH_VARARGS, "..."},
    {"history_compact_list_nth",  bitprim_native_history_compact_list_nth, METH_VARARGS, "..."},
    {"history_compact_get_point_kind",  bitprim_native_history_compact_get_point_kind, METH_VARARGS, "..."},
    {"history_compact_get_point",  bitprim_native_history_compact_get_point, METH_VARARGS, "..."},
    {"history_compact_get_height",  bitprim_native_history_compact_get_height, METH_VARARGS, "..."},
    {"history_compact_get_value_or_previous_checksum",  bitprim_native_history_compact_get_value_or_previous_checksum, METH_VARARGS, "..."},

    {"point_get_hash",  bitprim_native_point_get_hash, METH_VARARGS, "..."},
    {"point_is_valid",  bitprim_native_point_is_valid, METH_VARARGS, "..."},
    {"point_get_index",  bitprim_native_point_get_index, METH_VARARGS, "..."},
    {"point_get_checksum",  bitprim_native_point_get_checksum, METH_VARARGS, "..."},

    {"word_list_construct",  bitprim_native_word_list_construct, METH_VARARGS, "..."},
    {"word_list_destruct",  bitprim_native_word_list_destruct, METH_VARARGS, "..."},
    {"word_list_add_word",  bitprim_native_word_list_add_word, METH_VARARGS, "..."},

    {"wallet_mnemonics_to_seed",  bitprim_native_wallet_mnemonics_to_seed, METH_VARARGS, "..."},
    {"wallet_ec_new",  bitprim_native_wallet_ec_new, METH_VARARGS, "..."},
    {"wallet_ec_to_public",  bitprim_native_wallet_ec_to_public, METH_VARARGS, "..."},
    {"wallet_ec_to_address",  bitprim_native_wallet_ec_to_address, METH_VARARGS, "..."},
    {"wallet_hd_new",  bitprim_native_wallet_hd_new, METH_VARARGS, "..."},
    {"wallet_hd_private_to_ec",  bitprim_native_wallet_hd_private_to_ec, METH_VARARGS, "..."},


    {"script_destruct",  bitprim_native_chain_script_destruct, METH_VARARGS, "..."},
    {"script_is_valid",  bitprim_native_chain_script_is_valid, METH_VARARGS, "..."},
    {"script_is_valid_operations",  bitprim_native_chain_script_is_valid_operations, METH_VARARGS, "..."},
    {"script_satoshi_content_size",  bitprim_native_chain_script_satoshi_content_size, METH_VARARGS, "..."},
    {"script_serialized_size",  bitprim_native_chain_script_serialized_size, METH_VARARGS, "..."},
    {"script_to_string",  bitprim_native_chain_script_to_string, METH_VARARGS, "..."},
    {"script_sigops",  bitprim_native_chain_script_sigops, METH_VARARGS, "..."},
    {"script_embedded_sigops",  bitprim_native_chain_script_embedded_sigops, METH_VARARGS, "..."},

    {"payment_address_destruct",  bitprim_native_chain_payment_address_destruct, METH_VARARGS, "..."},
    {"payment_address_encoded",  bitprim_native_chain_payment_address_encoded, METH_VARARGS, "..."},
    {"payment_address_version",  bitprim_native_chain_payment_address_version, METH_VARARGS, "..."},
    {"payment_address_construct_from_string",  bitprim_native_chain_payment_address_construct_from_string, METH_VARARGS, "..."},

    {"output_point_get_hash",  bitprim_native_chain_output_point_get_hash, METH_VARARGS, "..."},
    //{"point_is_valid",  bitprim_native_point_is_valid, METH_VARARGS, "..."},
    {"output_point_get_index",  bitprim_native_chain_output_point_get_index, METH_VARARGS, "..."},
    {"output_point_construct",  bitprim_native_chain_output_point_construct, METH_VARARGS, "..."},
    {"output_point_construct_from_hash_index",  bitprim_native_chain_output_point_construct_from_hash_index, METH_VARARGS, "..."},
    {"output_point_destruct",  bitprim_native_chain_output_point_destruct, METH_VARARGS, "..."},
    //{"point_get_checksum",  bitprim_native_point_get_checksum, METH_VARARGS, "..."},

    {"compact_block_header",  bitprim_native_chain_compact_block_header, METH_VARARGS, "..."},
    {"compact_block_is_valid",  bitprim_native_chain_compact_block_is_valid, METH_VARARGS, "..."},
    {"compact_block_serialized_size",  bitprim_native_chain_compact_block_serialized_size, METH_VARARGS, "..."},
    {"compact_block_transaction_count",  bitprim_native_chain_compact_block_transaction_count, METH_VARARGS, "..."},
    {"compact_block_transaction_nth",  bitprim_native_chain_compact_block_transaction_nth, METH_VARARGS, "..."},
    {"compact_block_nonce",  bitprim_native_chain_compact_block_nonce, METH_VARARGS, "..."},
    {"compact_block_destruct",  bitprim_native_chain_compact_block_destruct, METH_VARARGS, "..."},
    {"compact_block_reset",  bitprim_native_chain_compact_block_reset, METH_VARARGS, "..."},

    {"header_destruct",  bitprim_native_chain_header_destruct, METH_VARARGS, "..."},
    {"block_destruct",  bitprim_native_chain_block_destruct, METH_VARARGS, "..."},
    {"merkle_block_destruct",  bitprim_native_chain_merkle_block_destruct, METH_VARARGS, "..."},
    {"transaction_destruct",  bitprim_native_chain_transaction_destruct, METH_VARARGS, "..."},
    {"output_destruct",  bitprim_native_chain_output_destruct, METH_VARARGS, "..."},
    {"input_destruct",  bitprim_native_chain_input_destruct, METH_VARARGS, "..."},

    {"block_list_construct_default",  bitprim_native_chain_block_list_construct_default, METH_VARARGS, "..."},
    {"block_list_push_back",  bitprim_native_chain_block_list_push_back, METH_VARARGS, "..."},
    {"block_list_destruct",  bitprim_native_chain_block_list_destruct, METH_VARARGS, "..."},
    {"block_list_count",  bitprim_native_chain_block_list_count, METH_VARARGS, "..."},
    {"block_list_nth",  bitprim_native_chain_block_list_nth, METH_VARARGS, "..."},

    {"transaction_list_construct_default",  bitprim_native_chain_transaction_list_construct_default, METH_VARARGS, "..."},
    {"transaction_list_push_back",  bitprim_native_chain_transaction_list_push_back, METH_VARARGS, "..."},
    {"transaction_list_destruct",  bitprim_native_chain_transaction_list_destruct, METH_VARARGS, "..."},
    {"transaction_list_count",  bitprim_native_chain_transaction_list_count, METH_VARARGS, "..."},
    {"transaction_list_nth",  bitprim_native_chain_transaction_list_nth, METH_VARARGS, "..."},

    {"stealth_compact_ephemeral_public_key_hash",  bitprim_native_stealth_compact_get_ephemeral_public_key_hash, METH_VARARGS, "..."},
    {"stealth_compact_get_transaction_hash",  bitprim_native_stealth_compact_get_transaction_hash, METH_VARARGS, "..."},
    {"stealth_compact_get_public_key_hash",  bitprim_native_stealth_compact_get_public_key_hash, METH_VARARGS, "..."},

    {"stealth_compact_list_destruct",  bitprim_native_chain_stealth_compact_list_destruct, METH_VARARGS, "..."},
    {"stealth_compact_list_count",  bitprim_native_chain_stealth_compact_list_count, METH_VARARGS, "..."},
    {"stealth_compact_list_nth",  bitprim_native_chain_stealth_compact_list_nth, METH_VARARGS, "..."},

    //{"long_hash_t_to_str",  bitprim_native_long_hash_t_to_str, METH_VARARGS, "..."},
    //{"long_hash_t_free",  bitprim_native_long_hash_t_free, METH_VARARGS, "..."},

    {NULL, NULL, 0, NULL}        /* Sentinel */
};

struct module_state {
    PyObject *error;
};

#if PY_MAJOR_VERSION >= 3
#define GETSTATE(m) ((struct module_state*)PyModule_GetState(m))
#else //PY_MAJOR_VERSION >= 3
#define GETSTATE(m) (&_state)
static struct module_state _state;
#endif //PY_MAJOR_VERSION >= 3

#if PY_MAJOR_VERSION >= 3

static 
int myextension_traverse(PyObject *m, visitproc visit, void *arg) {
    Py_VISIT(GETSTATE(m)->error);
    return 0;
}

static 
int myextension_clear(PyObject *m) {
    Py_CLEAR(GETSTATE(m)->error);
    return 0;
}

static 
struct PyModuleDef moduledef = {
        PyModuleDef_HEAD_INIT,
        "bitprim_native",
        NULL,
        sizeof(struct module_state),
        BitprimNativeMethods,
        NULL,
        myextension_traverse,
        myextension_clear,
        NULL
};

#define INITERROR return NULL

PyMODINIT_FUNC
PyInit_bitprim_native(void)


#else /* PY_MAJOR_VERSION >= 3 */

#define INITERROR return

void /*PyMODINIT_FUNC*/
initbitprim_native(void)

#endif /* PY_MAJOR_VERSION >= 3 */


{

    // Make sure the GIL has been created since we need to acquire it in our
    // callback to safely call into the python application.
    if (! PyEval_ThreadsInitialized()) {
        PyEval_InitThreads();
    }


#if PY_MAJOR_VERSION >= 3
    PyObject *module = PyModule_Create(&moduledef);
#else
    PyObject *module = Py_InitModule("bitprim_native", BitprimNativeMethods);
    // (void) Py_InitModule("bitprim_native", BitprimNativeMethods);
#endif

    if (module == NULL) {
        INITERROR;
    }

    struct module_state *st = GETSTATE(module);

    st->error = PyErr_NewException((char*)"myextension.Error", NULL, NULL);
    
    if (st->error == NULL) {
        Py_DECREF(module);
        INITERROR;
    }

#if PY_MAJOR_VERSION >= 3
    return module;
#endif
}


#ifdef __cplusplus
} // extern "C"
#endif  


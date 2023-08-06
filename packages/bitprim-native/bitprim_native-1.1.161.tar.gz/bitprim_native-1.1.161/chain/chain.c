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

#include "chain.h"
#include <bitprim/nodecint.h>
#include "../utils.h" //TODO(fernando): poner bien el dir del header


#ifdef __cplusplus
extern "C" {  
#endif  

// -------------------------------------------------------------------
// fetch_block
// -------------------------------------------------------------------

void chain_fetch_block_handler(chain_t chain, void* ctx, error_code_t error , block_t block, uint64_t /*size_t*/ h) {
    PyGILState_STATE gstate;
    gstate = PyGILState_Ensure();

    PyObject* py_callback = ctx;

    PyObject* py_block = to_py_obj(block);

    PyObject* arglist = Py_BuildValue("(iOK)", error, py_block, h);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    Py_XDECREF(py_callback);  // Dispose of the call

    PyGILState_Release(gstate);
}

PyObject* bitprim_native_chain_fetch_block_by_height(PyObject* self, PyObject* args){
    PyObject* py_chain;
    uint64_t py_height;
    PyObject* py_callback;

    if ( ! PyArg_ParseTuple(args, "OKO", &py_chain, &py_height, &py_callback)) {
        return NULL;
    }

    if (!PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }    

    chain_t chain = (chain_t)get_ptr(py_chain);
    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_block_by_height(chain, py_callback, py_height, chain_fetch_block_handler);
    Py_RETURN_NONE;
}

PyObject* bitprim_native_chain_fetch_block_by_hash(PyObject* self, PyObject* args){
    PyObject* py_chain;
    char* py_hash;
    size_t py_hash_size;
    PyObject* py_callback;

#if PY_MAJOR_VERSION >= 3
    if ( ! PyArg_ParseTuple(args, "Oy#O", &py_chain, &py_hash, &py_hash_size, &py_callback)) {
#else
    if ( ! PyArg_ParseTuple(args, "Os#O", &py_chain, &py_hash, &py_hash_size, &py_callback)) {
#endif
        return NULL;
    }

    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    hash_t hash;
    memcpy(hash.hash, py_hash, 32);

    chain_t chain = (chain_t)get_ptr(py_chain);
    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_block_by_hash(chain, py_callback, hash, chain_fetch_block_handler);
    Py_RETURN_NONE;
}


// -------------------------------------------------------------------
// fetch_merkle_block
// -------------------------------------------------------------------

void chain_fetch_merkle_block_handler(chain_t chain, void* ctx, error_code_t error, merkle_block_t merkle, uint64_t /*size_t*/ h) {
    PyObject* py_callback = ctx;

    PyObject* py_merkle = to_py_obj(merkle);

    PyObject* arglist = Py_BuildValue("(iOK)", error, py_merkle, h);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    Py_XDECREF(py_callback);  // Dispose of the call
}

PyObject* bitprim_native_chain_fetch_merkle_block_by_height(PyObject* self, PyObject* args){
    PyObject* py_chain;
    uint64_t py_height;
    PyObject* py_callback;
   
 if ( ! PyArg_ParseTuple(args, "OKO", &py_chain, &py_height, &py_callback)) {
         return NULL;
    }

    if (!PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }    

    chain_t chain = (chain_t)get_ptr(py_chain);
    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_merkle_block_by_height(chain, py_callback, py_height, chain_fetch_merkle_block_handler);
    Py_RETURN_NONE;
}


PyObject* bitprim_native_chain_fetch_merkle_block_by_hash(PyObject* self, PyObject* args){
    PyObject* py_chain;
    char* py_hash;
    size_t py_hash_size;
    PyObject* py_callback;

#if PY_MAJOR_VERSION >= 3
    if ( ! PyArg_ParseTuple(args, "Oy#O", &py_chain, &py_hash, &py_hash_size, &py_callback)) {
#else
    if ( ! PyArg_ParseTuple(args, "Os#O", &py_chain, &py_hash, &py_hash_size, &py_callback)) {
#endif
        return NULL;
    }

    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    hash_t hash;
    memcpy(hash.hash, py_hash, 32);

    chain_t chain = (chain_t)get_ptr(py_chain);
    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_merkle_block_by_hash(chain, py_callback, hash, chain_fetch_merkle_block_handler);

    Py_RETURN_NONE;
}

// -------------------------------------------------------------------
// fetch block header
// -------------------------------------------------------------------

void chain_fetch_block_header_handler(chain_t chain, void* ctx, error_code_t error , header_t header, uint64_t /*size_t*/ h) {
    PyObject* py_callback = ctx;

    PyObject* py_header = to_py_obj(header);

    PyObject* arglist = Py_BuildValue("(iOK)", error, py_header, h);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    Py_XDECREF(py_callback);  // Dispose of the call
}

PyObject* bitprim_native_chain_fetch_block_header_by_height(PyObject* self, PyObject* args){
    PyObject* py_chain;
    uint64_t py_height;
    PyObject* py_callback;

    if ( ! PyArg_ParseTuple(args, "OKO", &py_chain, &py_height, &py_callback)) {
        return NULL;
    }

    if (!PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }    

    chain_t chain = (chain_t)get_ptr(py_chain);
    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_block_header_by_height(chain, py_callback, py_height, chain_fetch_block_header_handler);

    Py_RETURN_NONE;
}

PyObject* bitprim_native_chain_fetch_block_header_by_hash(PyObject* self, PyObject* args){
    PyObject* py_chain;
    char* py_hash;
    size_t py_hash_size;
    PyObject* py_callback;

#if PY_MAJOR_VERSION >= 3
    if ( ! PyArg_ParseTuple(args, "Oy#O", &py_chain, &py_hash, &py_hash_size, &py_callback)) {
#else
    if ( ! PyArg_ParseTuple(args, "Os#O", &py_chain, &py_hash, &py_hash_size, &py_callback)) {
#endif
        return NULL;
    }

    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    hash_t hash;
    memcpy(hash.hash, py_hash, 32);

    chain_t chain = (chain_t)get_ptr(py_chain);
    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_block_header_by_hash(chain, py_callback, hash, chain_fetch_block_header_handler);
    Py_RETURN_NONE;
}


// ---------------------------------------------------------
// chain_fetch_last_height
// ---------------------------------------------------------

void chain_fetch_last_height_handler(chain_t chain, void* ctx, error_code_t error, uint64_t /*size_t*/ h) {
    PyGILState_STATE gstate;
    gstate = PyGILState_Ensure();

    PyObject* py_callback = ctx;

    PyObject* arglist = Py_BuildValue("(iK)", error, h);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    Py_XDECREF(py_callback);  // Dispose of the call

    PyGILState_Release(gstate);
}

PyObject* bitprim_native_chain_fetch_last_height(PyObject* self, PyObject* args) {
    PyObject* py_chain;
    PyObject* py_callback;

    if ( ! PyArg_ParseTuple(args, "OO:set_callback", &py_chain, &py_callback)) {
        return NULL;
    }

    if (!PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }    

    chain_t chain = (chain_t)get_ptr(py_chain);
    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_last_height(chain, py_callback, chain_fetch_last_height_handler);

    Py_RETURN_NONE;
}

// ---------------------------------------------------------
// chain_fetch_history
// ---------------------------------------------------------

void chain_fetch_history_handler(chain_t chain, void* ctx, error_code_t error, history_compact_list_t history_list) {

    PyObject* py_callback = ctx;
    PyObject* py_history_list = to_py_obj(history_list);

    // PyCapsule_GetPointer(py_history_list, NULL); //TODO: ????
    PyCapsule_IsValid(py_history_list, NULL);

    PyObject* arglist = Py_BuildValue("(iO)", error, py_history_list);

    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);
    Py_XDECREF(py_callback);  // Dispose of the call
}

PyObject* bitprim_native_chain_fetch_history(PyObject* self, PyObject* args) {
    PyObject* py_chain;
    char* address_str;
    uint64_t py_limit;
    uint64_t py_from_height;
    PyObject* py_callback;

    if ( ! PyArg_ParseTuple(args, "OsKKO:set_callback", &py_chain, &address_str, &py_limit, &py_from_height, &py_callback)) {
        return NULL;
    }

    if (!PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }    

    chain_t chain = (chain_t)get_ptr(py_chain);

    Py_XINCREF(py_callback);         /* Add a reference to new callback */

    payment_address_t pa = chain_payment_address_construct_from_string(address_str);
    chain_fetch_history(chain, py_callback, pa, py_limit, py_from_height, chain_fetch_history_handler);
    // payment_address_destruct(pa); //TODO!

    Py_RETURN_NONE;
}

// ---------------------------------------------------------
// chain_fetch_block_height
// ---------------------------------------------------------

void chain_block_height_fetch_handler(chain_t chain, void* ctx, error_code_t error, uint64_t /*size_t*/ h) {

    PyObject* py_callback = ctx;

    PyObject* arglist = Py_BuildValue("(iK)", error, h);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    Py_XDECREF(py_callback);  // Dispose of the call
}

PyObject* bitprim_native_chain_fetch_block_height(PyObject* self, PyObject* args) {
    PyObject* py_chain;
    char* py_hash;
    size_t py_hash_size;
    PyObject* py_callback;

#if PY_MAJOR_VERSION >= 3
    if ( ! PyArg_ParseTuple(args, "Oy#O", &py_chain, &py_hash, &py_hash_size, &py_callback)) {
#else
    if ( ! PyArg_ParseTuple(args, "Os#O", &py_chain, &py_hash, &py_hash_size, &py_callback)) {
#endif
        return NULL;
    }

    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }    

    chain_t chain = (chain_t)get_ptr(py_chain);
    
    hash_t hash;
    memcpy(hash.hash, py_hash, 32);

    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_block_height(chain, py_callback, hash, chain_block_height_fetch_handler);
    Py_RETURN_NONE;
}


// ---------------------------------------------------------
// stealth_history
// ---------------------------------------------------------

void chain_stealth_fetch_handler(chain_t chain, void* ctx, error_code_t error, stealth_compact_list_t stealth_list) {
    PyObject* py_callback = ctx;

    PyObject* py_stealth_list = to_py_obj(stealth_list);
    // /*void* ptr_void =*/ PyCapsule_GetPointer(py_stealth_list, NULL);
    /*int is_valid =*/ PyCapsule_IsValid(py_stealth_list, NULL); //TODO(fernando): chequear esto!

    PyObject* arglist = Py_BuildValue("(iO)", error, py_stealth_list);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    Py_XDECREF(py_callback);  // Dispose of the call
}

PyObject* bitprim_native_chain_fetch_stealth(PyObject* self, PyObject* args) {
    PyObject* py_chain;
    PyObject* py_filter;
    uint64_t py_from_height;
    PyObject* py_callback;

    if ( ! PyArg_ParseTuple(args, "OOKO:set_callback", &py_chain, &py_filter, &py_from_height, &py_callback)) {
        return NULL;
    }

    if (!PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }    

    chain_t chain = (chain_t)get_ptr(py_chain);
    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    binary_t binary_filter = (binary_t)get_ptr(py_filter);
    chain_fetch_stealth(chain, py_callback, binary_filter, py_from_height, chain_stealth_fetch_handler);
    Py_RETURN_NONE;
}

void chain_fetch_transaction_handler(chain_t chain, void* ctx, error_code_t error, transaction_t transaction, uint64_t index, uint64_t height) {
    PyGILState_STATE gstate;
    gstate = PyGILState_Ensure();

    PyObject* py_callback = ctx;
    PyObject* py_transaction = to_py_obj(transaction);

    PyObject* arglist = Py_BuildValue("(iOKK)", error, py_transaction, index, height);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    Py_XDECREF(py_callback);  // Dispose of the call

    PyGILState_Release(gstate);
}

PyObject* bitprim_native_chain_fetch_transaction(PyObject* self, PyObject* args) {
    PyObject* py_chain;
    char* py_hash;
    size_t py_hash_size;
    int py_require_confirmed;
    PyObject* py_callback;

#if PY_MAJOR_VERSION >= 3
    if ( ! PyArg_ParseTuple(args, "Oy#iO", &py_chain, &py_hash, &py_hash_size, &py_require_confirmed,&py_callback)) {
#else
    if ( ! PyArg_ParseTuple(args, "Os#iO", &py_chain, &py_hash, &py_hash_size, &py_require_confirmed,&py_callback)) {
#endif
        return NULL;
    }

    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    hash_t hash;
    memcpy(hash.hash, py_hash, 32);

    chain_t chain = (chain_t)get_ptr(py_chain);
    Py_XINCREF(py_callback);
    chain_fetch_transaction(chain, py_callback, hash, py_require_confirmed, chain_fetch_transaction_handler);

    Py_RETURN_NONE;
}


// Note: Removed on 3.3.0
// void chain_fetch_output_handler(chain_t chain, void* ctx, error_code_t error, output_t output) {
//     PyObject* py_callback = ctx;
//     PyObject* py_output = to_py_obj(output);

//     PyObject* arglist = Py_BuildValue("(iO)", error, py_output);
//     PyObject_CallObject(py_callback, arglist);
//     Py_DECREF(arglist);    
//     Py_XDECREF(py_callback);  // Dispose of the call
// }


// PyObject* bitprim_native_chain_fetch_output(PyObject* self, PyObject* args){
//     PyObject* py_chain;
//     char* py_hash;
//     size_t py_hash_size;
//     uint32_t py_index;
//     int py_require_confirmed;
//     PyObject* py_callback;

// #if PY_MAJOR_VERSION >= 3
//     if ( ! PyArg_ParseTuple(args, "Oy#IiO", &py_chain, &py_hash, &py_hash_size, &py_index, &py_require_confirmed, &py_callback)) {
// #else
//     if ( ! PyArg_ParseTuple(args, "Os#IiO", &py_chain, &py_hash, &py_hash_size, &py_index, &py_require_confirmed, &py_callback)) {
// #endif
//         return NULL;
//     }

//     if ( ! PyCallable_Check(py_callback)) {
//         PyErr_SetString(PyExc_TypeError, "parameter must be callable");
//         return NULL;
//     }

//     hash_t hash;
//     memcpy(hash.hash, py_hash, 32);

//     chain_t chain = (chain_t)get_ptr(py_chain);
//     Py_XINCREF(py_callback);
//     chain_fetch_output(chain, py_callback, hash, py_index, py_require_confirmed, chain_fetch_output_handler);

//     Py_RETURN_NONE;
// }

void chain_fetch_transaction_position_handler(chain_t chain, void* ctx, error_code_t error, uint64_t position, uint64_t height) {
    PyObject* py_callback = ctx;
    PyObject* arglist = Py_BuildValue("(iKK)", error, position, height);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    Py_XDECREF(py_callback);  // Dispose of the call
}


PyObject* bitprim_native_chain_fetch_transaction_position(PyObject* self, PyObject* args){
    PyObject* py_chain;
    char* py_hash;
    size_t py_hash_size;
    int py_require_confirmed;
    PyObject* py_callback;

#if PY_MAJOR_VERSION >= 3
    if ( ! PyArg_ParseTuple(args, "Oy#iO", &py_chain, &py_hash, &py_hash_size, &py_require_confirmed,&py_callback)) {
#else
    if ( ! PyArg_ParseTuple(args, "Os#iO", &py_chain, &py_hash, &py_hash_size, &py_require_confirmed,&py_callback)) {
#endif
        return NULL;
    }

    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    hash_t hash;
    memcpy(hash.hash, py_hash, 32);
    chain_t chain = (chain_t)get_ptr(py_chain);
    Py_XINCREF(py_callback);
    chain_fetch_transaction_position(chain, py_callback, hash, py_require_confirmed, chain_fetch_transaction_position_handler);
    Py_RETURN_NONE;
}

void chain_organize_handler(chain_t chain, void* ctx, error_code_t error) {
    PyObject* py_callback = ctx;
    PyObject* arglist = Py_BuildValue("(i)", error);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    Py_XDECREF(py_callback);  // Dispose of the call
}

PyObject* bitprim_native_chain_organize_block(PyObject* self, PyObject* args){
    PyObject* py_chain;
    PyObject* py_block;
    PyObject* py_callback;

    if ( ! PyArg_ParseTuple(args, "OOO", &py_chain, &py_block, &py_callback)) {
        return NULL;
    }

    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    chain_t chain = (chain_t)get_ptr(py_chain);
    block_t block = (block_t)get_ptr(py_block);

    Py_XINCREF(py_callback);
    chain_organize_block(chain, py_callback, block, chain_organize_handler);
    Py_RETURN_NONE;
}

PyObject* bitprim_native_chain_organize_transaction(PyObject* self, PyObject* args){
    PyObject* py_chain;
    PyObject* py_transaction;
    PyObject* py_callback;

    if ( ! PyArg_ParseTuple(args, "OOO", &py_chain, &py_transaction, &py_callback)) {
        return NULL;
    }

    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    chain_t chain = (chain_t)get_ptr(py_chain);
    transaction_t transaction = (transaction_t)get_ptr(py_transaction);

    Py_XINCREF(py_callback);
    chain_organize_transaction(chain, py_callback, transaction, chain_organize_handler);
    Py_RETURN_NONE;
}

void chain_validate_tx_handler(chain_t chain, void* ctx, error_code_t error, char const* msg) {
    PyObject* py_callback = ctx;
    PyObject* arglist = Py_BuildValue("(is)", error, msg);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    Py_XDECREF(py_callback);  // Dispose of the call
}

PyObject* bitprim_native_chain_validate_tx(PyObject* self, PyObject* args){
    PyObject* py_chain;
    PyObject* py_transaction;
    PyObject* py_callback;

    if ( ! PyArg_ParseTuple(args, "OOO", &py_chain, &py_transaction, &py_callback)) {
        return NULL;
    }

    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    chain_t chain = (chain_t)get_ptr(py_chain);
    transaction_t transaction = (transaction_t)get_ptr(py_transaction);

    Py_XINCREF(py_callback);
    chain_validate_tx(chain, py_callback, transaction, chain_validate_tx_handler);


// chain/chain.c:587:56: warning: incompatible pointer types passing 
// 'void (chain_t, void *, int, char *)' 
// (aka 'void (void *, void *, int, char *)') 
// to parameter of type 'validate_tx_handler_t' (aka 'void (*)(void *, void *, int, const char *)') [-Wincompatible-pointer-types]
// chain_validate_tx(chain, py_callback, transaction, chain_validate_tx_handler);
//                                                     ^~~~~~~~~~~~~~~~~~~~~~~~~
// bitprim/include/bitprim/nodecint/chain/chain.h:213:90: note: passing argument to parameter 'handler' here    

    Py_RETURN_NONE;
}


void chain_fetch_compact_block_handler(chain_t chain, void* ctx, error_code_t error , compact_block_t compact, uint64_t /*size_t*/ h) {
    PyObject* py_callback = ctx;
    PyObject* py_compact = to_py_obj(compact);

    PyObject* arglist = Py_BuildValue("(iOK)", error, py_compact, h);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    Py_XDECREF(py_callback);  // Dispose of the call
}

PyObject* bitprim_native_chain_fetch_compact_block_by_height(PyObject* self, PyObject* args){
    PyObject* py_chain;
    uint64_t py_height;
    PyObject* py_callback;
    if ( ! PyArg_ParseTuple(args, "OKO", &py_chain, &py_height, &py_callback)) {
        return NULL;
    }

    if (!PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }    

    chain_t chain = (chain_t)get_ptr(py_chain);
    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_compact_block_by_height(chain, py_callback, py_height, chain_fetch_compact_block_handler);
    Py_RETURN_NONE;
}



PyObject* bitprim_native_chain_fetch_compact_block_by_hash(PyObject* self, PyObject* args){
    PyObject* py_chain;
    char* py_hash;
    size_t py_hash_size;
    PyObject* py_callback;

#if PY_MAJOR_VERSION >= 3
    if ( ! PyArg_ParseTuple(args, "Oy#O", &py_chain, &py_hash, &py_hash_size, &py_callback)) {
#else
    if ( ! PyArg_ParseTuple(args, "Os#O", &py_chain, &py_hash, &py_hash_size, &py_callback)) {
#endif
        return NULL;
    }

    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    hash_t hash;
    memcpy(hash.hash, py_hash, 32);

    chain_t chain = (chain_t)get_ptr(py_chain);
    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_compact_block_by_hash(chain, py_callback, hash, chain_fetch_compact_block_handler);

    Py_RETURN_NONE;
}


void chain_fetch_spend_handler(chain_t chain, void* ctx, error_code_t error , point_t point) {
    PyObject* py_callback = ctx;
    PyObject* py_point = to_py_obj(point);

    PyObject* arglist = Py_BuildValue("(iO)", error, py_point);
    PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    Py_XDECREF(py_callback);  // Dispose of the call
}

PyObject* bitprim_native_chain_fetch_spend(PyObject* self, PyObject* args){
    PyObject* py_chain;
    PyObject* py_output_point;
    PyObject* py_callback;

    if ( ! PyArg_ParseTuple(args, "OOO", &py_chain, &py_output_point, &py_callback)) {
        return NULL;
    }

    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    chain_t chain = (chain_t)get_ptr(py_chain);
    output_point_t output_point = (output_point_t)get_ptr(py_output_point);
    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_fetch_spend(chain, py_callback, output_point, chain_fetch_spend_handler);
    Py_RETURN_NONE;
}

int chain_subscribe_blockchain_handler(executor_t exec, chain_t chain, void* ctx, error_code_t error, uint64_t fork_height, block_list_t blocks_incoming, block_list_t blocks_replaced) {
    
    //TODO(fernando): hardcoded error code, libbitcoin::error::service_stopped
    // if (exec->actual.stopped() || error == 1) {
    if (executor_stopped(exec) != 0 || error == 1) {
        return 0;
    }

    PyGILState_STATE gstate;
    gstate = PyGILState_Ensure();

    PyObject* py_callback = ctx;
    
    PyObject* py_blocks_incoming = blocks_incoming != NULL ? to_py_obj(blocks_incoming) : Py_None;
    PyObject* py_blocks_replaced = blocks_replaced != NULL ? to_py_obj(blocks_replaced) : Py_None;
    PyObject* arglist = Py_BuildValue("(iKOO)", error, fork_height, py_blocks_incoming, py_blocks_replaced);

    PyObject* ret = PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    
    if (ret != NULL) {
        int truthy = PyObject_IsTrue(ret);
        Py_DECREF(ret);
        
        PyGILState_Release(gstate);
            
        return truthy == 1 ? 1 : 0;

    }

    PyGILState_Release(gstate);
    return 0;
}

PyObject* bitprim_native_chain_subscribe_blockchain(PyObject* self, PyObject* args){
    PyObject* py_exec;
    PyObject* py_chain;
    PyObject* py_callback;

    if ( ! PyArg_ParseTuple(args, "OOO:set_callback", &py_exec, &py_chain, &py_callback)) {
        return NULL;
    }

    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    executor_t exec = cast_executor(py_exec);
    chain_t chain = (chain_t)get_ptr(py_chain);
    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    
    chain_subscribe_blockchain(exec, chain, py_callback, chain_subscribe_blockchain_handler);
    Py_RETURN_NONE;
}

int chain_subscribe_transaction_handler(executor_t exec, chain_t chain, void* ctx, error_code_t error, transaction_t tx) {

    //TODO(fernando): hardcoded error code, libbitcoin::error::service_stopped
    // if (exec->actual.stopped() || error == 1) {
    if (executor_stopped(exec) != 0 || error == 1) {
        return 0;
    }
    
    PyGILState_STATE gstate;
    gstate = PyGILState_Ensure();

    PyObject* py_callback = ctx;
    PyObject* py_transaction = to_py_obj(tx);

    PyObject* arglist = Py_BuildValue("(iO)", error, py_transaction);
    PyObject* ret = PyObject_CallObject(py_callback, arglist);
    Py_DECREF(arglist);    
    //Py_XDECREF(py_callback);  // Dispose of the call


    if (ret != NULL) {
#if PY_MAJOR_VERSION >= 3
        int py_ret = (int)PyLong_AsLong(ret); //TODO(fernando): warning! convertion.. how to conver PyObject to int
#else /* PY_MAJOR_VERSION >= 3 */
        int py_ret = (int)PyInt_AsLong(ret); //TODO(fernando): warning! convertion.. how to conver PyObject to int
#endif /* PY_MAJOR_VERSION >= 3 */


        Py_DECREF(ret);

        PyGILState_Release(gstate);
        
        return py_ret;
    }

    PyGILState_Release(gstate);
    return 0;
}

PyObject* bitprim_native_chain_subscribe_transaction(PyObject* self, PyObject* args){
    PyObject* py_exec;
    PyObject* py_chain;
    PyObject* py_callback;

    if ( ! PyArg_ParseTuple(args, "OOO:set_callback", &py_exec, &py_chain, &py_callback)) {
        return NULL;
    }

    if ( ! PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    executor_t exec = cast_executor(py_exec);
    chain_t chain = (chain_t)get_ptr(py_chain);
    Py_XINCREF(py_callback);         /* Add a reference to new callback */
    chain_subscribe_transaction(exec, chain, py_callback, chain_subscribe_transaction_handler);
    Py_RETURN_NONE;
}

PyObject* bitprim_native_chain_unsubscribe(PyObject* self, PyObject* args){
    PyObject* py_chain;

    if ( ! PyArg_ParseTuple(args, "O", &py_chain)) {
        return NULL;
    }

    chain_t chain = (chain_t)get_ptr(py_chain);
    
    chain_unsubscribe(chain);
    Py_RETURN_NONE;
}

#ifdef __cplusplus
} //extern "C"
#endif  


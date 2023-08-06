#include "input.h"

#ifdef __cplusplus
extern "C" {  
#endif  

PyObject* bitprim_native_chain_input_is_valid(PyObject* self, PyObject* args){
    PyObject* py_input;
    
    if ( ! PyArg_ParseTuple(args, "O", &py_input)) {
        return NULL;
    }

    input_t input = (input_t)get_ptr(py_input);
    int res = chain_input_is_valid(input);
    return Py_BuildValue("i", res);
}

PyObject* bitprim_native_chain_input_is_final(PyObject* self, PyObject* args){
    PyObject* py_input;
    
    if ( ! PyArg_ParseTuple(args, "O", &py_input)) {
        return NULL;
    }

    input_t input = (input_t)get_ptr(py_input);
    int res = chain_input_is_final(input);
    return Py_BuildValue("i", res);
}

PyObject* bitprim_native_chain_input_serialized_size(PyObject* self, PyObject* args){
    PyObject* py_input;
    int py_wire;
    
    if ( ! PyArg_ParseTuple(args, "Oi", &py_input, &py_wire)) {
        return NULL;
    }

    input_t input = (input_t)get_ptr(py_input);
    uint64_t res = chain_input_serialized_size(input, py_wire);
    return Py_BuildValue("K", res);
}

PyObject* bitprim_native_chain_input_sequence(PyObject* self, PyObject* args){
    PyObject* py_input;
    
    if ( ! PyArg_ParseTuple(args, "O", &py_input)) {
        return NULL;
    }

    input_t input = (input_t)get_ptr(py_input);
    uint32_t res = chain_input_sequence(input);
    return Py_BuildValue("I", res);
}

PyObject* bitprim_native_chain_input_signature_operations(PyObject* self, PyObject* args){
    PyObject* py_input;
    int py_bip16_active;
    
    if ( ! PyArg_ParseTuple(args, "Oi", &py_input, &py_bip16_active)) {
        return NULL;
    }

    input_t input = (input_t)get_ptr(py_input);
    uint64_t res = chain_input_signature_operations(input, py_bip16_active);
    return Py_BuildValue("K", res);
}

PyObject* bitprim_native_chain_input_destruct(PyObject* self, PyObject* args){
    PyObject* py_input;
    
    if ( ! PyArg_ParseTuple(args, "O", &py_input)) {
        return NULL;
    }

    input_t input = (input_t)get_ptr(py_input);
    chain_input_destruct(input);
    Py_RETURN_NONE;
}


PyObject* bitprim_native_chain_input_script(PyObject* self, PyObject* args){
    PyObject* py_input;
    
    if ( ! PyArg_ParseTuple(args, "O", &py_input)) {
        return NULL;
    }

    input_t input = (input_t)get_ptr(py_input);
    script_t script = chain_input_script(input);
    return to_py_obj(script);
}

PyObject* bitprim_native_chain_input_previous_output(PyObject* self, PyObject* args){
    PyObject* py_input;
    
    if ( ! PyArg_ParseTuple(args, "O", &py_input)) {
        return NULL;
    }

    input_t input = (input_t)get_ptr(py_input);
    output_point_t res = chain_input_previous_output(input);
    return to_py_obj(res);
}

/*
PyObject* bitprim_native_chain_input_get_hash(PyObject* self, PyObject* args){
    PyObject* py_input;
    
    if ( ! PyArg_ParseTuple(args, "O", &py_input)) {
        return NULL;
    }

    input_t input = (input_t)get_ptr(py_input);
    hash_t res = chain_input_get_hash(input);
    return PyByteArray_FromStringAndSize(res.hash, 32);

}
*/

/*
PyObject* bitprim_native_chain_input_get_index(PyObject* self, PyObject* args){
    PyObject* py_input;
    
    if ( ! PyArg_ParseTuple(args, "O", &py_input)) {
        return NULL;
    }

    input_t input = (input_t)get_ptr(py_input);
    uint32_t res = chain_input_get_index(input);
    return Py_BuildValue("L", res);

}
*/



// uint8_t const* chain_input_to_data(input_t input, int /*bool*/ wire, uint64_t* /*size_t*/ out_size) {
//     auto input_data = chain_input_const_cpp(input).to_data(wire);
//     auto* ret = (uint8_t*)malloc((input_data.size()) * sizeof(uint8_t)); // NOLINT
//     std::copy_n(input_data.begin(), input_data.size(), ret);
//     *out_size = input_data.size();
//     return ret;
// }

PyObject* bitprim_native_chain_input_to_data(PyObject* self, PyObject* args) {
    PyObject* py_input;
    int py_wire;
    
    if ( ! PyArg_ParseTuple(args, "Oi", &py_input, &py_wire)) {
        return NULL;
    }

    input_t input = (input_t)get_ptr(py_input);
    uint64_t /*size_t*/ out_n;
    uint8_t* data = (uint8_t*)chain_input_to_data(input, py_wire, &out_n);
    
#if PY_MAJOR_VERSION >= 3
    return Py_BuildValue("y#", data, out_n);    
#else
    return Py_BuildValue("s#", data, out_n);    
#endif
    
}


#ifdef __cplusplus
} //extern "C"
#endif  

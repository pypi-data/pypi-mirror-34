/** **************************************************************************
 * \brief Utility functions to used for creating the PyDim module.
 * These are used primarily for converting between DIM C buffers and python
 * objects.
 *
 * \authors M. Frank, N. Neufeld, R. Stoica
 * \date Nov. 2007 - September 2008
 *
 * Various defines necessary for converting between the dim buffers and Python
 * objects.
 *
 * TODO: All the tests until were done communicating between the same
 * architectures (32 bits and 64 bits). Not sure DIM supports communicating
 * between platforms that have different sizes for the basic types.
 * Anyway I can't fix this if DIM doesn't support this.
 * *************************************************************************/

#ifndef PYDIM_UTILS_H
#define PYDIM_UTILS_H

// includes
extern "C" {
#include <Python.h>
#include <limits.h>
#include "structmember.h"
}
#include <dic.hxx>
#include <cstdlib>
#include <cstdio>
#include <map>
#include <string>


#ifdef _WIN32
 #include <cstdarg>
  static inline void ___print(const char* fmt,...)
  {
    va_list args; va_start(args,fmt);
    vprintf(fmt,args); printf("\n"); va_end(args);
  }
 #define print printf("DIM Wrapper: %s:%u ::%s: ", __FILE__, __LINE__, __FUNCTION__); ___print
#else
 #define print(...) printf("DIM Wrapper: %s:%u ::%s: ", __FILE__, __LINE__, __FUNCTION__); printf(__VA_ARGS__); printf("\n");
#endif

#ifdef __DEBUG
 #define debug print
 #define debugPyObject printPyObject
#else
 #define debug(...) /* __VA_ARGS__ */
 #define debugPyObject(...) /* __VA_ARGS__ */
#endif

#ifndef HOST_NAME_MAX
#define HOST_NAME_MAX _POSIX_HOST_NAME_MAX
#endif

#ifndef Py_RETURN_NONE
#define Py_RETURN_NONE do { Py_INCREF(Py_None); return Py_None; } while(0);
#endif
#define errmsg(x) do { fprintf(stderr, "%s: %s\n", __FUNCTION__, x); } while(0);

#define _DIM_INT 0
#define _DIM_INT_LEN 4

#define _DIM_FLOAT 1
#define _DIM_FLOAT_LEN 4

#define _DIM_DOUBLE 2
#define _DIM_DOUBLE_LEN 8

#define _DIM_XTRA 3
#define _DIM_XTRA_LEN 8

#define _DIM_STRING 4
#define _DIM_CHAR_LEN 1

#define _DIM_SHORT 5
#define _DIM_SHORT_LEN 2

#define _DIM_LONG 6
#define _DIM_LONG_LEN 4

#define MUL_INFINITE -1
/* multiplicity == MUL_INFINITE  means an arbitrary amount of data types
 *                  (e.g. ..;I)
 * multiplicity == 0 is an illegal value and will not be returned by this
 *                 function
 */


 /**
 * This class manages a cache for the commands / service format
 * in order to not do a DNS call at each command call
 */
 class CacheFormat{
   private:
     std::map<std::string,std::string> cache;
     bool activated;

   public:
     /**
     * Constructor of CacheFormat
     */
     CacheFormat();
     /**
     * Returns the format corresponding to the named of service/command passed in parameter
     * @param service_command_name The service / command name to get the format of
     * @return The format of the service / command name if the service / command is in the cache. An empty string is returned if not.
     */
     std::string getFormat(std::string service_command_name);

     /**
     * Insert the format of the service/command in the cache.
     * @param service_command_name The name of the service/command to store the associated format
     * @param format The format associated to the service/command passed as first parameter
     */
     void insertFormat(std::string service_command_name,std::string format);

     /**
     * Deactivates the cache
     */
     void deactivate(){this->activated = false;}
     /**
     * Activates the cache
     */
     void activate(){this->activated = true;}

     /**
     * Returns true if the cache is activated, false if not
     */
     bool isActivated() const {return this->activated;}

     /**
     * Clears the cache
     */
     void flush();

     /**
     * Destructor of the cache
     */
     ~CacheFormat();
 };


 /* **************************************************************************
 * Cache of commands / services format definitions
 * *************************************************************************/
 /*typedef std::map<std::string,std::string> CacheFormat;*/

 /* *******************************
 * Commands and services cache
 * ********************************/
 /* Cache for commands format*/
 extern CacheFormat cacheCmndFormat;


 /**
 *  This function activates the cache where format of commands are stored
 */
 void activate_cmnd_format_cache();

 /**
 * This function reset the cache where format of commands are stored
 */
 void reset_cmnd_format_cache();


  /**
  *  This function deactivate the cache where format of commands are stored
  */
  void deactivate_cmnd_format_cache();

  /**
  *  This function check if the cache where format of commands are stored is activated or not
  *  Output: 1 if cache is activated, 0 if not
  */
  int cmnd_cache_activated();

  /**
  *  This function retieve the format of the command / service that name is passed in parameter
  *  from the cache passed in parameter
  *  Input: service_command_name, the name of the command / service to get the format
  *         value_returned : the address of a char pointer to put the result inside. The char pointer should be NULL
  *         or previously allocated with malloc (will be free and reallocated with the correct size)
  *         cache : the cache to get the format from
  *  If the format could not have been retrieved from the cache, the char pointer pointed
  *  by value_returned will be NULL
  */
  void get_format_from_cache(char *service_command_name,char **value_returned,CacheFormat &cache);

  /**
  *  This function insert the command / service name and its format in the cache
  *  passed in parameter
  *  Input:
  *    service_command_name: The name of the command / service to store the format
  *    format: The format of the command / service to store
  *    cache : The cache to store the command / service format in
  */
  void insert_format_in_cache(char *service_command_name, char *format,CacheFormat &cache);


  /* **************************************************************************
  * End of cache of commands format definitions
  * *************************************************************************/

 /* **************************************************************************
  * Utility functions
  * *************************************************************************/
 #ifndef DIMCPP_MODULE
 int listOrTuple2Int(PyObject* pyObj, int** buffer);
 PyObject* stringList_to_tuple (char* services);
 PyObject* pyCallFunction (PyObject* pyFunc, PyObject* args);
 #endif

 #ifdef __DEBUG
 void printPyObject(PyObject *object);
 void printDimBuf(const char *buf, int size);
 PyObject* list2Tuple(PyObject* list);
 #endif

 #ifndef DIMC_MODULE
 int verify_dim_format(const char *format);
 int next_element(const char *schema, unsigned int *p, int *type, int *mult);
 PyObject * dim_buf_to_list(const char *schema, const char *buf, unsigned int len);
 #endif

 PyObject* dim_buf_to_tuple(const char *schema, const char *buf, int len);
 int getSizeFromFormat(const char* format);
 unsigned int getElemNrFromFormat(const char *format);

 unsigned int getSizeFromFormatAndObjects(PyObject *iter, const char* format);

 int iterator_to_buffer(PyObject *iter, char *buffer, unsigned int size, const char   *format);
 int iterator_to_allocated_buffer(PyObject  *iter, const char   *format, char  **buffer, unsigned int *size );

 /*
  * This function returns a Python string or Python bytes from the
  * buffer passed in parameters
  * Input:
  *     buffer : The buffer to create the Python string / bytes from
  *     len : The size of the buffer to create the Python string / bytes from
  */
  PyObject *get_python_string_from_char_buf(const char *buffer, unsigned int len);

  /**
  * This function allows to retrieve from the DNS the format of the data waited by the service / command
  * which name is provided in parameters
  * If the service / command's name provided doesn't correspond to an existing service
  * the format returned is NULL.
  * Input : service_command_name, the name of the service / command to get the format
  *         returned_value, the address of a char pointer to store the format in. It should be NULL or previously
  *         allocated with malloc (will be free and reallocated to the good size)
  * If the format could not have been retrieved from the DNS, the char pointer pointed
  * by returned_value will be NULL
  */
 void get_format_from_dns(const char *service_command_name,char **returned_value);


 /**
 * This function allows to retrieve the format corresponding to the command name
 * passed in parameters.
 * It retrieves the format from the command format cache (if it has not been deactivated)
 * or from the the DNS. It also insert the format found from the DNS in
 * the command format cache (if it has not been deactivated)
 * Input:
 *   service_name: the name of the service to get the format
 *   returned_value : the address of a char pointer to put the retrieved format inside.
 *   The char pointer pointed by returned_value should be NULL or pre-allocated with malloc (it will be free and re-allocated)
 * If the format could not have been retrieved, the char pointer pointed by returned_value will be NULL.
 */
 void get_cmnd_format(char *cmnd_name,char **returned_value);

#endif

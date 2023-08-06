from libcpp cimport bool


cdef extern from "../third_party/chromium/url/third_party/mozilla/url_parse.h" namespace "url":
    cdef cppclass Component:
        Component()
        Component(int b, int l)
        int begin
        int len

    cdef cppclass Parsed:
        int Length()
        Component scheme
        Component username
        Component password
        Component host
        Component port
        Component path
        Component query
        Component ref

    cdef Component MakeRange(int begin, int end)
    cdef void ParseStandardURL(const char* url, int url_len, Parsed* parsed)
    cdef void ParseFileURL(const char* url, int url_len, Parsed* parsed)
    cdef void ParseMailtoURL(const char* url, int url_len, Parsed* parsed)
    cdef void ParseFileSystemURL(const char* url, int url_len, Parsed* parsed)
    cdef void ParsePathURL(const char* url, int url_len, bool trim_path_end, Parsed* parsed)
    cdef bool ExtractScheme(const char* url, int url_len, Component* scheme)

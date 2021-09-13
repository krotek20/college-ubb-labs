using System;

namespace services
{
    public class TriathlonException : Exception
    {
        public TriathlonException() : base() { }

        public TriathlonException(string msg) : base(msg) { }

        public TriathlonException(string msg, Exception ex) : base(msg, ex) { }
    }
}

using System;

namespace client
{
    public enum TriathlonRefereeEvent
    {
        PointsChanged
    };

    public class TriathlonRefereeEventArgs : EventArgs
    {
        public TriathlonRefereeEvent RefereeEventType { get; set; }

        public object Data { get; set; }
    }
}

#pragma once

class FakeGPS
{
public:
    FakeGPS();

    // get singleton instance
    static FakeGPS *get_singleton() { return _singleton; }

    // external position backend types (used by _TYPE parameter)
    enum FakeGPSLocation {
        FakeGPSLocation_None   = 0,
        FakeGPSLocation_Pozyx  = 1,
        FakeGPSLocation_Marvelmind = 2,
        FakeGPSLocation_Nooploop  = 3,
        FakeGPSLocation_SITL   = 10
    };

    // update state of all beacons
    void update(void);


private:

    static FakeGPS *_singleton;


    FakeGPSLocation beacon_state;

};

namespace AP {
    FakeGPS *fake_gps();
};




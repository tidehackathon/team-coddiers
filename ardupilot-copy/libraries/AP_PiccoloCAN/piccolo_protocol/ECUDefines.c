// ECUDefines.c was generated by ProtoGen version 3.2.a

/*
 * This file is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the
 * Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This file is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License along
 * with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Author: Oliver Walters / Currawong Engineering Pty Ltd
 */
 

#include "ECUDefines.h"
#include "fielddecode.h"
#include "fieldencode.h"
#include "scaleddecode.h"
#include "scaledencode.h"

/*!
 * \brief Encode a ECU_AuxiliaryErrorBits_t into a byte array
 *

 * \param _pg_data points to the byte array to add encoded data to
 * \param _pg_bytecount points to the starting location in the byte array, and will be incremented by the number of encoded bytes.
 * \param _pg_user is the data to encode in the byte array
 */
void encodeECU_AuxiliaryErrorBits_t(uint8_t* _pg_data, int* _pg_bytecount, const ECU_AuxiliaryErrorBits_t* _pg_user)
{
    int _pg_byteindex = *_pg_bytecount;

    // 1 if CAN servo is not connected
    _pg_data[_pg_byteindex] = (uint8_t)((_pg_user->servoLink == true) ? 1 : 0) << 7;

    // 1 if CAN servo is reporting a position error
    _pg_data[_pg_byteindex] |= (uint8_t)((_pg_user->servoPosition == true) ? 1 : 0) << 6;

    // Reserved for future use
    // Range of reserved_A is 0 to 63.
    _pg_data[_pg_byteindex] |= (uint8_t)_pg_user->reserved_A;

    // Reserved for future use
    // Range of reserved_B is 0 to 255.
    _pg_data[_pg_byteindex + 1] = (uint8_t)_pg_user->reserved_B;

    // Reserved for future use
    // Range of reserved_C is 0 to 255.
    _pg_data[_pg_byteindex + 2] = (uint8_t)_pg_user->reserved_C;

    // Reserved for future use
    // Range of reserved_D is 0 to 255.
    _pg_data[_pg_byteindex + 3] = (uint8_t)_pg_user->reserved_D;
    _pg_byteindex += 4; // close bit field

    *_pg_bytecount = _pg_byteindex;

}// encodeECU_AuxiliaryErrorBits_t

/*!
 * \brief Decode a ECU_AuxiliaryErrorBits_t from a byte array
 *

 * \param _pg_data points to the byte array to decoded data from
 * \param _pg_bytecount points to the starting location in the byte array, and will be incremented by the number of bytes decoded
 * \param _pg_user is the data to decode from the byte array
 * \return 1 if the data are decoded, else 0.
 */
int decodeECU_AuxiliaryErrorBits_t(const uint8_t* _pg_data, int* _pg_bytecount, ECU_AuxiliaryErrorBits_t* _pg_user)
{
    int _pg_byteindex = *_pg_bytecount;

    // 1 if CAN servo is not connected
    _pg_user->servoLink = ((_pg_data[_pg_byteindex] >> 7)) ? true : false;

    // 1 if CAN servo is reporting a position error
    _pg_user->servoPosition = (((_pg_data[_pg_byteindex] >> 6) & 0x1)) ? true : false;

    // Reserved for future use
    // Range of reserved_A is 0 to 63.
    _pg_user->reserved_A = ((_pg_data[_pg_byteindex]) & 0x3F);

    // Reserved for future use
    // Range of reserved_B is 0 to 255.
    _pg_user->reserved_B = _pg_data[_pg_byteindex + 1];

    // Reserved for future use
    // Range of reserved_C is 0 to 255.
    _pg_user->reserved_C = _pg_data[_pg_byteindex + 2];

    // Reserved for future use
    // Range of reserved_D is 0 to 255.
    _pg_user->reserved_D = _pg_data[_pg_byteindex + 3];
    _pg_byteindex += 4; // close bit field

    *_pg_bytecount = _pg_byteindex;

    return 1;

}// decodeECU_AuxiliaryErrorBits_t

/*!
 * \brief Encode a ECU_AutronicErrorBits_t into a byte array
 *

 * \param _pg_data points to the byte array to add encoded data to
 * \param _pg_bytecount points to the starting location in the byte array, and will be incremented by the number of encoded bytes.
 * \param _pg_user is the data to encode in the byte array
 */
void encodeECU_AutronicErrorBits_t(uint8_t* _pg_data, int* _pg_bytecount, const ECU_AutronicErrorBits_t* _pg_user)
{
    int _pg_byteindex = *_pg_bytecount;

    // Reserved
    _pg_data[_pg_byteindex] = 0;

    // Knock control error
    _pg_data[_pg_byteindex + 1] = (uint8_t)_pg_user->knockControl << 7;

    // AF closed loop error
    _pg_data[_pg_byteindex + 1] |= (uint8_t)_pg_user->afCloseLoop << 6;

    // EEPROM error
    _pg_data[_pg_byteindex + 1] |= (uint8_t)_pg_user->eepromError << 5;

    // CMOS RAM error
    _pg_data[_pg_byteindex + 1] |= (uint8_t)_pg_user->cmosRam << 4;

    // Over voltage error
    _pg_data[_pg_byteindex + 1] |= (uint8_t)_pg_user->overVoltage << 3;

    // Power down error
    _pg_data[_pg_byteindex + 1] |= (uint8_t)_pg_user->powerDown << 2;

    // Knock sensor error
    _pg_data[_pg_byteindex + 1] |= (uint8_t)_pg_user->knockSensor << 1;

    // Over boost error
    _pg_data[_pg_byteindex + 1] |= (uint8_t)_pg_user->overBoost;

    // CAM2 position error
    _pg_data[_pg_byteindex + 2] = (uint8_t)_pg_user->cam2Pos << 7;

    // CAM1 position error
    _pg_data[_pg_byteindex + 2] |= (uint8_t)_pg_user->cam1Pos << 6;

    // High speed input 1 error
    _pg_data[_pg_byteindex + 2] |= (uint8_t)_pg_user->highSpeedInput2 << 5;

    // High speed input 2 error
    _pg_data[_pg_byteindex + 2] |= (uint8_t)_pg_user->highSpeedInput1 << 4;

    // Set if too many cylinder pulses
    _pg_data[_pg_byteindex + 2] |= (uint8_t)_pg_user->tooManyCylPulse << 3;

    // Set if too few cylinder pulses
    _pg_data[_pg_byteindex + 2] |= (uint8_t)_pg_user->tooFewCylPulse << 2;

    // Set if sync input pulse missing
    _pg_data[_pg_byteindex + 2] |= (uint8_t)_pg_user->syncInputPulseMissing << 1;

    // Set if cylinder input pulse missing
    _pg_data[_pg_byteindex + 2] |= (uint8_t)_pg_user->cylinderInputPulseMissing;

    // Air fuel sensor 2 error
    _pg_data[_pg_byteindex + 3] = (uint8_t)_pg_user->af2Sensor << 7;

    // Air fuel sensor 1 error
    _pg_data[_pg_byteindex + 3] |= (uint8_t)_pg_user->af1Sensor << 6;

    // Barometric pressure sensor error
    _pg_data[_pg_byteindex + 3] |= (uint8_t)_pg_user->baroSensor << 5;

    // Exhaust back pressure sensor error
    _pg_data[_pg_byteindex + 3] |= (uint8_t)_pg_user->ebpSensor << 4;

    // Manifold pressure sensor error
    _pg_data[_pg_byteindex + 3] |= (uint8_t)_pg_user->mapSensor << 3;

    // Throttle position sensor error
    _pg_data[_pg_byteindex + 3] |= (uint8_t)_pg_user->tpsSensor << 2;

    // Cylinder head temperature sensor error
    _pg_data[_pg_byteindex + 3] |= (uint8_t)_pg_user->chtSensor << 1;

    // Manifold pressure sensor error
    _pg_data[_pg_byteindex + 3] |= (uint8_t)_pg_user->matSensor;
    _pg_byteindex += 4; // close bit field

    *_pg_bytecount = _pg_byteindex;

}// encodeECU_AutronicErrorBits_t

/*!
 * \brief Decode a ECU_AutronicErrorBits_t from a byte array
 *

 * \param _pg_data points to the byte array to decoded data from
 * \param _pg_bytecount points to the starting location in the byte array, and will be incremented by the number of bytes decoded
 * \param _pg_user is the data to decode from the byte array
 * \return 1 if the data are decoded, else 0.
 */
int decodeECU_AutronicErrorBits_t(const uint8_t* _pg_data, int* _pg_bytecount, ECU_AutronicErrorBits_t* _pg_user)
{
    int _pg_byteindex = *_pg_bytecount;

    // Reserved

    // Knock control error
    _pg_user->knockControl = (_pg_data[_pg_byteindex + 1] >> 7);

    // AF closed loop error
    _pg_user->afCloseLoop = ((_pg_data[_pg_byteindex + 1] >> 6) & 0x1);

    // EEPROM error
    _pg_user->eepromError = ((_pg_data[_pg_byteindex + 1] >> 5) & 0x1);

    // CMOS RAM error
    _pg_user->cmosRam = ((_pg_data[_pg_byteindex + 1] >> 4) & 0x1);

    // Over voltage error
    _pg_user->overVoltage = ((_pg_data[_pg_byteindex + 1] >> 3) & 0x1);

    // Power down error
    _pg_user->powerDown = ((_pg_data[_pg_byteindex + 1] >> 2) & 0x1);

    // Knock sensor error
    _pg_user->knockSensor = ((_pg_data[_pg_byteindex + 1] >> 1) & 0x1);

    // Over boost error
    _pg_user->overBoost = ((_pg_data[_pg_byteindex + 1]) & 0x1);

    // CAM2 position error
    _pg_user->cam2Pos = (_pg_data[_pg_byteindex + 2] >> 7);

    // CAM1 position error
    _pg_user->cam1Pos = ((_pg_data[_pg_byteindex + 2] >> 6) & 0x1);

    // High speed input 1 error
    _pg_user->highSpeedInput2 = ((_pg_data[_pg_byteindex + 2] >> 5) & 0x1);

    // High speed input 2 error
    _pg_user->highSpeedInput1 = ((_pg_data[_pg_byteindex + 2] >> 4) & 0x1);

    // Set if too many cylinder pulses
    _pg_user->tooManyCylPulse = ((_pg_data[_pg_byteindex + 2] >> 3) & 0x1);

    // Set if too few cylinder pulses
    _pg_user->tooFewCylPulse = ((_pg_data[_pg_byteindex + 2] >> 2) & 0x1);

    // Set if sync input pulse missing
    _pg_user->syncInputPulseMissing = ((_pg_data[_pg_byteindex + 2] >> 1) & 0x1);

    // Set if cylinder input pulse missing
    _pg_user->cylinderInputPulseMissing = ((_pg_data[_pg_byteindex + 2]) & 0x1);

    // Air fuel sensor 2 error
    _pg_user->af2Sensor = (_pg_data[_pg_byteindex + 3] >> 7);

    // Air fuel sensor 1 error
    _pg_user->af1Sensor = ((_pg_data[_pg_byteindex + 3] >> 6) & 0x1);

    // Barometric pressure sensor error
    _pg_user->baroSensor = ((_pg_data[_pg_byteindex + 3] >> 5) & 0x1);

    // Exhaust back pressure sensor error
    _pg_user->ebpSensor = ((_pg_data[_pg_byteindex + 3] >> 4) & 0x1);

    // Manifold pressure sensor error
    _pg_user->mapSensor = ((_pg_data[_pg_byteindex + 3] >> 3) & 0x1);

    // Throttle position sensor error
    _pg_user->tpsSensor = ((_pg_data[_pg_byteindex + 3] >> 2) & 0x1);

    // Cylinder head temperature sensor error
    _pg_user->chtSensor = ((_pg_data[_pg_byteindex + 3] >> 1) & 0x1);

    // Manifold pressure sensor error
    _pg_user->matSensor = ((_pg_data[_pg_byteindex + 3]) & 0x1);
    _pg_byteindex += 4; // close bit field

    *_pg_bytecount = _pg_byteindex;

    return 1;

}// decodeECU_AutronicErrorBits_t

/*!
 * \brief Encode a ECU_ErrorBits_t into a byte array
 *

 * \param _pg_data points to the byte array to add encoded data to
 * \param _pg_bytecount points to the starting location in the byte array, and will be incremented by the number of encoded bytes.
 * \param _pg_user is the data to encode in the byte array
 */
void encodeECU_ErrorBits_t(uint8_t* _pg_data, int* _pg_bytecount, const ECU_ErrorBits_t* _pg_user)
{
    int _pg_byteindex = *_pg_bytecount;

    // Error information for autronic processor
    encodeECU_AutronicErrorBits_t(_pg_data, &_pg_byteindex, &_pg_user->autronic);

    // Error information for auxiliary processor
    encodeECU_AuxiliaryErrorBits_t(_pg_data, &_pg_byteindex, &_pg_user->auxiliary);

    *_pg_bytecount = _pg_byteindex;

}// encodeECU_ErrorBits_t

/*!
 * \brief Decode a ECU_ErrorBits_t from a byte array
 *

 * \param _pg_data points to the byte array to decoded data from
 * \param _pg_bytecount points to the starting location in the byte array, and will be incremented by the number of bytes decoded
 * \param _pg_user is the data to decode from the byte array
 * \return 1 if the data are decoded, else 0.
 */
int decodeECU_ErrorBits_t(const uint8_t* _pg_data, int* _pg_bytecount, ECU_ErrorBits_t* _pg_user)
{
    int _pg_byteindex = *_pg_bytecount;

    // Error information for autronic processor
    if(decodeECU_AutronicErrorBits_t(_pg_data, &_pg_byteindex, &_pg_user->autronic) == 0)
        return 0;

    // Error information for auxiliary processor
    if(decodeECU_AuxiliaryErrorBits_t(_pg_data, &_pg_byteindex, &_pg_user->auxiliary) == 0)
        return 0;

    *_pg_bytecount = _pg_byteindex;

    return 1;

}// decodeECU_ErrorBits_t

/*!
 * \brief Encode a ECU_ThrottleDelayConfigBits_t into a byte array
 *

 * \param _pg_data points to the byte array to add encoded data to
 * \param _pg_bytecount points to the starting location in the byte array, and will be incremented by the number of encoded bytes.
 * \param _pg_user is the data to encode in the byte array
 */
void encodeECU_ThrottleDelayConfigBits_t(uint8_t* _pg_data, int* _pg_bytecount, const ECU_ThrottleDelayConfigBits_t* _pg_user)
{
    int _pg_byteindex = *_pg_bytecount;

    // reserved for future use
    // Range of reserved is 0 to 127.
    _pg_data[_pg_byteindex] = (uint8_t)_pg_user->reserved << 1;

    // Set to base the delay on temperature, else the delay is manually set
    _pg_data[_pg_byteindex] |= (uint8_t)((_pg_user->delayOnTemp == true) ? 1 : 0);
    _pg_byteindex += 1; // close bit field

    *_pg_bytecount = _pg_byteindex;

}// encodeECU_ThrottleDelayConfigBits_t

/*!
 * \brief Decode a ECU_ThrottleDelayConfigBits_t from a byte array
 *

 * \param _pg_data points to the byte array to decoded data from
 * \param _pg_bytecount points to the starting location in the byte array, and will be incremented by the number of bytes decoded
 * \param _pg_user is the data to decode from the byte array
 * \return 1 if the data are decoded, else 0.
 */
int decodeECU_ThrottleDelayConfigBits_t(const uint8_t* _pg_data, int* _pg_bytecount, ECU_ThrottleDelayConfigBits_t* _pg_user)
{
    int _pg_byteindex = *_pg_bytecount;

    // reserved for future use
    // Range of reserved is 0 to 127.
    _pg_user->reserved = (_pg_data[_pg_byteindex] >> 1);

    // Set to base the delay on temperature, else the delay is manually set
    _pg_user->delayOnTemp = (((_pg_data[_pg_byteindex]) & 0x1)) ? true : false;
    _pg_byteindex += 1; // close bit field

    *_pg_bytecount = _pg_byteindex;

    return 1;

}// decodeECU_ThrottleDelayConfigBits_t

/*!
 * \brief Encode a ECU_ThrottleConfigBits_t into a byte array
 *

 * \param _pg_data points to the byte array to add encoded data to
 * \param _pg_bytecount points to the starting location in the byte array, and will be incremented by the number of encoded bytes.
 * \param _pg_user is the data to encode in the byte array
 */
void encodeECU_ThrottleConfigBits_t(uint8_t* _pg_data, int* _pg_bytecount, const ECU_ThrottleConfigBits_t* _pg_user)
{
    int _pg_byteindex = *_pg_bytecount;

    // Enable pass-through of CAN servo data over serial link
    _pg_data[_pg_byteindex] = (uint8_t)((_pg_user->servoPassthrough == true) ? 1 : 0) << 7;

    // Reserved for future use

    // Set if the CAN throttle is detected
    _pg_data[_pg_byteindex] |= (uint8_t)((_pg_user->canThrottleDetected == true) ? 1 : 0) << 1;

    // Set if CAN throttle is enabled. This bit is ignored when this packet is sent to the ECU. To enable CAN throttle you must use system commands
    _pg_data[_pg_byteindex] |= (uint8_t)((_pg_user->canThrottle == true) ? 1 : 0);
    _pg_byteindex += 1; // close bit field

    *_pg_bytecount = _pg_byteindex;

}// encodeECU_ThrottleConfigBits_t

/*!
 * \brief Decode a ECU_ThrottleConfigBits_t from a byte array
 *

 * \param _pg_data points to the byte array to decoded data from
 * \param _pg_bytecount points to the starting location in the byte array, and will be incremented by the number of bytes decoded
 * \param _pg_user is the data to decode from the byte array
 * \return 1 if the data are decoded, else 0.
 */
int decodeECU_ThrottleConfigBits_t(const uint8_t* _pg_data, int* _pg_bytecount, ECU_ThrottleConfigBits_t* _pg_user)
{
    int _pg_byteindex = *_pg_bytecount;

    // Enable pass-through of CAN servo data over serial link
    _pg_user->servoPassthrough = ((_pg_data[_pg_byteindex] >> 7)) ? true : false;

    // Reserved for future use

    // Set if the CAN throttle is detected
    _pg_user->canThrottleDetected = (((_pg_data[_pg_byteindex] >> 1) & 0x1)) ? true : false;

    // Set if CAN throttle is enabled. This bit is ignored when this packet is sent to the ECU. To enable CAN throttle you must use system commands
    _pg_user->canThrottle = (((_pg_data[_pg_byteindex]) & 0x1)) ? true : false;
    _pg_byteindex += 1; // close bit field

    *_pg_bytecount = _pg_byteindex;

    return 1;

}// decodeECU_ThrottleConfigBits_t

/*!
 * \brief Encode a ECU_ThrottleCurveConfigBits_t into a byte array
 *

 * \param _pg_data points to the byte array to add encoded data to
 * \param _pg_bytecount points to the starting location in the byte array, and will be incremented by the number of encoded bytes.
 * \param _pg_user is the data to encode in the byte array
 */
void encodeECU_ThrottleCurveConfigBits_t(uint8_t* _pg_data, int* _pg_bytecount, const ECU_ThrottleCurveConfigBits_t* _pg_user)
{
    int _pg_byteindex = *_pg_bytecount;

    // Reserved for future use
    _pg_data[_pg_byteindex] = 0;

    // Throttle curve is active
    _pg_data[_pg_byteindex] |= (uint8_t)((_pg_user->curveActive == true) ? 1 : 0);
    _pg_byteindex += 1; // close bit field

    *_pg_bytecount = _pg_byteindex;

}// encodeECU_ThrottleCurveConfigBits_t

/*!
 * \brief Decode a ECU_ThrottleCurveConfigBits_t from a byte array
 *

 * \param _pg_data points to the byte array to decoded data from
 * \param _pg_bytecount points to the starting location in the byte array, and will be incremented by the number of bytes decoded
 * \param _pg_user is the data to decode from the byte array
 * \return 1 if the data are decoded, else 0.
 */
int decodeECU_ThrottleCurveConfigBits_t(const uint8_t* _pg_data, int* _pg_bytecount, ECU_ThrottleCurveConfigBits_t* _pg_user)
{
    int _pg_byteindex = *_pg_bytecount;

    // Reserved for future use

    // Throttle curve is active
    _pg_user->curveActive = (((_pg_data[_pg_byteindex]) & 0x1)) ? true : false;
    _pg_byteindex += 1; // close bit field

    *_pg_bytecount = _pg_byteindex;

    return 1;

}// decodeECU_ThrottleCurveConfigBits_t

/*!
 * \brief Encode a ECU_ECUSettings_t into a byte array
 *

 * \param _pg_data points to the byte array to add encoded data to
 * \param _pg_bytecount points to the starting location in the byte array, and will be incremented by the number of encoded bytes.
 * \param _pg_user is the data to encode in the byte array
 */
void encodeECU_ECUSettings_t(uint8_t* _pg_data, int* _pg_bytecount, const ECU_ECUSettings_t* _pg_user)
{
    int _pg_byteindex = *_pg_bytecount;

    // Range of powerCycles is 0 to 65535.
    uint16ToBeBytes(_pg_user->powerCycles, _pg_data, &_pg_byteindex);

    // Deprecated - DO NOT USE
    // Range of customerID_deprecated is 0 to 65535.
    uint16ToBeBytes(_pg_user->customerID_deprecated, _pg_data, &_pg_byteindex);

    // Range of versionHardware is 0 to 255.
    uint8ToBytes(_pg_user->versionHardware, _pg_data, &_pg_byteindex);

    // reserved for future use
    // Range of reservedA is 0 to 255.
    uint8ToBytes(_pg_user->reservedA, _pg_data, &_pg_byteindex);

    // reserved for future use
    // Range of reservedB is 0 to 255.
    uint8ToBytes(_pg_user->reservedB, _pg_data, &_pg_byteindex);

    *_pg_bytecount = _pg_byteindex;

}// encodeECU_ECUSettings_t

/*!
 * \brief Decode a ECU_ECUSettings_t from a byte array
 *

 * \param _pg_data points to the byte array to decoded data from
 * \param _pg_bytecount points to the starting location in the byte array, and will be incremented by the number of bytes decoded
 * \param _pg_user is the data to decode from the byte array
 * \return 1 if the data are decoded, else 0.
 */
int decodeECU_ECUSettings_t(const uint8_t* _pg_data, int* _pg_bytecount, ECU_ECUSettings_t* _pg_user)
{
    int _pg_byteindex = *_pg_bytecount;

    // Range of powerCycles is 0 to 65535.
    _pg_user->powerCycles = uint16FromBeBytes(_pg_data, &_pg_byteindex);

    // Deprecated - DO NOT USE
    // Range of customerID_deprecated is 0 to 65535.
    _pg_user->customerID_deprecated = uint16FromBeBytes(_pg_data, &_pg_byteindex);

    // Range of versionHardware is 0 to 255.
    _pg_user->versionHardware = uint8FromBytes(_pg_data, &_pg_byteindex);

    // reserved for future use
    // Range of reservedA is 0 to 255.
    _pg_user->reservedA = uint8FromBytes(_pg_data, &_pg_byteindex);

    // reserved for future use
    // Range of reservedB is 0 to 255.
    _pg_user->reservedB = uint8FromBytes(_pg_data, &_pg_byteindex);

    *_pg_bytecount = _pg_byteindex;

    return 1;

}// decodeECU_ECUSettings_t

/*!
 * \brief Encode a ECU_CompileOptions_t into a byte array
 *

 * \param _pg_data points to the byte array to add encoded data to
 * \param _pg_bytecount points to the starting location in the byte array, and will be incremented by the number of encoded bytes.
 * \param _pg_user is the data to encode in the byte array
 */
void encodeECU_CompileOptions_t(uint8_t* _pg_data, int* _pg_bytecount, const ECU_CompileOptions_t* _pg_user)
{
    int _pg_byteindex = *_pg_bytecount;

    // If set, the ECU will pass servo CAN packet data over the serial link
    _pg_data[_pg_byteindex] = (uint8_t)((_pg_user->servoPassthrough == true) ? 1 : 0) << 7;

    // If set, the ECU will decode CAN messages in the PICCOLO_DATA_UP group
    _pg_data[_pg_byteindex] |= (uint8_t)((_pg_user->piccoloUplink == true) ? 1 : 0) << 6;

    // If set, the ECU supports Autronic message passthrough
    _pg_data[_pg_byteindex] |= (uint8_t)((_pg_user->autronicRelay == true) ? 1 : 0) << 5;

    // If set, the ECU supports redundant fuel pump control
    _pg_data[_pg_byteindex] |= (uint8_t)((_pg_user->dualPump == true) ? 1 : 0) << 4;

    // If set, the ECU runs a PI controller for fuel pressure. If not set, it uses bang-bang control
    _pg_data[_pg_byteindex] |= (uint8_t)((_pg_user->piPump == true) ? 1 : 0) << 3;

    // If set, the ECU will automatically compensate for degredation of the MAP sensor over time
    _pg_data[_pg_byteindex] |= (uint8_t)((_pg_user->mapCorrection == true) ? 1 : 0) << 2;

    // If set, the ECU watchdog timer is enabled
    _pg_data[_pg_byteindex] |= (uint8_t)((_pg_user->watchdog == true) ? 1 : 0) << 1;

    // If set, the ECU is compiled with extra debug functionality enabled
    _pg_data[_pg_byteindex] |= (uint8_t)((_pg_user->debug == true) ? 1 : 0);
    _pg_byteindex += 1; // close bit field

    // Reserved for future use
    uint8ToBytes((uint8_t)(0), _pg_data, &_pg_byteindex);

    *_pg_bytecount = _pg_byteindex;

}// encodeECU_CompileOptions_t

/*!
 * \brief Decode a ECU_CompileOptions_t from a byte array
 *

 * \param _pg_data points to the byte array to decoded data from
 * \param _pg_bytecount points to the starting location in the byte array, and will be incremented by the number of bytes decoded
 * \param _pg_user is the data to decode from the byte array
 * \return 1 if the data are decoded, else 0.
 */
int decodeECU_CompileOptions_t(const uint8_t* _pg_data, int* _pg_bytecount, ECU_CompileOptions_t* _pg_user)
{
    int _pg_byteindex = *_pg_bytecount;

    // If set, the ECU will pass servo CAN packet data over the serial link
    _pg_user->servoPassthrough = ((_pg_data[_pg_byteindex] >> 7)) ? true : false;

    // If set, the ECU will decode CAN messages in the PICCOLO_DATA_UP group
    _pg_user->piccoloUplink = (((_pg_data[_pg_byteindex] >> 6) & 0x1)) ? true : false;

    // If set, the ECU supports Autronic message passthrough
    _pg_user->autronicRelay = (((_pg_data[_pg_byteindex] >> 5) & 0x1)) ? true : false;

    // If set, the ECU supports redundant fuel pump control
    _pg_user->dualPump = (((_pg_data[_pg_byteindex] >> 4) & 0x1)) ? true : false;

    // If set, the ECU runs a PI controller for fuel pressure. If not set, it uses bang-bang control
    _pg_user->piPump = (((_pg_data[_pg_byteindex] >> 3) & 0x1)) ? true : false;

    // If set, the ECU will automatically compensate for degredation of the MAP sensor over time
    _pg_user->mapCorrection = (((_pg_data[_pg_byteindex] >> 2) & 0x1)) ? true : false;

    // If set, the ECU watchdog timer is enabled
    _pg_user->watchdog = (((_pg_data[_pg_byteindex] >> 1) & 0x1)) ? true : false;

    // If set, the ECU is compiled with extra debug functionality enabled
    _pg_user->debug = (((_pg_data[_pg_byteindex]) & 0x1)) ? true : false;
    _pg_byteindex += 1; // close bit field

    // Reserved for future use
    _pg_byteindex += 1;

    *_pg_bytecount = _pg_byteindex;

    return 1;

}// decodeECU_CompileOptions_t

// end of ECUDefines.c

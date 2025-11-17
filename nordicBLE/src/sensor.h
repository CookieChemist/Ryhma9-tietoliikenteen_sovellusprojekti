#ifndef ADC_H_KJJ
#define ADC_H_KJJ

#include <zephyr/types.h>
#include <stddef.h>
#include <string.h>
#include <errno.h>
#include <zephyr/sys/printk.h>
#include <zephyr/sys/byteorder.h>
#include <zephyr/kernel.h>
#include <zephyr/logging/log.h>
#include <zephyr/bluetooth/bluetooth.h>
#include <zephyr/bluetooth/hci.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/bluetooth/uuid.h>
#include <zephyr/bluetooth/gatt.h>

struct Measurement
{
   uint16_t x;
   uint16_t y;
   uint16_t z;
};

int initializeADC(void);
struct Measurement readADCValue(void);
void printDebugInfo(void);
extern int currentDirection;


#endif
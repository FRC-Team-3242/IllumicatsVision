#!/usr/bin/env python

from networktables import NetworkTable

#USB Rio IP: 172.22.11.2
#DHCP Rio IP Range: 10.32.42.20-199


class VisionTable:
  
  def __init__(self, ip="roboRIO-3242-FRC.local"):
    NetworkTable.setIPAddress(ip)
    NetworkTable.setClientMode()
    NetworkTable.initialize()
    self.table = NetworkTable.getTable("rpi")

  def update(self, afound, ax=-1, ay=-1, bfound, bx=-1, by=-1):
    self.table.putNumber("AvisionX", ax)
    self.table.putNumber("AvisionY", ay)
    self.table.putBoolean("Afound", afound)
    self.table.putNumber("BvisionX", bx)
    self.table.putNumber("BvisionY", by)
    self.table.putBoolean("Bfound", bfound)

  def useA(self):
    return self.table.getBoolean("Aenabled", True)

  def useB(self):
    return self.table.getBoolean("Benabled", True)

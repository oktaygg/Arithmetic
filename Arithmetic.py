import io
import random
import sys

from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QMediaPlaylist

TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="enabled">
   <bool>true</bool>
  </property>
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1300</width>
    <height>900</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>100</width>
    <height>100</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Arithmetic</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255,
    75, 31, 255), stop:1 rgba(31, 221, 255, 255));;</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QGridLayout" name="gridLayout_2">
    <item row="0" column="0">
     <layout class="QGridLayout" name="gridLayout">
      <item row="26" column="2">
       <spacer name="horizontalSpacer_5">
        <property name="orientation">
         <enum>Qt::Horizontal</enum>
        </property>
        <property name="sizeHint" stdset="0">
         <size>
          <width>40</width>
          <height>20</height>
         </size>
        </property>
       </spacer>
      </item>
      <item row="7" column="1">
       <layout class="QHBoxLayout" name="horizontalLayout_5">
        <item>
         <widget class="QLabel" name="quastionlabel">
          <property name="styleSheet">
           <string notr="true">background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,
            stop:0 rgba(255, 75, 31, 0), stop:1 rgba(31, 221, 255, 0));
    font: bold 14px;</string>
          </property>
          <property name="text">
           <string>Quastion</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="btnend">
          <property name="styleSheet">
           <string notr="true">background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1,
            y2:0, stop:0 rgba(255, 75, 31, 255), stop:1 rgba(31, 221, 255, 255));;
    border-style: outset;
    border-width: 2px;
    border-radius: 7px;
    border-color: black;
    font: bold 14px;
    min-width: 10em;
    padding: 0px;</string>
          </property>
          <property name="text">
           <string>end game</string>
          </property>
         </widget>
        </item>
       </layout>
      </item>
      <item row="28" column="1">
       <spacer name="verticalSpacer_7">
        <property name="orientation">
         <enum>Qt::Vertical</enum>
        </property>
        <property name="sizeHint" stdset="0">
         <size>
          <width>20</width>
          <height>40</height>
         </size>
        </property>
       </spacer>
      </item>
      <item row="24" column="1">
       <widget class="QPushButton" name="btnbs">
        <property name="styleSheet">
         <string notr="true">background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1,
          y2:0, stop:0 rgba(255, 75, 31, 255), stop:1 rgba(31, 221, 255, 255));;
    border-style: outset;
    border-width: 2px;
    border-radius: 7px;
    border-color: black;
    font: bold 14px;
    min-width: 10em;
    padding: 0px;</string>
        </property>
        <property name="text">
         <string>back</string>
        </property>
       </widget>
      </item>
      <item row="18" column="1">
       <widget class="QPushButton" name="btncn">
        <property name="styleSheet">
         <string notr="true">background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1,
          y2:0, stop:0 rgba(255, 75, 31, 255), stop:1 rgba(31, 221, 255, 255));;
    border-style: outset;
    border-width: 2px;
    border-radius: 7px;
    border-color: black;
    font: bold 14px;
    min-width: 10em;
    padding: 0px;</string>
        </property>
        <property name="text">
         <string>change name</string>
        </property>
       </widget>
      </item>
      <item row="14" column="1">
       <layout class="QHBoxLayout" name="horizontalLayout_2">
        <item>
         <widget class="QLabel" name="shoptxt2">
          <property name="styleSheet">
           <string notr="true">background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1,
            y2:0, stop:0 rgba(255, 75, 31, 0), stop:1 rgba(31, 221, 255, 0));
    font: bold 14px;</string>
          </property>
          <property name="text">
           <string>skip the question                            100 coins                        </string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QSpinBox" name="shopn2">
          <property name="styleSheet">
           <string notr="true">background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1,
            y2:0, stop:0 rgba(255, 75, 31, 0), stop:1 rgba(31, 221, 255, 0));
    font: bold 14px;</string>
          </property>
         </widget>
        </item>
       </layout>
      </item>
      <item row="5" column="1">
       <layout class="QHBoxLayout" name="dl1">
        <item>
         <widget class="QPushButton" name="btncnb">
          <property name="styleSheet">
           <string notr="true">background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1,
            y2:0, stop:0 rgba(255, 75, 31, 255), stop:1 rgba(31, 221, 255, 255));;
    border-style: outset;
    border-width: 2px;
    border-radius: 7px;
    border-color: black;
    font: bold 14px;
    min-width: 10em;
    padding: 0px;</string>
          </property>
          <property name="text">
           <string>back</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="btncnok">
          <property name="styleSheet">
           <string notr="true">background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1,
            y2:0, stop:0 rgba(255, 75, 31, 255), stop:1 rgba(31, 221, 255, 255));;
    border-style: outset;
    border-width: 2px;
    border-radius: 7px;
    border-color: black;
    font: bold 14px;
    min-width: 10em;
    padding: 0px;</string>
          </property>
          <property name="text">
           <string>change</string>
          </property>
         </widget>
        </item>
       </layout>
      </item>
      <item row="6" column="1">
       <widget class="QPushButton" name="btnstart">
        <property name="styleSheet">
         <string notr="true">background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1,
          y2:0, stop:0 rgba(255, 75, 31, 255), stop:1 rgba(31, 221, 255, 255));;
    border-style: outset;
    border-width: 2px;
    border-radius: 7px;
    border-color: black;
    font: bold 14px;
    min-width: 10em;
    padding: 0px;</string>
        </property>
        <property name="text">
         <string>start</string>
        </property>
       </widget>
      </item>
      <item row="26" column="0">
       <spacer name="horizontalSpacer">
        <property name="orientation">
         <enum>Qt::Horizontal</enum>
        </property>
        <property name="sizeHint" stdset="0">
         <size>
          <width>40</width>
          <height>20</height>
         </size>
        </property>
       </spacer>
      </item>
      <item row="29" column="1">
       <spacer name="verticalSpacer_6">
        <property name="orientation">
         <enum>Qt::Vertical</enum>
        </property>
        <property name="sizeHint" stdset="0">
         <size>
          <width>20</width>
          <height>40</height>
         </size>
        </property>
       </spacer>
      </item>
      <item row="21" column="1">
       <layout class="QHBoxLayout" name="horizontalLayout_7">
        <item>
         <widget class="QPushButton" name="btnc1">
          <property name="styleSheet">
           <string notr="true">background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1,
            y2:0, stop:0 rgba(255, 75, 31, 255), stop:1 rgba(31, 221, 255, 255));;
    border-style: outset;
    border-width: 2px;
    border-radius: 7px;
    border-color: black;
    font: bold 14px;
    min-width: 10em;
    padding: 0px;</string>
          </property>
          <property name="text">
           <string>class 1</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="btnc2">
          <property name="styleSheet">
           <string notr="true">background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1,
            y2:0, stop:0 rgba(255, 75, 31, 255), stop:1 rgba(31, 221, 255, 255));;
    border-style: outset;
    border-width: 2px;
    border-radius: 7px;
    border-color: black;
    font: bold 14px;
    min-width: 10em;
    padding: 0px;</string>
          </property>
          <property name="text">
           <string>class 2</string>
          </property>
         </widget>
        </item>
       </layout>
      </item>
      <item row="1" column="1">
       <spacer name="verticalSpacer_5">
        <property name="orientation">
         <enum>Qt::Vertical</enum>
        </property>
        <property name="sizeHint" stdset="0">
         <size>
          <width>20</width>
          <height>40</height>
         </size>
        </property>
       </spacer>
      </item>
      <item row="9" column="1">
       <layout class="QHBoxLayout" name="horizontalLayout_4">
        <item>
         <widget class="QPushButton" name="btna1">
          <property name="styleSheet">
           <string notr="true">background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1,
            y2:0, stop:0 rgba(255, 75, 31, 255), stop:1 rgba(31, 221, 255, 255));;
    border-style: outset;
    border-width: 2px;
    border-radius: 7px;
    border-color: black;
    font: bold 14px;
    min-width: 5em;
    padding: 0px;</string>
          </property>
          <property name="text">
           <string>ans1</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="btna2">
          <property name="styleSheet">
           <string notr="true">background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1,
            y2:0, stop:0 rgba(255, 75, 31, 255), stop:1 rgba(31, 221, 255, 255));;
    border-style: outset;
    border-width: 2px;
    border-radius: 7px;
    border-color: black;
    font: bold 14px;
    min-width: 5em;
    padding: 0px;</string>
          </property>
          <property name="text">
           <string>ans2</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="btna3">
          <property name="styleSheet">
           <string notr="true">background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1,
            y2:0, stop:0 rgba(255, 75, 31, 255), stop:1 rgba(31, 221, 255, 255));;
    border-style: outset;
    border-width: 2px;
    border-radius: 7px;
    border-color: black;
    font: bold 14px;
    min-width: 5em;
    padding: 0px;</string>
          </property>
          <property name="text">
           <string>ans3</string>
          </property>
         </widget>
        </item>
       </layout>
      </item>
      <item row="8" column="1">
       <layout class="QHBoxLayout" name="horizontalLayout_6">
        <item>
         <widget class="QPushButton" name="btnpod1">
          <property name="styleSheet">
           <string notr="true">background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1,
            y2:0, stop:0 rgba(255, 75, 31, 255), stop:1 rgba(31, 221, 255, 255));;
    border-style: outset;
    border-width: 2px;
    border-radius: 7px;
    border-color: black;
    font: bold 14px;
    min-width: 10em;
    padding: 0px;</string>
          </property>
          <property name="text">
           <string>minus one answer: 0</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="btnpod2">
          <property name="styleSheet">
           <string notr="true">background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1,
            y2:0, stop:0 rgba(255, 75, 31, 255), stop:1 rgba(31, 221, 255, 255));;
    border-style: outset;
    border-width: 2px;
    border-radius: 7px;
    border-color: black;
    font: bold 14px;
    min-width: 10em;
    padding: 0px;</string>
          </property>
          <property name="text">
           <string>skip quastion: 0</string>
          </property>
         </widget>
        </item>
       </layout>
      </item>
      <item row="27" column="1">
       <widget class="QPushButton" name="btnex">
        <property name="styleSheet">
         <string notr="true">background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1,
          y2:0, stop:0 rgba(255, 75, 31, 255), stop:1 rgba(31, 221, 255, 255));;
    border-style: outset;
    border-width: 2px;
    border-radius: 7px;
    border-color: black;
    font: bold 14px;
    min-width: 10em;
    padding: 0px;</string>
        </property>
        <property name="text">
         <string>exit</string>
        </property>
       </widget>
      </item>
      <item row="16" column="1">
       <widget class="QPushButton" name="btnshopb">
        <property name="styleSheet">
         <string notr="true">background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1,
          y2:0, stop:0 rgba(255, 75, 31, 255), stop:1 rgba(31, 221, 255, 255));;
    border-style: outset;
    border-width: 2px;
    border-radius: 7px;
    border-color: black;
    font: bold 14px;
    min-width: 10em;
    padding: 0px;</string>
        </property>
        <property name="text">
         <string>back</string>
        </property>
       </widget>
      </item>
      <item row="26" column="1">
       <widget class="QPushButton" name="btnset">
        <property name="styleSheet">
         <string notr="true">background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1,
          y2:0, stop:0 rgba(255, 75, 31, 255), stop:1 rgba(31, 221, 255, 255));;
    border-style: outset;
    border-width: 2px;
    border-radius: 7px;
    border-color: black;
    font: bold 14px;
    min-width: 10em;
    padding: 0px;</string>
        </property>
        <property name="text">
         <string>settings</string>
        </property>
       </widget>
      </item>
      <item row="12" column="1">
       <widget class="QLabel" name="txtbalance">
        <property name="styleSheet">
         <string notr="true">background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1,
          y2:0, stop:0 rgba(255, 75, 31, 0), stop:1 rgba(31, 221, 255, 0));
    font: bold 14px;</string>
        </property>
        <property name="text">
         <string>                                       Balance: 0 coins                        </string>
        </property>
       </widget>
      </item>
      <item row="0" column="1">
       <spacer name="verticalSpacer_3">
        <property name="orientation">
         <enum>Qt::Vertical</enum>
        </property>
        <property name="sizeHint" stdset="0">
         <size>
          <width>20</width>
          <height>40</height>
         </size>
        </property>
       </spacer>
      </item>
      <item row="2" column="1">
       <widget class="QLabel" name="mainlabel">
        <property name="styleSheet">
         <string notr="true">background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1,
          y2:0, stop:0 rgba(255, 75, 31, 0), stop:1 rgba(31, 221, 255, 0));
    font: bold 14px;</string>
        </property>
        <property name="text">
         <string>                            Arifmetic game                              </string>
        </property>
       </widget>
      </item>
      <item row="4" column="1">
       <widget class="QLineEdit" name="nameedit">
        <property name="styleSheet">
         <string notr="true">background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1,
          y2:0, stop:0 rgba(255, 75, 31, 255), stop:1 rgba(31, 221, 255, 255));
    font: bold 14px;</string>
        </property>
       </widget>
      </item>
      <item row="17" column="1">
       <widget class="QPushButton" name="btnbp">
        <property name="styleSheet">
         <string notr="true">background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1,
          y2:0, stop:0 rgba(255, 75, 31, 255), stop:1 rgba(31, 221, 255, 255));;
    border-style: outset;
    border-width: 2px;
    border-radius: 7px;
    border-color: black;
    font: bold 14px;
    min-width: 10em;
    padding: 0px;</string>
        </property>
        <property name="text">
         <string>back</string>
        </property>
       </widget>
      </item>
      <item row="25" column="1">
       <widget class="QPushButton" name="btnplay">
        <property name="styleSheet">
         <string notr="true">background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1,
          y2:0, stop:0 rgba(255, 75, 31, 255), stop:1 rgba(31, 221, 255, 255));;
    border-style: outset;
    border-width: 2px;
    border-radius: 7px;
    border-color: black;
    font: bold 14px;
    min-width: 10em;
    padding: 0px;</string>
        </property>
        <property name="text">
         <string>play</string>
        </property>
       </widget>
      </item>
      <item row="3" column="1">
       <spacer name="verticalSpacer_8">
        <property name="orientation">
         <enum>Qt::Vertical</enum>
        </property>
        <property name="sizeHint" stdset="0">
         <size>
          <width>20</width>
          <height>40</height>
         </size>
        </property>
       </spacer>
      </item>
      <item row="22" column="1">
       <widget class="QPushButton" name="btnmusic">
        <property name="styleSheet">
         <string notr="true">background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1,
          y2:0, stop:0 rgba(255, 75, 31, 255), stop:1 rgba(31, 221, 255, 255));;
    border-style: outset;
    border-width: 2px;
    border-radius: 7px;
    border-color: black;
    font: bold 14px;
    min-width: 10em;
    padding: 0px;</string>
        </property>
        <property name="text">
         <string>revove music</string>
        </property>
       </widget>
      </item>
      <item row="30" column="1">
       <spacer name="verticalSpacer_4">
        <property name="orientation">
         <enum>Qt::Vertical</enum>
        </property>
        <property name="sizeHint" stdset="0">
         <size>
          <width>20</width>
          <height>40</height>
         </size>
        </property>
       </spacer>
      </item>
      <item row="11" column="1">
       <widget class="QPushButton" name="shopbtn">
        <property name="styleSheet">
         <string notr="true">background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1,
          y2:0, stop:0 rgba(255, 75, 31, 255), stop:1 rgba(31, 221, 255, 255));;
    border-style: outset;
    border-width: 2px;
    border-radius: 7px;
    border-color: black;
    font: bold 14px;
    min-width: 10em;
    padding: 0px;</string>
        </property>
        <property name="text">
         <string>shop</string>
        </property>
       </widget>
      </item>
      <item row="13" column="1">
       <layout class="QHBoxLayout" name="horizontalLayout">
        <item>
         <widget class="QLabel" name="shoptxt1">
          <property name="styleSheet">
           <string notr="true">background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1,
            y2:0, stop:0 rgba(255, 75, 31, 0), stop:1 rgba(31, 221, 255, 0));
    font: bold 14px;</string>
          </property>
          <property name="text">
           <string>minus one answer                          50 coins                          </string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QSpinBox" name="shopn1">
          <property name="styleSheet">
           <string notr="true">background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1,
            y2:0, stop:0 rgba(255, 75, 31, 0), stop:1 rgba(31, 221, 255, 0));
    font: bold 14px;</string>
          </property>
         </widget>
        </item>
       </layout>
      </item>
      <item row="10" column="1">
       <widget class="QPushButton" name="btncon">
        <property name="styleSheet">
         <string notr="true">background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1,
          y2:0, stop:0 rgba(255, 75, 31, 255), stop:1 rgba(31, 221, 255, 255));;
    border-style: outset;
    border-width: 2px;
    border-radius: 7px;
    border-color: black;
    font: bold 14px;
    min-width: 10em;
    padding: 0px;</string>
        </property>
        <property name="text">
         <string>Continue</string>
        </property>
       </widget>
      </item>
      <item row="15" column="1">
       <layout class="QHBoxLayout" name="horizontalLayout_3">
        <item>
         <widget class="QLabel" name="shoptxt3">
          <property name="styleSheet">
           <string notr="true">background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1,
            y2:0, stop:0 rgba(255, 75, 31, 0), stop:1 rgba(31, 221, 255, 0));
    font: bold 14px;</string>
          </property>
          <property name="text">
           <string>sum = 0 coins</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="btnshopbuy">
          <property name="styleSheet">
           <string notr="true">background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1,
            y2:0, stop:0 rgba(255, 75, 31, 255), stop:1 rgba(31, 221, 255, 255));;
    border-style: outset;
    border-width: 2px;
    border-radius: 7px;
    border-color: black;
    font: bold 14px;
    min-width: 10em;
    padding: 0px;</string>
          </property>
          <property name="text">
           <string>buy</string>
          </property>
         </widget>
        </item>
       </layout>
      </item>
     </layout>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1300</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('iconka.ico'))

        self.setWindowTitle('Arithmetic')

        self.playlist = QMediaPlaylist()
        self.url = QUrl.fromLocalFile("lobby soundtrack.mp3")
        self.playlist.addMedia(QMediaContent(self.url))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)

        self.player = QMediaPlayer()
        self.player.setPlaylist(self.playlist)

        self.workcoin = 0
        self.kolichestvo = 0
        self.answer = -1
        self.answerlist = []
        self.wins = []
        self.winnew = 0
        self.winold = 0
        self.kolichestvopodskazok1 = 0
        self.kolichestvopodskazok2 = 0
        with open('config.txt', encoding='utf-8') as t:
            lines = t.readlines()
            self.name = " ".join(lines[0].split())
            self.clas = " ".join(lines[1].split())
            self.balance = lines[2].split()[0]
            self.podskaza1 = int(lines[3].split()[0])
            self.podskaza2 = int(lines[4].split()[0])
            self.musicnum = int(lines[5].split()[0])
        f = io.StringIO(TEMPLATE)
        uic.loadUi(f, self)

        self.gomusic()

        self.btns = [self.btnplay, self.btnset, self.btnex,
                     self.btnstart, self.shopbtn, self.btnbp,
                     self.btnc1, self.btnc2,
                     self.btncn, self.btnbs, self.btncnok, self.btncnb,
                     self.btnshopb, self.btnshopbuy, self.btnpod1, self.btnpod2,
                     self.btna1, self.btna2, self.btna3, self.btnend, self.btncon, self.btnmusic]

        self.wins.append([self.btnplay, self.btnset, self.btnex])
        self.wins.append([self.btnstart, self.shopbtn, self.btnbp])
        self.wins.append([self.btnc1, self.btnc2, self.btncn, self.btnbs, self.btnmusic])
        self.wins.append([self.btncnok, self.btncnb, self.nameedit])
        self.wins.append([self.shoptxt1, self.shopn1, self.shoptxt2,
                          self.shopn2, self.shoptxt3, self.btnshopbuy,
                          self.btnshopb, self.txtbalance])
        self.wins.append([self.quastionlabel, self.btnend, self.btnpod1, self.btnpod2,
                          self.btna1, self.btna2, self.btna3])
        self.wins.append([self.btncon])

        self.shopn1.setMinimum(0)
        self.shopn2.setMinimum(0)
        self.shopn1.valueChanged.connect(self.reshop1)
        self.shopn2.valueChanged.connect(self.reshop2)

        with open('config.txt', encoding='utf-8') as f:
            gg = f.readlines()
            if gg[0] == '\n':
                for i in self.wins:
                    for el in i:
                        el.hide()
                self.mainlabel.setText('                                      Add your name:')
                self.nameedit.show()
                self.btncnok.setText('add name')
                self.btncnok.clicked.connect(self.firststart)
                self.btncnok.show()
            else:
                self.start()

    def keyPressEvent(self, event):
        if self.winnew == 5:
            if event.key() == Qt.Key_Z:
                self.btna1.click()
            elif event.key() == Qt.Key_X:
                self.btna2.click()
            elif event.key() == Qt.Key_C:
                self.btna3.click()

    def firststart(self):
        name = self.nameedit.text()
        x = 0
        if name.split():
            for el in name:
                if el.lower() not in 'abcdefghigklmnopqrstuvwxyz':
                    x += 1
            if x == 0:
                self.name = name
                self.nameedit.setText('')
                self.mainlabel.setText('                             Add your class')
                self.nameedit.hide()
                self.btncnok.setText('change')
                self.btncnok.clicked.disconnect(self.firststart)
                self.btncnok.hide()
                self.btnc1.clicked.connect(self.firststart1)
                self.btnc2.clicked.connect(self.firststart1)
                self.btnc1.show()
                self.btnc2.show()
            else:
                self.mainlabel.setText('                                         Invalid name!')
        else:
            self.mainlabel.setText('                                         Invalid name!')

    def firststart1(self):
        gg = self.sender().text()
        self.clas = gg
        self.btnc1.clicked.disconnect(self.firststart1)
        self.btnc2.clicked.disconnect(self.firststart1)
        self.btnc1.hide()
        self.btnc2.hide()
        self.mainlabel.setText('                            Arifmetic game                            ')
        with open('config.txt', 'w') as f:
            f.write(self.name + '\n' + gg + '\n' + str(self.balance) + '\n'
                    + str(self.podskaza1) + '\n' + str(self.podskaza2) + '\n1')
        for i in self.btns:
            i.clicked.connect(self.okno)
        for el in self.wins[0]:
            el.show()

    def start(self):
        for i in range(1, len(self.wins)):
            for el in self.wins[i]:
                el.hide()
        for i in self.btns:
            i.clicked.connect(self.okno)
        print(self.musicnum)

    def changeclass(self, cl):
        with open('config.txt', encoding='utf-8') as f:
            gg = f.readlines()
            gg[1] = cl + '\n'
            self.clas = cl
        with open('config.txt', 'w') as f:
            for el in gg:
                f.write(el)

    def smenapodskazi(self):
        with open('config.txt', encoding='utf-8') as f:
            gg = f.readlines()
        with open('config.txt', 'w') as f:
            gg[3] = str(self.podskaza1) + '\n'
            gg[4] = str(self.podskaza2) + '\n'
            for el in gg:
                f.write(el)
        self.btnpod1.setText(f'remove one answer: {self.podskaza1}')
        self.btnpod2.setText(f'skip the question: {self.podskaza2}')

    def smenan(self, name):
        x = 0
        if name.split():
            for el in name:
                if el.lower() not in 'abcdefghigklmnopqrstuvwxyz':
                    x += 1
            if x == 0:
                with open('config.txt', encoding='utf-8') as f:
                    gg = f.readlines()
                gg[0] = name + '\n'
                with open('config.txt', 'w') as f:
                    for el in gg:
                        f.write(el)
                self.nameedit.setText('Succesfully')
                self.name = name
            else:
                self.nameedit.setText('                                         Invalid name!')
        else:
            self.nameedit.setText('                                         Invalid name!')

    def smenabalanca(self):
        with open('config.txt', encoding='utf-8') as f:
            gg = f.readlines()
        with open('config.txt', 'w') as f1:
            gg[2] = str(self.balance) + '\n'
            for el in gg:
                f1.write(el)

    def reshop1(self, value_as_int):
        self.kolichestvopodskazok1 = 50 * int(value_as_int)
        self.shoptxt3.setText('sum = ' + str(self.kolichestvopodskazok1 + self.kolichestvopodskazok2) + ' coins')

    def reshop2(self, value_as_int):
        self.kolichestvopodskazok2 = 100 * int(value_as_int)
        self.shoptxt3.setText('sum = ' + str(self.kolichestvopodskazok2 + self.kolichestvopodskazok1) + ' coins')

    def buy(self):
        gg = self.kolichestvopodskazok2 + self.kolichestvopodskazok1
        if gg != 0:
            if int(self.balance) >= gg:
                self.balance = str(int(self.balance) - gg)
                self.podskaza1 += self.kolichestvopodskazok1 // 50
                self.podskaza2 += self.kolichestvopodskazok2 // 100
                self.txtbalance.setText('                        Balance: ' + str(self.balance) + ' coins')
                with open('config.txt', encoding='utf-8') as f:
                    x = f.readlines()
                with open('config.txt', 'w') as f1:
                    x[2] = str(self.balance) + '\n'
                    x[3] = str(self.podskaza1) + '\n'
                    x[4] = str(self.podskaza2) + '\n'
                    for el in x:
                        f1.write(el)
                self.shopn1.setValue(0)
                self.shopn2.setValue(0)
                self.shoptxt3.setText('Succesfully')

            else:
                self.shopn1.setValue(0)
                self.shopn2.setValue(0)
                self.shoptxt3.setText('No money')

    def startgg(self):
        self.workcoin = 0
        self.kolichestvo = 0
        self.btnpod1.setText(f'remove one answer: {self.podskaza1}')
        self.btnpod2.setText(f'skip the question: {self.podskaza2}')
        print(self.clas)
        if self.clas == 'class 1':
            self.playclass1()
        elif self.clas == 'class 2':
            self.playclass2()

    def playclass1(self):
        spisokvarotvetov = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        spisokotvetov = []
        vibor = random.randint(0, 1)
        if vibor == 0:
            if self.kolichestvo < 10:
                n1 = random.randint(1, 9)
                n2 = random.randint(1, 10 - n1)

                self.answer = n1 + n2

                self.quastionlabel.setText(f'{n1} + {n2} = ?')
            elif self.kolichestvo >= 10:
                n1 = random.randint(1, 8)
                n2 = random.randint(1, 9 - n1)
                n3 = random.randint(1, 10 - n2 - n1)

                self.answer = n1 + n2 + n3

                self.quastionlabel.setText(f'{n1} + {n2} + {n3} = ?')
        else:
            if self.kolichestvo < 10:
                n1 = random.randint(2, 10)
                n2 = random.randint(1, n1 - 1)

                self.answer = n1 - n2

                self.quastionlabel.setText(f'{n1} - {n2} = ?')
            elif self.kolichestvo >= 10:
                n1 = random.randint(3, 10)
                n2 = random.randint(1, n1 - 2)
                n3 = random.randint(1, n1 - n2 - 1)

                self.answer = n1 - n2 - n3

                self.quastionlabel.setText(f'{n1} - {n2} - {n3} = ?')
        spisokvarotvetov.remove(self.answer)
        spisokotvetov.append(self.answer)
        answer1 = random.choice(spisokvarotvetov)
        spisokotvetov.append(answer1)
        spisokvarotvetov.remove(answer1)
        answer2 = random.choice(spisokvarotvetov)
        spisokotvetov.append(answer2)
        self.vivodotveta(spisokotvetov)

    def playclass2(self):
        spisokotvetov = []
        s = []
        if self.kolichestvo < 10:
            vibor = random.randint(1, 4)
            if vibor == 1:
                n1 = random.randint(10, 88)
                n2 = random.randint(10, 99 - n1)
                self.answer = n1 + n2
                self.quastionlabel.setText(f'{n1} + {n2} = ?')
                for i in range(10, 100):
                    if i != self.answer:
                        s.append(i)
            elif vibor == 2:
                n1 = random.randint(20, 99)
                n2 = random.randint(10, n1 - 1)
                self.answer = n1 - n2
                self.quastionlabel.setText(f'{n1} - {n2} = ?')
                for i in range(1, 100):
                    if i != self.answer:
                        s.append(i)
            elif vibor == 3:
                n1 = random.randint(1, 9)
                n2 = random.randint(1, 9)
                self.answer = n1 * n2
                self.quastionlabel.setText(f'{n1} * {n2} = ?')
                for i in range(1, 9):
                    for j in range(1, 9):
                        if i * j != self.answer:
                            s.append(i * j)
            elif vibor == 4:
                n1 = random.randint(2, 9)
                n2 = random.randint(2, 9)
                n3 = n1 * n2
                s = [2, 3, 4, 5, 6, 7, 8, 9]
                s.remove(n1)
                self.answer = n1
                self.quastionlabel.setText(f'{n3} / {n2} = ?')
        else:
            z = random.randint(1, 2)
            if z == 1:
                z1 = random.randint(1, 2)
                n1 = random.randint(2, 9)
                n2 = random.randint(2, 9)
                if z1 == 1:
                    n3 = random.randint(1, 99 - n1 * n2)
                    self.answer = n1 * n2 + n3
                    self.quastionlabel.setText(f'{n1} * {n2} + {n3} = ?')
                    for i in range(5, 100):
                        if i != self.answer:
                            s.append(i)
                elif z1 == 2:
                    n3 = random.randint(1, n1 * n2 - 1)
                    self.answer = n1 * n2 - n3
                    self.quastionlabel.setText(f'{n1} * {n2} - {n3} = ?')
                    for i in range(1, 81):
                        if i != self.answer:
                            s.append(i)
            else:
                z1 = random.randint(1, 2)
                n1 = random.randint(2, 9)
                n2 = random.randint(2, 9)
                n3 = n1 * n2
                if z1 == 1:
                    n4 = random.randint(1, 99 - n1)
                    self.answer = n3 // n2 + n4
                    self.quastionlabel.setText(f'{n3} / {n2} + {n4} = ?')
                    for i in range(5, 99):
                        if i != self.answer:
                            s.append(i)
                elif z1 == 2:
                    n4 = random.randint(1, n1 - 1)
                    self.answer = n3 // n2 - n4
                    self.quastionlabel.setText(f'{n3} / {n2} - {n4} = ?')
                    for i in range(1, 8):
                        if i != self.answer:
                            s.append(i)
        answer1 = random.choice(s)
        s.remove(answer1)
        answer2 = random.choice(s)
        spisokotvetov.append(str(self.answer))
        spisokotvetov.append(str(answer1))
        spisokotvetov.append(str(answer2))
        self.vivodotveta(spisokotvetov)

    def vivodotveta(self, spisokotvetov):
        answer1 = random.choice(spisokotvetov)
        spisokotvetov.remove(answer1)
        answer2 = random.choice(spisokotvetov)
        spisokotvetov.remove(answer2)
        answer3 = spisokotvetov[0]

        self.btna1.setText(str(answer1))
        self.btna2.setText(str(answer2))
        self.btna3.setText(str(answer3))

        self.answerlist = [str(answer1), str(answer2), str(answer3)]

    def win(self):
        self.kolichestvo += 1
        self.mainlabel.setText(f'                         Player {self.name}     {self.clas}                    \n'
                               f'                         Completed levels: {self.kolichestvo}                     \n')
        if self.clas == 'class 1':
            if self.kolichestvo < 10:
                self.balance = int(self.balance) + 3
                self.workcoin += 3
            else:
                self.balance = int(self.balance) + 5
                self.workcoin += 5
            self.smenabalanca()
            self.playclass1()
        if self.clas == 'class 2':
            if self.kolichestvo < 10:
                self.balance = int(self.balance) + 5
                self.workcoin += 5
            else:
                self.balance = int(self.balance) + 8
                self.workcoin += 8
            self.smenabalanca()
            self.playclass2()

    def lose(self):
        self.winnew = 6
        self.winold = 5
        self.mainlabel.setText(f'Nice try {self.name}! \nYou completed {self.kolichestvo} levels and'
                               f' got {self.workcoin} coins!')

    def gomusic(self):
        if self.musicnum == 1:
            self.player.play()
            self.btnmusic.setText('remove music')
        else:
            self.player.stop()
            self.btnmusic.setText('play music')

    def changemusic(self):
        if self.musicnum == 1:
            self.musicnum = 0
        else:
            self.musicnum = 1
        with open('config.txt', encoding='utf-8') as t:
            lines = t.readlines()
            lines[5] = str(self.musicnum)
        with open('config.txt', 'w') as t1:
            for el in lines:
                t1.write(el)
        self.gomusic()

    def smenaokna(self):
        for el in self.wins[self.winold]:
            el.hide()
        for el in self.wins[self.winnew]:
            el.show()
        if self.winnew == 0:
            self.mainlabel.setText('                            Arifmetic game                            ')
        elif self.winnew == 1:
            self.mainlabel.setText('                               Play menu                                ')
        elif self.winnew == 2:
            self.mainlabel.setText(f'                                Settings menu                            \n'
                                   f'                                Class: {self.clas}\n'
                                   f'                                Name: {self.name}\n')
        elif self.winnew == 3:
            self.mainlabel.setText(f'                                          Settings name                          '
                                   f'  \n'
                                   f'                                          Name: {self.name}\n')
        elif self.winnew == 4:
            self.mainlabel.setText(
                '                                                 Shop                               ')
        elif self.winnew == 5:
            self.mainlabel.setText(f'                         Player {self.name}     {self.clas}                    \n'
                                   f'                         Completed levels: {self.kolichestvo}            '
                                   f'         \n')

    def okno(self):
        x = self.sender().text()
        print(x)
        if x == 'play':
            self.winnew = 1
            self.winold = 0
        elif x == 'start':
            self.winnew = 5
            self.winold = 1
            self.startgg()
        elif x == 'end game':
            self.lose()
        elif x.isnumeric():
            if int(x) == self.answer:
                self.win()
            else:
                self.lose()
        elif x == 'Continue':
            self.mainlabel.setText('                            Arifmetic game                            ')
            self.winnew = 1
            self.winold = 6
            self.smenaokna()
            self.winold = 0
        elif 'remove one answer' in x:
            if self.btna1.text() != 'no answer':
                if self.btna2.text() != 'no answer':
                    if self.btna3.text() != 'no answer':
                        if self.podskaza1 > 0:
                            s = []
                            if str(self.answer) != self.answerlist[0]:
                                s.append(self.btna1)
                            if str(self.answer) != self.answerlist[1]:
                                s.append(self.btna2)
                            if str(self.answer) != self.answerlist[2]:
                                s.append(self.btna3)
                            g = random.choice(s)
                            g.setText('no answer')
                            self.podskaza1 -= 1
                            self.smenapodskazi()
        elif 'skip the question' in x:
            if self.podskaza2 > 0:
                self.podskaza2 -= 1
                self.smenapodskazi()
                self.win()
        elif x == 'shop':
            self.txtbalance.setText(f'Balance: {self.balance} coins\nMinus one answer: {self.podskaza1}'
                                    f'\nSkip the question: {self.podskaza2}')
            self.winnew = 4
            self.winold = 1
        elif x == 'buy':
            self.buy()
            self.txtbalance.setText(f'Balance: {self.balance} coins\nMinus one answer: {self.podskaza1}'
                                    f'\nSkip the question: {self.podskaza2}')
        elif x == 'settings':
            self.winnew = 2
            self.winold = 0
        elif 'music' in x:
            self.changemusic()
        elif x == 'exit':
            exit()
        elif x == 'change name':
            self.winnew = 3
            self.winold = 2
        elif x == 'change':
            self.smenan(self.nameedit.text())
            self.mainlabel.setText(f'                                          Settings name                '
                                   f'            \n'
                                   f'                                          Name: {self.name}\n')
        elif 'class' in x:
            self.changeclass(x)
            self.mainlabel.setText(f'                                Settings menu                            \n'
                                   f'                                Class: {self.clas}\n'
                                   f'                                Name: {self.name}\n')
        elif x == 'back':
            gg = self.winnew
            if gg == 3:
                self.nameedit.setText('')
            elif gg == 4:
                self.shopn1.setValue(0)
                self.shopn2.setValue(0)
            self.winnew = self.winold
            self.winold = gg
            self.shoptxt3.setText('sum = 0 coins')
        self.smenaokna()
        if x == 'back':
            self.winold -= 2
            if self.winnew == 2:
                self.winold = 0
            elif self.winnew == 4:
                self.winold = 1
            elif self.winnew == 1:
                self.winold = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

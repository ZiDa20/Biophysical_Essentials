PROTOCOL-FILE 9

PROTOCOL  "Test Pulse"
REPEAT                           ( 0.000s): sweeps 10.00s
   Amplifier                        ( 0.000s): C-slow
   #Command                          ( 0.000s): "  E  AutoRsComp"
   Sweep                            ( 0.000s): "Block Pulse","",""
END_REPEAT

PROTOCOL  "IV & Rheo"
Command                          ( 0.000s): "E Mode 3; Whole Cell"
#Command                          ( 0.000s): "E Gain 7; 0.5mV/pA"
Command                          ( 0.000s): "E VHold -60.0mV"
Command                          ( 0.000s): "O YScale 1.00 "
Amplifier                        ( 0.000s): C-slow
#Series                           ( 0.000s): "IV","",""
#Amplifier                        ( 0.000s): C-slow
Series                           ( 0.000s): "IV-120","",""
Amplifier                        ( 0.000s): C-slow
Wait                             ( 0.000s): abs  5.000s
Series                           ( 0.000s): "IV-40","",""
Amplifier                        ( 0.000s): C-slow
Wait                             ( 0.000s): abs  5.000s
Series                           ( 0.000s): "Inact","",""
Command                          ( 10.00s): "E Mode 4; C-Clamp"
Command                          ( 5.000s): "E IHold 0.0pA"
Command                          ( 0.000s): "O YScale 5.0 "
Series                           ( 10.00s): "CClamp","",""
#Series                           ( 10.00s): "InputRes.","",""
#Wait                             ( 0.000s): abs  10.00s
#Series                           ( 10.00s): "APfastCI","",""
#Wait                             ( 0.000s): abs  10.00s
Series                           ( 10.00s): "Rheobase","",""
Series                           ( 0.000s): "Rheobase2","",""

PROTOCOL  "2xRheo&Ramp"
Series                           ( 0.000s): "5xRheo","",""
Wait                             ( 0.000s): abs  10.00s
Series                           ( 10.00s): "RheoRamp","",""
Wait                             ( 0.000s): abs  10.00s
Series                           ( 10.00s): "2xRheobase","",""
Chain                            ( 0.000s): "1min"
#Chain                            ( 0.000s): "Heat Ramp"

PROTOCOL  "Heat Ramp"
Command                          ( 0.000s): "E Mode 3; Whole Cell"
Command                          ( 0.000s): "E Gain 7; 0.5mV/pA"
Command                          ( 0.000s): "E VHold -60.0mV"
Command                          ( 0.000s): "O YScale 4.00 "
Command                          ( 0.000s): "  O  YOffset        100.m"
Amplifier                        ( 0.000s): C-slow
Series                           ( 0.000s): "1min","",""
REPEAT                           ( 0.000s): sweeps 30.00s
   Amplifier                        ( 0.000s): C-slow
   Sweep                            ( 0.000s): "Heat Ramp","",""
END_REPEAT

PROTOCOL  "1min"
Command                          ( 0.000s): "E Mode 3; Whole Cell"
Command                          ( 0.000s): "E Gain 7; 0.5mV/pA"
Command                          ( 0.000s): "E VHold -60.0mV"
Command                          ( 0.000s): "O YScale 4.00 "
Command                          ( 0.000s): "  O  YOffset        100.m"
Amplifier                        ( 0.000s): C-slow
REPEAT                           ( 0.000s): 10 x 0.000s
   Series                           ( 0.000s): "1min","",""
END_REPEAT
#REPEAT                           ( 0.000s): sweeps 30.00s
   #Amplifier                        ( 0.000s): C-slow
   #Sweep                            ( 0.000s): "Heat Ramp","",""
#END_REPEAT

PROTOCOL  "SETUP"
Command                          ( 0.000s): "E Reset"
Command                          ( 0.000s): "N TimerSet"
Command                          ( 0.000s): "E Mode 3; Whole Cell"
Command                          ( 0.000s): "O YScale 1.00 "
Command                          ( 0.000s): "  O  YOffset        0.00 "
Command                          ( 0.000s): "E Pulsemode 1; Single Test Pulse"
Command                          ( 0.000s): "E PulseAmp -10.0mV"
Command                          ( 0.000s): "E PulseDur 10.0ms"
Command                          ( 0.000s): "E Gain 9;  2.0 mV/pA"
Command                          ( 0.000s): "E AutoZero"
Command                          ( 0.000s): "E PulseOn TRUE"
Command                          ( 0.000s): "E SaveRpip"
Beep                             ( 0.000s)

PROTOCOL  "SEAL"
Command                          ( 0.000s): "E Mode 3; Whole Cell"
Command                          ( 0.000s): "E Vhold -60mV"
Command                          ( 0.000s): "E AutoCFast"
Command                          ( 0.000s): "E AutoCFast"
Command                          ( 0.000s): "E Gain 11; 10 mV/pA"
Beep                             ( 0.000s)

PROTOCOL  "WHOLE-CELL"
Command                          ( 0.000s): "N TimerSet"
Command                          ( 0.000s): "E Mode 3; Whole Cell"
Command                          ( 0.000s): "E Gain 7; 0.5 mV/pA"
Command                          ( 0.000s): "E Vhold -60mV"
Command                          ( 0.000s): "E CSlow 30.00pF"
Command                          ( 0.000s): "E RSeries 10.0MOhm"
Command                          ( 0.000s): "E AutoCSlow"
Command                          ( 0.000s): "E AutoCSlow"
#Command                          ( 0.000s): "E RsMode 1"
#Command                          ( 0.000s): "E RsComp 10%"
Beep                             ( 0.000s)

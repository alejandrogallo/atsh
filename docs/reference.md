AT Commands Tutorial {#at-commands-tutorial .single-title}
====================


The controlling of a MODEM can be done by using instructions or AT
commands. Here term AT in the command is the short form of an Attention.
The command line used in every modem starts with 'AT' otherwise 'at' so
these commands are named as AT commands. There are many commands which
are used for controlling modems (wired dial-up) like ATD -- Dial, ATA --
Answer, ATH -- Hook control & ATO -- Come back to the online data state.
These are supported by modems like mobile phones, GSM or GPRS. There are
some commands which support GSM. These **commands which are used for
[GSM](https://www.elprocus.com/gsm-architecture-features-working/)**
mainly include SMS based commands like AT+CMGS, AT+CMSS, AT+CMGL &
AT+CMGR. Here the prefix AT in these commands informs the modem
regarding the begin of a command line.

What are AT Commands? {#what-are-at-commands style="text-align: justify;"}
---------------------

In AT commands, AT stands for Attention and these commands are used for
controlling MODEMs. These types of commands are taken from the commands
like Hayes. The Hayes-commands mainly used in the Hayes smart modems.
These commands are indicated with the term AT to specify the attention
from MODEM. These commands are mainly used in the devices which use
machine-to-machine communication to communicate with a PC. These devices
consist of a subset of the Hayes command set with other extensive AT
commands.

[]{.underline}

\

These commands are used in GSM, GPRS, or mobile phone MODEMs can be used
to access the information as well as services which include the
following.

-   The information & configuration related to phone otherwise [SIM
    card](https://www.elprocus.com/how-sim-card-works/) & MODEM.
-   The services like SMS, MMS and Fax services.
-   Voice and data link on a mobile network.

The basic commands are called as the Hayes subset commands and the
commands which are exact to a GSM network are known as extended AT
commands.


### Types of AT Commands {#types-of-at-commands style="text-align: justify;"}

These commands are classified into four types namely Test, Read, Set and
Execution.

**Test Command**

![PCBWay](/ad-creatives/pcbway-750x170-june-2020.gif)

![PCBWay](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20210%20140%22%3E%3C/svg%3E){.lazyload}

\

[]{.underline}

The test AT command is mainly used for checking the command's
compatibility using a modem. The SYNTAX for this command is AT \< name
of the command\>. The best example of this command is AD =?

**Read Command**

[]{.underline}

The Read command is mainly used for changing the settings of mobile
phone otherwise modem required for operations. The SYNTAX for this
command is AT \< name of the command\>. The best example of this command
is AT+CBC =?

**Set Command**

The Set command is mainly used for making modifications in the settings
of mobile phone otherwise modem required for operations. The SYNTAX for
this command is AT \< name of the command\> = Value 1, Value 2....Value
N. The best example of this is AT+CBC ="+923140", 110

**Execution Command**

The Execution command is mainly used for executing the said operation.
The SYNTAX for this command is AT \< name of the command\> =
parameter-1, parameter-2... parameter-N. The best example of this is
AT+CBC = 2,"+ 4867512120", 210.

### AT Commands List {#at-commands-list style="text-align: justify;"}

The list of AT commands is discussed below.

**For Testing**

AT command is used to check the communication among the computer as well
as module

**For Controlling Call**

The commands used for controlling call mainly include the following.

-   ATA command is an answer command
-   ATH is used to hang up call
-   ATD is a dial command
-   ATM command is used to check speaker mode
-   ATT command is used to fix tone dial like the default
-   ATL command is used to check speaker loudness
-   AT+CSTA command is used to select an address type
-   ATP command is used to fix pulse dial like the default
-   ATO is a Go on-line command
-   AT+CRC command is used for cellular result codes

**For Data Card Control**

The commands used for data call control mainly include the following.

-   ATI command is used for identification
-   AT&F command is used to reinstate factory settings
-   ATZ command is used to remind stored profile
-   AT&W command is used to store parameters within the specified
    profile
-   AT+CSTA command is used to select an address type
-   AT+GMM command is used to identify request model
-   AT&V command is used to examine the active configuration
-   AT+CLCK command is used for facility lock
-   AT+GCAP command is used to complete request of a capabilities list
-   AT&Y command is used to choose power-up option
-   AT+GMR command is used to identify request revision
-   AT+COLP is a connected line recognition presentation
-   AT+GMI is a request manufacturer identification command
-   AT+GSN command is used to request product IMEI number.

**For Phone Control**

The commands used for [phone
control](https://www.elprocus.com/know-how-a-cell-phone-controlled-robotic-vehicle-works/)
mainly include the following.

-   AT+CBC command is used to charge the battery
-   AT+CGMR command is used to identify request revision
-   AT+CGSN command is used to request product serial number
-   AT+CMEE command is used to report the error of mobile equipment
-   AT+CPBF command is used to find the entries of the phone book
-   AT+CPBR command is used to read entries of the phone book
-   AT+CPBS command is used to choose the storage of phone book memory
-   AT+CSCS command is used to select TE character set
-   AT+CPBW command is used to write phone book entry
-   AT+CGMM command is used to identify request model
-   AT+CGMI command is used to identify request manufacturer
-   AT+CSQ is a signal quality command
-   AT+CPAS command is used to check the status of phone activity

**Computer Data Interface**

The commands used for computer data interface mainly include the
following.\
ATE is an Echo command

-   ATQ command results code suppression
-   ATX command is used to select response rang
-   AT+ICF command is used to framing the character of DTE-DCE
-   AT&Q command is used to identify an option for communications mode
-   AT&C command is used to identify the usage of DCD
-   AT&D command is used to identify the usage of DTR
-   ATV command is a define response format
-   AT+IFC command is used to control local flow for DTE-DCE
-   AT&K command is used to choose flow control
-   AT&S command is used to identify an option for DSR
-   AT+IPR command is used to set DTE rate

**For Service**

The commands used for service mainly include the following.

-   AT+CLIP command is used for calling line recognition presentation
-   AT+ILRR command is used for reporting DTE-DCE
-   AT+CR command is used to control service reporting
-   AT+DR command is used for reporting data compression

**For Network Communication Parameter**

The commands used for network
[communication](https://www.elprocus.com/what-is-a-communication-system-and-its-basic-elements/)
parameter mainly include the following.

-   ATB command is an option for a communications standard
-   AT+DS command is used to compress the data
-   AT+CEER command is used to extend error report
-   AT+CBST command is used to choose the type of bearer service
-   AT+CRLP command is a radio link
    [protocol](https://www.elprocus.com/communication-protocols/)

**For Miscellaneous**

The commands used for miscellaneous mainly include the following.

-   A/ command is used to the re-execute command line
-   AT\*C command is used to start SMS interpreter
-   AT? is used to command help
-   AT\*V command is used to activate V.25bis mode
-   AT\*T command is used to enter SMS block mode protocol
-   AT+CESP command is used to enter SMS block mode protocol
-   AT\*NOKIATEST command is used to test command

**For SMS Text Mode**

The commands used for SMS text mode mainly include the following.

-   AT+CSMS command is used to select message service
-   AT+CSMP command is used to fix text mode parameters
-   AT+CMGF command is used to format message
-   AT+CPMS command is used to choose message storage
-   AT+CRES command is used to restore settings
-   AT+CNMI command is used to indicate a new message to TE
-   AT+CSCA command is used for service center address
-   AT+CSCB command is used to choose types of cell broadcast message
-   AT+CMGR command is used to read the message
-   AT+CSDH command is used to illustrate text mode parameters
-   AT+CSAS command is used to save settings
-   AT+CMSS command is used to send a message from storage
-   AT+CMGD command is used to delete the message
-   AT+CMGL command is used to list messages
-   AT+CMGS command is used to send message
-   AT+CMGW command is used to write a message to memory

**SMS PDU Mode**

The commands used for SMS PDU mode mainly include the following.

-   AT+CMGL command is used to list messages
-   AT+CMGW command is used to write a message to memory
-   AT+CMGS command is used to send message
-   AT+CMGR command is used to read the message

**ESP8266 AT Commands**

The ESP8266 Commands mainly include the following.

-   AT+RST command is used to restart the module
-   AT+CWQAP command is used to quit the AP
-   AT+ CIPSTATUS command is used to obtain the connection status
-   AT+CWJAP command is used to join the AP
-   AT+CWMODE command is used to
    [wi-fi](https://www.elprocus.com/how-does-wifi-work/) mode
-   AT+CWLAP command is used to list the AP
-   AT+CIPSTART command is used to set up the connection for TCP
    otherwise UDP
-   AT+CIPCLOSE command is used to close the connection for TCP
    otherwise UDP
-   AT+ CIPMUX command is used to fix multiple connections
-   AT+ CWSAP command is used to fix the parameters of AP
-   AT+ CIPSERVER command is used to set as serve
-   AT+CIPSEND command is used to send data
-   AT+CIFSR command is used to obtain an IP address
-   IPD command is used to receive data

#
# PySNMP MIB module PARALLEL-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/PARALLEL-MIB
# Produced by pysmi-0.0.7 at Sun Feb 14 00:23:18 2016
# On host bldfarm platform Linux version 4.1.13-100.fc21.x86_64 by user goose
# Using Python version 3.5.0 (default, Jan  5 2016, 17:11:52) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
( InterfaceIndex, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
( ModuleCompliance, ObjectGroup, NotificationGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
( Counter32, Gauge32, NotificationType, TimeTicks, ObjectIdentity, ModuleIdentity, transmission, Integer32, Counter64, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, iso, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "NotificationType", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "transmission", "Integer32", "Counter64", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "iso")
( TextualConvention, DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
para = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 34))
if mibBuilder.loadTexts: para.setLastUpdated('9405261700Z')
if mibBuilder.loadTexts: para.setOrganization('IETF Character MIB Working Group')
if mibBuilder.loadTexts: para.setContactInfo('        Bob Stewart\n                Postal: Xyplex, Inc.\n                        295 Foster Street\n                        Littleton, MA 01460\n\n                   Tel: 508-952-4816\n                   Fax: 508-952-4887\n                E-mail: rlstewart@eng.xyplex.com')
if mibBuilder.loadTexts: para.setDescription('The MIB module for Parallel-printer-like hardware devices.')
paraNumber = MibScalar((1, 3, 6, 1, 2, 1, 10, 34, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraNumber.setDescription('The number of ports (regardless of their current\n           state) in the Parallel-printer-like port table.')
paraPortTable = MibTable((1, 3, 6, 1, 2, 1, 10, 34, 2), )
if mibBuilder.loadTexts: paraPortTable.setDescription('A list of port entries.  The number of entries is\n           given by the value of paraNumber.')
paraPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 34, 2, 1), ).setIndexNames((0, "PARALLEL-MIB", "paraPortIndex"))
if mibBuilder.loadTexts: paraPortEntry.setDescription('Status and parameter values for a port.')
paraPortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraPortIndex.setDescription('The value of ifIndex for the port.  By convention\n           and if possible, hardware port numbers map directly\n           to external connectors.  The value for each port must\n           remain constant at least from one re-initialization\n           of the network management agent to the next.')
paraPortType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3,))).clone(namedValues=NamedValues(("other", 1), ("centronics", 2), ("dataproducts", 3),))).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraPortType.setDescription("The port's hardware type.")
paraPortInSigNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraPortInSigNumber.setDescription('The number of input signals for the port in the\n           input signal table (paraPortInSigTable).  The table\n           contains entries only for those signals the software\n           can detect and that are useful to observe.')
paraPortOutSigNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraPortOutSigNumber.setDescription('The number of output signals for the port in the\n           output signal table (paraPortOutSigTable).  The\n           table contains entries only for those signals the\n           software can assert and that are useful to observe.')
paraInSigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 34, 3), )
if mibBuilder.loadTexts: paraInSigTable.setDescription('A list of port input control signal entries.')
paraInSigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 34, 3, 1), ).setIndexNames((0, "PARALLEL-MIB", "paraInSigPortIndex"), (0, "PARALLEL-MIB", "paraInSigName"))
if mibBuilder.loadTexts: paraInSigEntry.setDescription('Input control signal status for a hardware port.')
paraInSigPortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 3, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraInSigPortIndex.setDescription('The value of paraPortIndex for the port to which\n           this entry belongs.')
paraInSigName = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5,))).clone(namedValues=NamedValues(("power", 1), ("online", 2), ("busy", 3), ("paperout", 4), ("fault", 5),))).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraInSigName.setDescription('Identification of a hardware signal.')
paraInSigState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3,))).clone(namedValues=NamedValues(("none", 1), ("on", 2), ("off", 3),))).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraInSigState.setDescription('The current signal state.')
paraInSigChanges = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraInSigChanges.setDescription("The number of times the signal has changed from\n           'on' to 'off' or from 'off' to 'on'.")
paraOutSigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 34, 4), )
if mibBuilder.loadTexts: paraOutSigTable.setDescription('A list of port output control signal entries.')
paraOutSigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 34, 4, 1), ).setIndexNames((0, "PARALLEL-MIB", "paraOutSigPortIndex"), (0, "PARALLEL-MIB", "paraOutSigName"))
if mibBuilder.loadTexts: paraOutSigEntry.setDescription('Output control signal status for a hardware port.')
paraOutSigPortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 4, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraOutSigPortIndex.setDescription('The value of paraPortIndex for the port to which\n           this entry belongs.')
paraOutSigName = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5,))).clone(namedValues=NamedValues(("power", 1), ("online", 2), ("busy", 3), ("paperout", 4), ("fault", 5),))).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraOutSigName.setDescription('Identification of a hardware signal.')
paraOutSigState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3,))).clone(namedValues=NamedValues(("none", 1), ("on", 2), ("off", 3),))).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraOutSigState.setDescription('The current signal state.')
paraOutSigChanges = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraOutSigChanges.setDescription("The number of times the signal has changed from\n           'on' to 'off' or from 'off' to 'on'.")
paraConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 34, 5))
paraGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 34, 5, 1))
paraCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 34, 5, 2))
paraCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 34, 5, 2, 1)).setObjects(*(("PARALLEL-MIB", "paraGroup"),))
if mibBuilder.loadTexts: paraCompliance.setDescription('The compliance statement for SNMPv2 entities\n               which have Parallel-printer-like hardware\n               interfaces.')
paraGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 34, 5, 1, 1)).setObjects(*(("PARALLEL-MIB", "paraNumber"), ("PARALLEL-MIB", "paraPortIndex"), ("PARALLEL-MIB", "paraPortType"), ("PARALLEL-MIB", "paraPortInSigNumber"), ("PARALLEL-MIB", "paraPortOutSigNumber"), ("PARALLEL-MIB", "paraInSigPortIndex"), ("PARALLEL-MIB", "paraInSigName"), ("PARALLEL-MIB", "paraInSigState"), ("PARALLEL-MIB", "paraInSigChanges"), ("PARALLEL-MIB", "paraOutSigPortIndex"), ("PARALLEL-MIB", "paraOutSigName"), ("PARALLEL-MIB", "paraOutSigState"), ("PARALLEL-MIB", "paraOutSigChanges"),))
if mibBuilder.loadTexts: paraGroup.setDescription('A collection of objects providing information\n                applicable to all Parallel-printer-like interfaces.')
mibBuilder.exportSymbols("PARALLEL-MIB", paraOutSigPortIndex=paraOutSigPortIndex, paraInSigState=paraInSigState, paraInSigName=paraInSigName, paraNumber=paraNumber, paraOutSigState=paraOutSigState, paraOutSigName=paraOutSigName, paraPortOutSigNumber=paraPortOutSigNumber, paraPortTable=paraPortTable, PYSNMP_MODULE_ID=para, paraGroup=paraGroup, paraInSigChanges=paraInSigChanges, paraPortInSigNumber=paraPortInSigNumber, paraPortEntry=paraPortEntry, paraInSigPortIndex=paraInSigPortIndex, paraOutSigChanges=paraOutSigChanges, paraInSigTable=paraInSigTable, para=para, paraOutSigTable=paraOutSigTable, paraPortType=paraPortType, paraGroups=paraGroups, paraOutSigEntry=paraOutSigEntry, paraConformance=paraConformance, paraPortIndex=paraPortIndex, paraCompliance=paraCompliance, paraCompliances=paraCompliances, paraInSigEntry=paraInSigEntry)

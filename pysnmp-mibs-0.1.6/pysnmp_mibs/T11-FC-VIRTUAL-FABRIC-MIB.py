#
# PySNMP MIB module T11-FC-VIRTUAL-FABRIC-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/T11-FC-VIRTUAL-FABRIC-MIB
# Produced by pysmi-0.0.7 at Sun Feb 14 00:30:38 2016
# On host bldfarm platform Linux version 4.1.13-100.fc21.x86_64 by user goose
# Using Python version 3.5.0 (default, Jan  5 2016, 17:11:52) 
#
( OctetString, Integer, ObjectIdentifier, ) = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
( FcNameIdOrZero, fcmPortEntry, fcmInstanceIndex, fcmSwitchEntry, ) = mibBuilder.importSymbols("FC-MGMT-MIB", "FcNameIdOrZero", "fcmPortEntry", "fcmInstanceIndex", "fcmSwitchEntry")
( InterfaceIndex, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
( ModuleCompliance, ObjectGroup, NotificationGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
( MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, Counter64, mib_2, IpAddress, MibIdentifier, iso, Unsigned32, NotificationType, Gauge32, Counter32, TimeTicks, Integer32, ObjectIdentity, ) = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "Counter64", "mib-2", "IpAddress", "MibIdentifier", "iso", "Unsigned32", "NotificationType", "Gauge32", "Counter32", "TimeTicks", "Integer32", "ObjectIdentity")
( StorageType, RowStatus, DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "RowStatus", "DisplayString", "TextualConvention")
( T11FabricIndex, ) = mibBuilder.importSymbols("T11-TC-MIB", "T11FabricIndex")
t11FcVirtualFabricMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 147)).setRevisions(("2006-11-10 00:00",))
if mibBuilder.loadTexts: t11FcVirtualFabricMIB.setLastUpdated('200611100000Z')
if mibBuilder.loadTexts: t11FcVirtualFabricMIB.setOrganization('IETF IMSS (Internet and Management Support\n                     for Storage) Working Group')
if mibBuilder.loadTexts: t11FcVirtualFabricMIB.setContactInfo('\n                     Scott Kipp\n                     McDATA Corporation\n                Tel: +1 720 558-3452\n             E-mail: scott.kipp@mcdata.com\n             Postal: 4 McDATA Parkway\n                     Broomfield, CO USA 80021\n\n                     G D Ramkumar\n                     SnapTell, Inc.\n                Tel: +1 650-326-7627\n             E-mail: gramkumar@stanfordalumni.org\n             Postal: 2741 Middlefield Rd, Suite 200\n                     Palo Alto, CA USA 94306\n\n                     Keith McCloghrie\n                     Cisco Systems, Inc.\n                Tel: +1 408 526-5260\n             E-mail: kzm@cisco.com\n             Postal: 170 West Tasman Drive\n                     San Jose, CA USA 95134\n            ')
if mibBuilder.loadTexts: t11FcVirtualFabricMIB.setDescription('This module defines management information specific to\n         Fibre Channel Virtual Fabrics.  A Virtual Fabric is a\n\n\n\n         Fabric composed of partitions of switches, links and\n         N_Ports with a single Fabric management domain, Fabric\n         Services and independence from other Virtual Fabrics.\n\n         Copyright (C) The IETF Trust (2006).  This version of\n         this MIB module is part of RFC 4747; see the RFC itself for\n         full legal notices.')
t11vfObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 147, 1))
t11vfConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 147, 2))
t11vfCoreSwitchTable = MibTable((1, 3, 6, 1, 2, 1, 147, 1, 1), )
if mibBuilder.loadTexts: t11vfCoreSwitchTable.setDescription('A table of core switches supported by the current\n         management entity.')
t11vfCoreSwitchEntry = MibTableRow((1, 3, 6, 1, 2, 1, 147, 1, 1, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "T11-FC-VIRTUAL-FABRIC-MIB", "t11vfCoreSwitchSwitchName"))
if mibBuilder.loadTexts: t11vfCoreSwitchEntry.setDescription('Each entry represents one core switch.')
t11vfCoreSwitchSwitchName = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 1, 1, 1), FcNameIdOrZero().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(8,8),ValueSizeConstraint(16,16),)))
if mibBuilder.loadTexts: t11vfCoreSwitchSwitchName.setDescription('The Core Switch_Name (WWN) of this Core Switch.')
t11vfCoreSwitchMaxSupported = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1,4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11vfCoreSwitchMaxSupported.setDescription('In switches that do not support Virtual Fabrics,\n         this object has the value of 1.  If Virtual Fabrics\n         are supported, this object is the maximum number of\n         Virtual Fabrics supported by the Core Switch.  For\n         the purpose of this count, the Control VF_ID is\n         ignored.')
t11vfCoreSwitchStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 1, 1, 3), StorageType().clone('nonVolatile')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11vfCoreSwitchStorageType.setDescription("The storage type for this conceptual row.\n         Conceptual rows having the value 'permanent' need not\n         allow write-access to any columnar objects in the row.")
t11vfVirtualSwitchTable = MibTable((1, 3, 6, 1, 2, 1, 147, 1, 2), )
if mibBuilder.loadTexts: t11vfVirtualSwitchTable.setDescription('A table of Virtual Switches.  When one Core Switch\n         provides switching functions for multiple Virtual Fabrics,\n         that Core Switch is modeled as containing multiple\n         Virtual Switches, one for each Virtual Fabric.  This table\n         contains one row for every Virtual Switch on every Core\n         Switch.  This table augments the basic switch information in\n         the fcmSwitchTable Table in the FC-MGMT-MIB.')
t11vfVirtualSwitchEntry = MibTableRow((1, 3, 6, 1, 2, 1, 147, 1, 2, 1), )
fcmSwitchEntry.registerAugmentions(("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfVirtualSwitchEntry"))
t11vfVirtualSwitchEntry.setIndexNames(*fcmSwitchEntry.getIndexNames())
if mibBuilder.loadTexts: t11vfVirtualSwitchEntry.setDescription('An entry of the Virtual Switch table.  Each row is for a\n         Virtual Switch.\n\n         This table augments the fcmSwitchTable, i.e., every entry\n         in this table has a one-to-one correspondence with an\n         entry in the fcmSwitchTable.  At the time when the\n         fcmSwitchTable was defined, it applied to physical\n         switches.  With the definition and usage of virtual\n         switches, fcmSwitchTable now applies to virtual switches\n         as well as physical switches, and (in contrast to physical\n         switches) it is appropriate to provide the capability for\n         virtual switches to be created via remote management\n         applications, e.g., via SNMP.\n\n         So, this entry contains a RowStatus object (to allow the\n         creation of a virtual switch), as well as a StorageType\n         object.  Obviously, if a row is created/deleted in this\n         table, the corresponding row in the fcmSwitchTable will\n         be created/deleted.')
t11vfVirtualSwitchVfId = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 2, 1, 1), T11FabricIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: t11vfVirtualSwitchVfId.setDescription('The VF_ID of the Virtual Fabric for which this virtual\n         switch performs its switching function.  The Control\n         VF_ID is implicitly enabled and is not set.\n         Communication with the Control VF_ID is required.')
t11vfVirtualSwitchCoreSwitchName = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 2, 1, 2), FcNameIdOrZero().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(8,8),ValueSizeConstraint(16,16),))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11vfVirtualSwitchCoreSwitchName.setDescription('The Core Switch_Name (WWN) of the Core Switch that\n         contains this Virtual Switch.')
t11vfVirtualSwitchRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: t11vfVirtualSwitchRowStatus.setDescription('The status of this row.')
t11vfVirtualSwitchStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 2, 1, 4), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: t11vfVirtualSwitchStorageType.setDescription("The storage type for this conceptual row.\n         Conceptual rows having the value 'permanent' need not\n         allow write-access to any columnar objects in the row.")
t11vfPortTable = MibTable((1, 3, 6, 1, 2, 1, 147, 1, 3), )
if mibBuilder.loadTexts: t11vfPortTable.setDescription('A table of Port attributes related to Virtual Fabrics.')
t11vfPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 147, 1, 3, 1), )
fcmPortEntry.registerAugmentions(("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfPortEntry"))
t11vfPortEntry.setIndexNames(*fcmPortEntry.getIndexNames())
if mibBuilder.loadTexts: t11vfPortEntry.setDescription('Each entry represents a physical Port on a switch.\n         Switches that support Virtual Fabrics would add\n\n\n\n         these four additional columns to the fcmPortEntry\n         row.')
t11vfPortVfId = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 3, 1, 1), T11FabricIndex().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11vfPortVfId.setDescription('The Port VF_ID assigned to this Port.  The Port VF_ID is the\n         default Virtual Fabric that is assigned to untagged frames\n         arriving at this Port.  The Control VF_ID is implicitly\n         enabled and is not set.  Communication with the Control\n         VF_ID is required.')
t11vfPortTaggingAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3,))).clone(namedValues=NamedValues(("off", 1), ("on", 2), ("auto", 3),))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11vfPortTaggingAdminStatus.setDescription("This object is used to configure the administrative status\n         of Virtual Fabric tagging on this Port.\n\n         SET operation   Description\n         --------------  -------------------------------------------\n         off(1)          To disable Virtual Fabric tagging on this\n                         Port.\n\n         on(2)           To enable Virtual Fabric tagging on this\n\n\n\n                         Port if the attached Port doesn't\n                         prohibit it.\n\n         auto(3)         To enable Virtual Fabric tagging if the\n                         peer requests it.")
t11vfPortTaggingOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2,))).clone(namedValues=NamedValues(("off", 1), ("on", 2),))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11vfPortTaggingOperStatus.setDescription('This object is used to report the operational status of\n         Virtual Fabric tagging on this Port.\n\n         SET operation   Description\n         --------------  -------------------------------------------\n         off(1)          Virtual Fabric tagging is disabled on this\n                         Port.\n\n         on(2)           Virtual Fabric tagging is enabled on this\n                         Port.')
t11vfPortStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 3, 1, 4), StorageType().clone('nonVolatile')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11vfPortStorageType.setDescription("The storage type for this conceptual row, and for the\n         corresponding row in the augmented fcmPortTable.\n\n         Conceptual rows having the value 'permanent' need not\n         allow write-access to any columnar objects in the row.")
t11vfLocallyEnabledTable = MibTable((1, 3, 6, 1, 2, 1, 147, 1, 4), )
if mibBuilder.loadTexts: t11vfLocallyEnabledTable.setDescription("A table for assigning and reporting operational status of\n         locally-enabled Virtual Fabric IDs to Ports.  The set of\n         Virtual Fabrics operational on the Port is the bit-wise\n         'AND' of the set of locally-enabled VF_IDs of this Port\n         and the locally-enabled VF_IDs of the attached Port.")
t11vfLocallyEnabledEntry = MibTableRow((1, 3, 6, 1, 2, 1, 147, 1, 4, 1), ).setIndexNames((0, "T11-FC-VIRTUAL-FABRIC-MIB", "t11vfLocallyEnabledPortIfIndex"), (0, "T11-FC-VIRTUAL-FABRIC-MIB", "t11vfLocallyEnabledVfId"))
if mibBuilder.loadTexts: t11vfLocallyEnabledEntry.setDescription('An entry for each locally-enabled VF_ID on\n         each Port.')
t11vfLocallyEnabledPortIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 4, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: t11vfLocallyEnabledPortIfIndex.setDescription('The value of the ifIndex that identifies the Port.')
t11vfLocallyEnabledVfId = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 4, 1, 2), T11FabricIndex())
if mibBuilder.loadTexts: t11vfLocallyEnabledVfId.setDescription('A locally-enabled VF_ID on this Port.')
t11vfLocallyEnabledOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2,))).clone(namedValues=NamedValues(("off", 1), ("on", 2),))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11vfLocallyEnabledOperStatus.setDescription('This object is used to report the operational status of\n         Virtual Fabric tagging on this Port.\n\n         SET operation   Description\n         --------------  -------------------------------------------\n         off(1)          Virtual Fabric tagging is disabled on this\n                         Port.\n\n         on(2)           Virtual Fabric tagging is enabled on this\n                         Port.')
t11vfLocallyEnabledRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: t11vfLocallyEnabledRowStatus.setDescription("The status of this conceptual row.\n\n             When a row in this table is in 'active(1)' state,\n             no object in that row can be modified except\n             t11vfLocallyEnabledRowStatus and\n             t11vfLocallyEnabledStorageType.")
t11vfLocallyEnabledStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 4, 1, 5), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: t11vfLocallyEnabledStorageType.setDescription("The storage type for this conceptual row.\n             Conceptual rows having the value 'permanent' need not\n             allow write-access to any columnar objects in the row.")
t11vfMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 147, 2, 1))
t11vfMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 147, 2, 2))
t11vfMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 147, 2, 1, 1)).setObjects(*(("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfGeneralGroup"),))
if mibBuilder.loadTexts: t11vfMIBCompliance.setDescription('Describes the requirements for compliance to the\n         Fibre Channel Virtual Fabric MIB.')
t11vfGeneralGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 147, 2, 2, 1)).setObjects(*(("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfCoreSwitchMaxSupported"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfVirtualSwitchVfId"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfVirtualSwitchCoreSwitchName"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfVirtualSwitchRowStatus"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfPortVfId"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfPortTaggingAdminStatus"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfLocallyEnabledOperStatus"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfPortTaggingOperStatus"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfLocallyEnabledRowStatus"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfCoreSwitchStorageType"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfVirtualSwitchStorageType"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfPortStorageType"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfLocallyEnabledStorageType"),))
if mibBuilder.loadTexts: t11vfGeneralGroup.setDescription('A collection of objects for monitoring and\n             configuring Virtual Fabrics in a Fibre Channel switch.')
mibBuilder.exportSymbols("T11-FC-VIRTUAL-FABRIC-MIB", t11vfPortTaggingAdminStatus=t11vfPortTaggingAdminStatus, t11vfLocallyEnabledStorageType=t11vfLocallyEnabledStorageType, t11vfVirtualSwitchEntry=t11vfVirtualSwitchEntry, t11vfGeneralGroup=t11vfGeneralGroup, t11vfVirtualSwitchTable=t11vfVirtualSwitchTable, t11vfLocallyEnabledOperStatus=t11vfLocallyEnabledOperStatus, t11vfCoreSwitchStorageType=t11vfCoreSwitchStorageType, PYSNMP_MODULE_ID=t11FcVirtualFabricMIB, t11vfObjects=t11vfObjects, t11vfMIBGroups=t11vfMIBGroups, t11vfPortEntry=t11vfPortEntry, t11vfPortTable=t11vfPortTable, t11vfLocallyEnabledVfId=t11vfLocallyEnabledVfId, t11vfMIBCompliances=t11vfMIBCompliances, t11FcVirtualFabricMIB=t11FcVirtualFabricMIB, t11vfPortTaggingOperStatus=t11vfPortTaggingOperStatus, t11vfPortStorageType=t11vfPortStorageType, t11vfLocallyEnabledTable=t11vfLocallyEnabledTable, t11vfLocallyEnabledPortIfIndex=t11vfLocallyEnabledPortIfIndex, t11vfConformance=t11vfConformance, t11vfVirtualSwitchStorageType=t11vfVirtualSwitchStorageType, t11vfLocallyEnabledRowStatus=t11vfLocallyEnabledRowStatus, t11vfVirtualSwitchCoreSwitchName=t11vfVirtualSwitchCoreSwitchName, t11vfVirtualSwitchVfId=t11vfVirtualSwitchVfId, t11vfCoreSwitchTable=t11vfCoreSwitchTable, t11vfMIBCompliance=t11vfMIBCompliance, t11vfCoreSwitchSwitchName=t11vfCoreSwitchSwitchName, t11vfLocallyEnabledEntry=t11vfLocallyEnabledEntry, t11vfCoreSwitchEntry=t11vfCoreSwitchEntry, t11vfCoreSwitchMaxSupported=t11vfCoreSwitchMaxSupported, t11vfPortVfId=t11vfPortVfId, t11vfVirtualSwitchRowStatus=t11vfVirtualSwitchRowStatus)

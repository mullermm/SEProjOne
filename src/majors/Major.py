import sys
import ConLib

transcript = ['AlS105', 'AlS205', 'HIS236', 'RLN370','A15264', 'A15299', 'A15305', 'A15320', 'A15332',  'PHI230']

def american_indian_studies():
    section1 = ['AlS105', 'AlS205', 'HIS236', 'RLN370']
    section2 = ['A15264', 'ENL255']
    section3 = ['A15208', 'A15233', 'A15264', 'A15299', 'A15305', 'A15320', 'A15332', 'A15364', 'A15396', 'A15399', 'A15405', 'A15408', 'A15490', 'A15495', 'A15498', 'A15499', 'ART290', 'DAK111', 'DAK112', 'ENL255', 'ENL355', 'OJB111', 'OJB112']
    section4 = ['GST200', 'MAT163', 'MAT164', 'PHI230']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some_upper(4, 3, section3)
    major.do_some(1, section4)

def american_history():
    section1 = ['ART240', 'ART388', 'ART305','ART405']
    section2 = ['ART102', 'ART107']
    section3 = ['ART118', 'ART221']
    section4 = ['ART231', 'ART243', 'ART244', 'ART249', 'ART349', 'ART290', 'ART390','ART352', 'ART382', 'ART385', 'ART386', 'RART387', 'ART389', 'ART499']
    section5 = ['GST200', 'MAT111', 'MAT145', 'MAT146', 'MAT163', 'PHI230', 'PHY119']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(6, section4)
    major.do_some(1, section5)

def art_education():
    section1 = ['ART102', 'ART107', 'ART240','ART280', 'ART305','ART405']
    section2 = ['ART118', 'ART257']
    section3 = ['ART221', 'ART250']
    section4 = ['ART132','ART223']
    section5 = ['ART201','ART202']
    section6 = ['ART349', 'ART352', 'ART382', 'ART385', 'ART386', 'ART387', 'ART388', 'ART389', 'ART390']
    section7 = ['GST200', 'MAT111', 'MAT145', 'MAT146', 'MAT163', 'PHI230', 'PHY119']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)
    major.do_some(1, section5)
    major.do_some(2, section6)
    major.do_some(1, section7)

def graphic_design():
    section1 = ['ART107', 'ART133', 'ART201', 'ART202', 'ART240', 'ART315', 'ART324', 'ART326', 'ART424', 'ART425']
    section2 = ['ART105', 'ART221', 'ART250', 'ART280']
    section3 = ['ART349', 'ART352', 'ART385', 'ART386', 'ART387', 'ART388', 'ART389', 'ART390']
    section4 = ['GST200', 'MAT111', 'MAT145', 'MAT146', 'MAT163', 'PHI230', 'PHY119']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def studio_art():
    section1 = ['ART102', 'ART107', 'ART240', 'ART305','ART405']
    section2 = ['ART118', 'ART201', 'ART223', 'ART257']
    section3 = ['ART221', 'ART250', 'ART280']
    section4 = ['GST200', 'MAT111', 'MAT145', 'MAT146', 'MAT163', 'PHI230', 'PHY119']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def biology_bs():
    section1 = ['B10151', 'B10152', 'B10253', 'B10255']
    section2 = ['B10351', 'B10353', 'B10361', 'B10369', 'B10440', 'B10471', 'B10473', 'B10474', 'B10475', 'B10476', 'B10481', 'B10486', 'B10495', 'PHY317']
    section3 = ['BIO490','SCI490','HON490']
    section4 = ['PHY116', 'PHY107','PHY108','PHY121','PHY122']
    section5 = ['MAT114', 'MAT145', 'MAT163', 'MAT164', 'PSY215']
    section6 = ['COM115','COM111','HON130']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(5, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)
    major.do_some(1, section5)
    major.do_some(1, section6)

def biology_ba():
    section1 = ['B10151', 'B10152', 'B10253', 'B10255']
    section2 = ['B10351', 'B10353', 'B10361', 'B10369', 'B10440', 'B10471', 'B10473', 'B10474', 'B10475', 'B10476', 'B10481', 'B10486', 'B10495', 'PHY317']
    section3 = ['BIO490','SCI490','HON490']
    section4 = ['COM115','COM111','HON130']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(5, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def biopsychology():
    section1 = ['B10151', 'B10152', 'B10253', 'B10475', 'PSY105', 'PSY215', 'PSY315', 'PSY355']
    section2 = ['PSY253','PSY262','PSY299','PSY325','PSY360', 'PSY354', 'PSY391', 'PSY410', 'PSY491', 'PSYC322', 'PSYC407', 'PSYC378', 'PSYC486']
    section3 = ['B10255', 'B10369', 'B10471', 'B10473', 'B10474', 'B10495', 'PHY317', 'BIOL356']
    section4 = ['B10490', 'SC1490', 'PSY400']
    section5 = ['COM111','COM115','HON130']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(2, section2)
    major.do_some(2, section3)
    major.do_some(1, section4)
    major.do_some(1, section5)

def life_sciences():
    section1 = ['B10151', 'B10152', 'B10253', 'B10255']
    section2 = ['B10351', 'B10353', 'B10361', 'B10369', 'B10440', 'B10471', 'B10473', 'B10474', 'B10475', 'B10476', 'B10481', 'B10486', 'B10495', 'PHY317']
    section3 = ['B10490', 'SC1490', 'HON490', 'CHM115', 'CHM115', 'CHM115L','CHM116', 'CHM116L']
    section4 = ['PHY101', 'SC1106']
    section5 = ['MAT114', 'MAT145', 'MAT163', 'MAT164', 'PSY215']
    section6 = ['COM115', 'COM111', 'HON130']
    major = ConLib.Conlib(transcript)
    major.do_all(section1)
    major.do_some(4, section2)
    major.do_some(1, section3)
    major.do_some(2, section4)
    major.do_some(1, section5)
    major.do_some(1, section6)

def accounting():
    section1 = ['ACC221','ACC222','ACC322','ACC323','ACC324','ACC326','ACC423','ACC425', 'BUS301', 'BUS362', 'ECO112', 'ECO113', 'FIN331', 'MIS260', 'MIS379', 'MKT252']
    section2 = ['COM111','COM112','COM115','ENL240','ENL241','ENL250','ENL251','ENL255','ENL260','ENL270','ENL280','ENL290','ENL291', 'HIS102','HIS103','HIS282']
    section3 = ['MAT110', 'MAT111', 'MAT114', 'MAT145', 'MAT146', 'MAT171', 'MAT173', 'MAT273']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)

def managment():
    section1 = ['ACC221', 'ACC222', 'BUS242', 'BUS301', 'BUS340', 'BUS362', 'BUS440', 'BUS465', 'ECO112', 'ECO113', 'FIN331', 'MIS260', 'MKT252']
    section2 = ['MIS264','MIS379']
    section3 = ['MIS376','ECO318']
    section4 = ['COM111', 'COM112', 'COM115', 'ENL240', 'ENL241', 'ENL250', 'ENL251', 'ENL255', 'ENL260', 'ENL270', 'ENL280', 'ENL290', 'ENL291', 'HIS102', 'HIS103', 'HIS282']
    section5 = ['MAT110', 'MAT111', 'MAT114', 'MAT145', 'MAT146', 'MAT171', 'MAT173', 'MAT273']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)
    major.do_some(1, section5)

def international_business():
    section1 = ['ACC221', 'ACC222', 'BUS242', 'BUS301', 'BUS362', 'BUS465', 'ECO112', 'ECO113', 'ECO360', 'FIN331', 'MIS260', 'MIS264', 'MKT252', 'MKT466']
    section2 = ['FRE211', 'GER211', 'SPA211']
    section3 = ['COM111', 'COM112', 'COM115', 'ENL240', 'ENL241', 'ENL250', 'ENL251', 'ENL255', 'ENL260', 'ENL270', 'ENL280', 'ENL290', 'ENL291', 'HIS102', 'HIS103', 'HIS282']
    section4 = ['MAT110', 'MAT111', 'MAT114', 'MAT145', 'MAT146', 'MAT171', 'MAT173', 'MAT273']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def finance():
    section1 = ['ACC221 ', 'ACC222 ', 'ACC322 ', 'BUS242 ', 'BUS301 ', 'BUS362 ', 'ECO112 ', 'ECO113 ', 'ECO315 ', 'FIN331 ', 'FIN433 ', 'FIN438 ', 'FlN460', 'MIS260 ', 'MIS379 ', 'MKT252']
    section2 = ['COM111', 'COM112', 'COM115', 'ENL240', 'ENL241', 'ENL250', 'ENL251', 'ENL255', 'ENL260', 'ENL270', 'ENL280', 'ENL290', 'ENL291', 'HIS102', 'HIS103', 'HIS282']
    section3 = ['MAT110', 'MAT111', 'MAT114', 'MAT145', 'MAT146', 'MAT171', 'MAT173', 'MAT273']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)

def music_business():
    section1 = ['ACC221', 'ACC222', 'BUS242', 'ECO112', 'ECO113', 'FIN331', 'MIS260', 'MKT252', 'MUS205', 'MUS335', 'MUS336', 'MUS162', 'MUS408']
    section2 = ['BUS399', 'MUS399']
    section3 = ['MUS113', 'MUS114', 'MUS130', 'MUS220', 'MUS241']
    section4 = ['MIS264', 'MIS379']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(3, section3)
    major.do_some(1, section4)

def managment_information_systems():
    section1 = ['ACC221', 'ACC222', 'BUS242', 'BUS301', 'BUS362', 'CSC160', 'ECO112', 'ECO113', 'FIN331', 'MAT171', 'MIS260', 'MIS270', 'MIS375', 'MIS376', 'MIS475', 'MIS476', 'MKT252']
    section2 = ['MIS264', 'MIS379']
    section3 = ['CSC170', 'CSC240']
    section4 = ['COM111', 'COM112', 'COM115', 'ENL240', 'ENL241', 'ENL250', 'ENL251', 'ENL255', 'ENL260', 'ENL270', 'ENL280', 'ENL290', 'ENL291', 'HIS102', 'HIS103', 'HIS282']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def marketing():
    section1 = ['ACC221', 'ACC222', 'BUS242', 'BUS301', 'BUS362', 'ECO112', 'ECO113', 'FIN331', 'MIS260', 'MIS264', 'MKT252', 'MKT352', 'MKT450', 'MKT466']
    section2 = ['MKT350', 'MKT354']
    section3 = ['MKT355', 'MKT357']
    section4 = ['COM111', 'COM112', 'COM115', 'ENL240', 'ENL241', 'ENL250', 'ENL251', 'ENL255', 'ENL260', 'ENL270', 'ENL280', 'ENL290', 'ENL291', 'HIS102', 'HIS103', 'HIS282']
    section5 = ['MAT110', 'MAT111', 'MAT114', 'MAT145', 'MAT146', 'MAT171', 'MAT173', 'MAT273']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)
    major.do_some(1, section5)

def cross_cultural_studies():
    section1 = ['CCS100', 'CCS399', 'KEY480']
    section2 = ['GST200', 'HIS369', 'MAT111', 'MAT145', 'MAT146', 'MAT163', 'MAT164', 'PHI230', 'PHY119', 'P0L483']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)

def communication_studies():
    section1 = ['COM111', 'COM120', 'COM280', 'COM281', 'COM329', 'COM351', 'COM352', 'COM490']
    section2 = ['COM254', 'COM355']
    section3 = ['COM243', 'COM247', 'COM260', 'COM299', 'COM321', 'COM345', 'COM399', 'COM405', 'COM415', 'COM480', 'COM495', 'COM499', 'ART132', 'ART201', 'ART215', 'BUS242', 'ENL227', 'ENL228', 'FLM399', 'MKT252']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(3, section4)

def chemistry_non_acs():
    section1 = ['CHM115', 'CHM116', 'CHM251', 'CHM252', 'CHM280', 'SCI490']
    section2 = ['CHM362', 'CHM368']
    section3 = ['CHM370', 'B10369']
    section4 = ['CHM430', 'CHM440', 'CHM450']
    section5 = ['CHM362', 'CHM368', 'CHM464', 'CHM481', 'CHM482', 'CHM494', 'CHM495', 'CHM498', 'PHY317']
    section6 = ['CHM491', 'CHM491', 'CHM491', 'CHM491', 'MAT145', 'MAT146', 'PHY121', 'PHY122']
    section7 = ['COM111' , 'COM115', 'HON130']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(2, section4)
    major.do_some(3, section5)
    major.do_some(4, section6)
    major.do_some(1, section7)

def chemistry():
    section1 = ['CHM115', 'CHM116', 'CHM251', 'CHM252', 'CHM280', 'SCI490']
    section2 = ['CHM362', 'CHM368']
    section3 = ['CHM370', 'B10369']
    section4 = ['CHM430', 'CHM440', 'CHM450']
    section5 = ['CHM362', 'CHM368', 'CHM464', 'CHM481', 'CHM482', 'CHM494', 'CHM495', 'CHM498', 'PHY317']
    section6 = ['CHM491', 'CHM491', 'CHM491', 'CHM491', 'MAT145', 'MAT146', 'PHY121', 'PHY122']
    section7 = ['COM111' , 'COM115', 'HON130']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(2, section4)
    major.do_some(3, section5)
    major.do_some(4, section6)
    major.do_some(1, section7)

def chemistry_acs():
    section1 = ['CHM115', 'CHM116', 'CHM251', 'CHM252', 'CHM280', 'CHM362', 'CHM368', 'CHM430', 'CHM440', 'CHM450', 'CHM464', 'CHM481', 'CHM482', 'SCI490']
    section2 = ['CHM370', 'BI0369']
    section3 = ['CHM494', 'CHM495', 'CHM498 ', 'PHY317']
    section4 = ['CHM491', 'CHM491', 'CHM491', 'CHM491', 'MAT145', 'MAT146', 'MAT245', 'PHY121', 'PHY122']
    section5 = ['COM115', 'COM111', 'HON130']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_all(section4)
    major.do_some(1, section5)    

def computational_economics():
    section1 = ['CSC160', 'CSC170', 'CSC210', 'CSC345', 'ECO112', 'ECO113', 'ECO312', 'ECO313', 'ECO315', 'ECO318', 'MAT145']
    section2 = ['CSC240', 'CSC320', 'CSC352']
    section3 = ['CSC499', 'EC0499']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)

def computer_science_bs():
    section1 = ['CSC160', 'CSC170', 'CSC210', 'CSC240', 'CSC320', 'CSC345', 'CSC385', 'CSC450', 'CSC451', 'MAT145', 'MAT271']
    section2 = ['MAT146', 'MAT245', 'MAT246', 'MAT304', 'MAT355', 'MAT363', 'MAT369']
    section3 = ['CSC250', 'CSC272', 'CSC310', 'CSC352', 'CSC353', 'CSC373', 'CSC395', 'CSC399', 'CSC431', 'CSC457', 'CSC495', 'CSC499', 'MAT355', 'MIS475', 'PHY261']
    section4 = ['COM115', 'COM111', 'MAT201']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(2, section2)
    major.do_some(3, section3)
    major.do_some(1, section4)

def computer_science_ba():
    section1 = ['CSC160', 'CSC170', 'CSC210', 'CSC240', 'CSC320', 'CSC345', 'CSC385', 'CSC450', 'CSC451', 'MAT114']
    section2 = ['MAT171', 'MAT271']
    section3 = ['CSC250', 'CSC272', 'CSC310', 'CSC352', 'CSC353', 'CSC373', 'CSC395', 'CSC399', 'CSC431', 'CSC457', 'CSC495', 'CSC499', 'MAT355', 'MIS475', 'PHY261']
    section4 = ['COM115', 'COM111', 'MAT201']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(2, section3)
    major.do_some(1, section4)

def computational_philosophy():
    section1 = ['CSC160 ', 'CSC170 ', 'CSC210 ', 'CSC320 ', 'CSC373 ', 'CSC385 ', 'MAT114 ', 'PHI241', 'PHI242', 'PHI343', 'PHI344 ', 'PHI365']
    section2 = ['MAT171', 'MAT271']
    section3 = ['CSC495', 'PHI410']
    section4 = ['PHI315', 'PHI350', 'PHI370', 'PHI380', 'PHI499']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def applied_economics():
    section1 = ['ECO112', 'ECO113', 'ECO313', 'ECO318', 'ECO350', 'ECO360', 'EC0490', 'ENL223']
    section2 = ['ECO312', 'ECO315']
    section3 = ['MAT163', 'MAT164', 'MIS379']
    section4 = ['ECO399', 'EC0499']
    section5 = ['PHI120', 'PHI125']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)
    major.do_some(1, section5)

def mathematical_economics():
    section1 = ['ECO112', 'ECO113', 'ECO312', 'ECO313', 'EC0416', 'EC0490', 'MAT145', 'MAT146', 'MAT245', 'MAT246', 'MAT373', 'MAT374']
    section2 = ['ECO315', 'ECO318', 'ECO350', 'ECO360', 'ECO365', 'ECO370', 'ECO399', 'EC0495', 'EC0499']
    section3 = ['MAT324', 'MAT369', 'MAT377']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some_upper(2, 2, section2)
    major.do_some(1, section3)

def economics():
    section1 = ['ECO112', 'ECO113', 'ECO312', 'ECO313', 'EC0490']
    section2 = ['ECO315', 'ECO318', 'ECO350', 'ECO360', 'ECO365', 'ECO370', 'ECO399', 'EC0416', 'EC0495', 'EC0499']
    section3 = ['MAT163', 'MAT164', 'MIS379']
    section4 = ['MAT114', 'MAT145', 'MAT146']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some_upper(3, 3, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def business_economics():
    section1 = ['ECO112', 'ECO113', 'ECO312', 'ECO313', 'ACC221', 'ACC222', 'BUS242', 'MKT252']
    section2 = ['FIN331', 'MIS379']
    section3 = ['ECO315', 'ECO318', 'ECO350', 'ECO360', 'ECO365', 'ECO370', 'ECO399', 'EC0416', 'EC0490', 'EC0495', 'EC0499']
    section4 = ['ECO318', 'EC0490', 'MIS379']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def elementary_education_general_science():
    section1 = ['EDC200', 'EDC220', 'EDC310', 'EDC410', 'EDC490', 'EED225', 'EED311', 'EED312', 'EED325', 'EED326', 'EED336', 'EED341', 'EED342', 'EED350', 'EED360', 'EED370', 'EED380', 'EED386']
    section2 = ['EDC206', 'EDC210']
    section3 = ['EDC481', 'EED489','ENL111', 'HPE115', 'MAT137', 'MAT138']
    section4 = ['B10102', 'B10121', 'CHM115', 'CHM116', 'PHY116', 'SC1106', 'ESE300', 'ESE341']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_all(section3)
    major.do_all(section4)

def elementary_education_comm_arts():
    section1 = ['EDC200', 'EDC220', 'EDC310', 'EDC410', 'EDC490', 'EED225', 'EED311', 'EED312', 'EED325', 'EED326', 'EED336', 'EED341', 'EED342', 'EED350', 'EED360', 'EED370', 'EED380', 'EED386']
    section2 = ['EDC206', 'EDC210']
    section3 = ['EDC481', 'EED489','ENL111', 'HPE115', 'MAT137', 'MAT138']
    section4 = ['PHY203', 'EED200']
    section5 = ['B10102', 'ENV120']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_all(section3)
    major.do_some(1, section4)
    major.do_some(1, section5)

def elementary_education_social_studies():
    section1 = ['EDC200', 'EDC220', 'EDC310', 'EDC410', 'EDC490', 'EED225', 'EED311', 'EED312', 'EED325', 'EED326', 'EED336', 'EED341', 'EED342', 'EED350', 'EED360', 'EED370', 'EED380', 'EED386']
    section2 = ['EDC206', 'EDC210']
    section3 = ['EDC481', 'EED489','ENL111', 'HPE115', 'MAT137', 'MAT138']
    section4 = ['PHY203', 'EED200']
    section5 = ['B10102', 'ENV120']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_all(section3)
    major.do_some(1, section4)
    major.do_some(1, section5)

def elementary_education_math():
    section1 = ['EDC200', 'EDC220', 'EDC310', 'EDC410', 'EDC490', 'EED225', 'EED311', 'EED312', 'EED325', 'EED326', 'EED336', 'EED341', 'EED342', 'EED350', 'EED360', 'EED370', 'EED380', 'EED386']
    section2 = ['EDC206', 'EDC210']
    section3 = ['EDC481', 'EED489','ENL111', 'HPE115', 'MAT137', 'MAT138']
    section4 = ['PHY203', 'EED200']
    section5 = ['B10102', 'ENV120']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_all(section3)
    major.do_some(1, section4)
    major.do_some(1, section5)

def elementary_education():
    section1 = ['EDC200', 'EDC220', 'EDC310', 'EDC410', 'EDC490', 'EED225', 'EED311', 'EED312', 'EED325', 'EED326', 'EED336', 'EED341', 'EED342', 'EED350', 'EED360', 'EED370', 'EED380', 'EED386']
    section2 = ['EDC206', 'EDC210']
    section3 = ['EDC481', 'EED489','ENL111', 'HPE115', 'MAT137', 'MAT138']
    section4 = ['PHY203', 'EED200']
    section5 = ['B10102', 'ENV120']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_all(section3)
    major.do_some(1, section4)
    major.do_some(1, section5)

def english_literature():
    section1 = ['ENL220', 'ENL221']
    section2 = ['ENL240', 'ENL242', 'ENL250', 'ENL251', 'ENL255', 'ENL260', 'ENL270', 'ENL280', 'ENL290']
    section3 = ['ENL330', 'ENL332', 'ENL333', 'ENL334', 'ENL336', 'ENL337', 'ENL338', 'ENL339']
    section4 = ['ENL350', 'ENL351', 'ENL352', 'ENL353', 'ENL354', 'ENL355', 'ENL358']
    section5 = ['ENL360', 'ENL361', 'ENL362', 'ENL365', 'ENL367', 'ENL368']
    section6 = ['ENL410', 'ENL430']
    section7 = ['GST200', 'HIS369', 'MAT111', 'MAT145', 'MAT146', 'MAT163', 'MAT164', 'PH 123', 'PHY119', 'P0L483']
    major = ConLib.ConLib(transcript)
    major.do_some(1, section1)
    major.do_some(2, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)
    major.do_some(1, section5)
    major.do_some(1, section6)
    major.do_all(section7)

def english_creative_writing():
    section1 = ['ENL226', 'ENL420']
    section2 = ['ENL220', 'ENL221']
    section3 = ['ENL320', 'ENL321', 'ENL322', 'ENL323']
    section4 = ['ENL227', 'ENL228', 'ENL229', 'ENL320', 'ENL322', 'ENL324', 'ENL325', 'ENL396', 'ENL397', 'ENL399']
    section5 = ['ART201', 'ART215']
    section6 = ['GST200', 'HIS369', 'MAT111', 'MAT145', 'MAT146', 'MAT163', 'MAT164', 'PHI230', 'PHY119', 'P0L483']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)
    major.do_some(1, section5)
    major.do_all(section6)

def english_commication_arts():
    section1 = ['ENL220', 'ENL240', 'ENL365', 'ENL380', 'ENL396', 'COM111', 'C0M254', 'COM351', 'ESE350', 'ESE351']
    section2 = ['COM120', 'C0M243', 'P0L342']
    section3 = ['ENL330', 'ENL332', 'ENL333', 'ENL334', 'ENL336', 'ENL337', 'ENL338', 'ENL339']
    section4 = ['ENL350', 'ENL351', 'ENL352', 'ENL353', 'ENL354', 'ENL355', 'ENL358']
    section5 = ['ENL360', 'ENL361', 'ENL362', 'ENL365', 'ENL367', 'ENL368']
    section6 = ['GST200', 'HIS369', 'MAT111', 'MAT145', 'MAT146', 'MAT163', 'MAT164', 'PHI230', 'PHY119', 'P0L483']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)
    major.do_some(1, section5)
    major.do_all(section6)

def enviormental_studies():
    section1 = ['BI0151', 'BI0152', 'BI0481', 'CHM115', 'CHM116', 'ECO365', 'ENV100', 'ENV120', 'HIS316', 'SWK210']
    section2 = ['ENV310', 'P0L241', 'P0L325', 'SOC381']
    section3 = ['C0M260', 'RLN333', 'WST313']
    section4 = ['ENV490', 'ENV492']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def enviormental_studies_HECUA():
    section1 = ['B10151', 'B10152', 'B10481', 'CHM115', 'CHM116', 'ENV100', 'HIS316', 'INS345', 'INS346', 'INS399', 'INS399', 'SWK210']
    section2 = ['C0M260', 'RLN333', 'WST313']
    section3 = ['ENV490', 'ENV492']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)

def secondary_education():
    section1 = ['EDC200', 'EDC220', 'EDC310', 'EDC410', 'EDC490', 'ESE300', 'ESE325']
    section2 = ['EDC206', 'EDC210']
    section3 = ['ESE489', 'EDC481', 'ENL111', 'HPE115']
    section4 = ['ESE310', 'ESE330', 'ESE340', 'ESE350', 'ESE351', 'ESE360', 'ESE370', 'HPE365', 'HPE368', 'HPE390']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def english_second_language():
    section1 = ['EDC200', 'EDC220', 'EDC310', 'EDC410', 'EED325', 'EED326', 'ESE325', 'ESL310', 'ESL320', 'ESL330', 'ESL340', 'ESL410', 'ESL420', 'ESL490']
    section2 = ['EDC206', 'EDC210']
    section3 = ['EDC483', 'ESL489', 'ENL111', 'HPE115']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)

def social_studies():
    section1 = ['ANT141', 'ECO113', 'ESE220', 'POL121', 'PSY105', 'SOC121']
    section2 = ['HIS120', 'HIS121', 'HIS122']
    section3 = ['EDC200', 'EDC220', 'EDC310', 'EDC410', 'EDC490', 'ESE300', 'ESE310', 'ESE325']
    section4 = ['EDC206', 'EDC210']
    section5 = ['EDC481', 'ESE489', 'ENL111', 'HPE115']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_all(section3)
    major.do_some(1, section4)
    major.do_all(section5)

def ():
    section1 = ['']
    section2 = ['']
    section3 = ['']
    section4 = ['']
    section5 = ['']
    section6 = ['']
    section7 = ['']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def ():
    section1 = ['']
    section2 = ['']
    section3 = ['']
    section4 = ['']
    section5 = ['']
    section6 = ['']
    section7 = ['']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def ():
    section1 = ['']
    section2 = ['']
    section3 = ['']
    section4 = ['']
    section5 = ['']
    section6 = ['']
    section7 = ['']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def ():
    section1 = ['']
    section2 = ['']
    section3 = ['']
    section4 = ['']
    section5 = ['']
    section6 = ['']
    section7 = ['']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def ():
    section1 = ['']
    section2 = ['']
    section3 = ['']
    section4 = ['']
    section5 = ['']
    section6 = ['']
    section7 = ['']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def ():
    section1 = ['']
    section2 = ['']
    section3 = ['']
    section4 = ['']
    section5 = ['']
    section6 = ['']
    section7 = ['']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def ():
    section1 = ['']
    section2 = ['']
    section3 = ['']
    section4 = ['']
    section5 = ['']
    section6 = ['']
    section7 = ['']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def ():
    section1 = ['']
    section2 = ['']
    section3 = ['']
    section4 = ['']
    section5 = ['']
    section6 = ['']
    section7 = ['']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def ():
    section1 = ['']
    section2 = ['']
    section3 = ['']
    section4 = ['']
    section5 = ['']
    section6 = ['']
    section7 = ['']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def ():
    section1 = ['']
    section2 = ['']
    section3 = ['']
    section4 = ['']
    section5 = ['']
    section6 = ['']
    section7 = ['']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def ():
    section1 = ['']
    section2 = ['']
    section3 = ['']
    section4 = ['']
    section5 = ['']
    section6 = ['']
    section7 = ['']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def ():
    section1 = ['']
    section2 = ['']
    section3 = ['']
    section4 = ['']
    section5 = ['']
    section6 = ['']
    section7 = ['']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def ():
    section1 = ['']
    section2 = ['']
    section3 = ['']
    section4 = ['']
    section5 = ['']
    section6 = ['']
    section7 = ['']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def ():
    section1 = ['']
    section2 = ['']
    section3 = ['']
    section4 = ['']
    section5 = ['']
    section6 = ['']
    section7 = ['']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def ():
    section1 = ['']
    section2 = ['']
    section3 = ['']
    section4 = ['']
    section5 = ['']
    section6 = ['']
    section7 = ['']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def ():
    section1 = ['']
    section2 = ['']
    section3 = ['']
    section4 = ['']
    section5 = ['']
    section6 = ['']
    section7 = ['']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def ():
    section1 = ['']
    section2 = ['']
    section3 = ['']
    section4 = ['']
    section5 = ['']
    section6 = ['']
    section7 = ['']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def ():
    section1 = ['']
    section2 = ['']
    section3 = ['']
    section4 = ['']
    section5 = ['']
    section6 = ['']
    section7 = ['']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def ():
    section1 = ['']
    section2 = ['']
    section3 = ['']
    section4 = ['']
    section5 = ['']
    section6 = ['']
    section7 = ['']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def ():
    section1 = ['']
    section2 = ['']
    section3 = ['']
    section4 = ['']
    section5 = ['']
    section6 = ['']
    section7 = ['']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def ():
    section1 = ['']
    section2 = ['']
    section3 = ['']
    section4 = ['']
    section5 = ['']
    section6 = ['']
    section7 = ['']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def ():
    section1 = ['']
    section2 = ['']
    section3 = ['']
    section4 = ['']
    section5 = ['']
    section6 = ['']
    section7 = ['']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def ():
    section1 = ['']
    section2 = ['']
    section3 = ['']
    section4 = ['']
    section5 = ['']
    section6 = ['']
    section7 = ['']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def ():
    section1 = ['']
    section2 = ['']
    section3 = ['']
    section4 = ['']
    section5 = ['']
    section6 = ['']
    section7 = ['']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def ():
    section1 = ['']
    section2 = ['']
    section3 = ['']
    section4 = ['']
    section5 = ['']
    section6 = ['']
    section7 = ['']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def ():
    section1 = ['']
    section2 = ['']
    section3 = ['']
    section4 = ['']
    section5 = ['']
    section6 = ['']
    section7 = ['']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)

def ():
    section1 = ['']
    section2 = ['']
    section3 = ['']
    section4 = ['']
    section5 = ['']
    section6 = ['']
    section7 = ['']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)


functions = {
    0 : american_indian_studies,
    1 : american_history,
    2 : art_education,
    3 : graphic_design,

}

def main():

    functions[1]()
if __name__ == "__main__":
    main()
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
    return major.completion_percent()

def art_history():
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
    return major.completion_percent()

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
    return major.completion_percent()

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
    return major.completion_percent()

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
    return major.completion_percent()

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
    return major.completion_percent()

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
    return major.completion_percent()

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
    return major.completion_percent()

def life_sciences():
    section1 = ['B10151', 'B10152', 'B10253', 'B10255']
    section2 = ['B10351', 'B10353', 'B10361', 'B10369', 'B10440', 'B10471', 'B10473', 'B10474', 'B10475', 'B10476', 'B10481', 'B10486', 'B10495', 'PHY317']
    section3 = ['B10490', 'SC1490', 'HON490', 'CHM115', 'CHM115', 'CHM115L','CHM116', 'CHM116L']
    section4 = ['PHY101', 'SC1106']
    section5 = ['MAT114', 'MAT145', 'MAT163', 'MAT164', 'PSY215']
    section6 = ['COM115', 'COM111', 'HON130']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(4, section2)
    major.do_some(1, section3)
    major.do_some(2, section4)
    major.do_some(1, section5)
    major.do_some(1, section6)
    return major.completion_percent()

def accounting():
    section1 = ['ACC221','ACC222','ACC322','ACC323','ACC324','ACC326','ACC423','ACC425', 'BUS301', 'BUS362', 'ECO112', 'ECO113', 'FIN331', 'MIS260', 'MIS379', 'MKT252']
    section2 = ['COM111','COM112','COM115','ENL240','ENL241','ENL250','ENL251','ENL255','ENL260','ENL270','ENL280','ENL290','ENL291', 'HIS102','HIS103','HIS282']
    section3 = ['MAT110', 'MAT111', 'MAT114', 'MAT145', 'MAT146', 'MAT171', 'MAT173', 'MAT273']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    return major.completion_percent()

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
    return major.completion_percent()

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
    return major.completion_percent()

def finance():
    section1 = ['ACC221 ', 'ACC222 ', 'ACC322 ', 'BUS242 ', 'BUS301 ', 'BUS362 ', 'ECO112 ', 'ECO113 ', 'ECO315 ', 'FIN331 ', 'FIN433 ', 'FIN438 ', 'FlN460', 'MIS260 ', 'MIS379 ', 'MKT252']
    section2 = ['COM111', 'COM112', 'COM115', 'ENL240', 'ENL241', 'ENL250', 'ENL251', 'ENL255', 'ENL260', 'ENL270', 'ENL280', 'ENL290', 'ENL291', 'HIS102', 'HIS103', 'HIS282']
    section3 = ['MAT110', 'MAT111', 'MAT114', 'MAT145', 'MAT146', 'MAT171', 'MAT173', 'MAT273']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    return major.completion_percent()

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
    return major.completion_percent()

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
    return major.completion_percent()

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
    return major.completion_percent()

def cross_cultural_studies():
    section1 = ['CCS100', 'CCS399', 'KEY480']
    section2 = ['GST200', 'HIS369', 'MAT111', 'MAT145', 'MAT146', 'MAT163', 'MAT164', 'PHI230', 'PHY119', 'P0L483']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    return major.completion_percent()

def communication_studies():
    section1 = ['COM111', 'COM120', 'COM280', 'COM281', 'COM329', 'COM351', 'COM352', 'COM490']
    section2 = ['COM254', 'COM355']
    section3 = ['COM243', 'COM247', 'COM260', 'COM299', 'COM321', 'COM345', 'COM399', 'COM405', 'COM415', 'COM480', 'COM495', 'COM499', 'ART132', 'ART201', 'ART215', 'BUS242', 'ENL227', 'ENL228', 'FLM399', 'MKT252']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    return major.completion_percent()

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
    return major.completion_percent()

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
    return major.completion_percent()

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
    return major.completion_percent()    

def computational_economics():
    section1 = ['CSC160', 'CSC170', 'CSC210', 'CSC345', 'ECO112', 'ECO113', 'ECO312', 'ECO313', 'ECO315', 'ECO318', 'MAT145']
    section2 = ['CSC240', 'CSC320', 'CSC352']
    section3 = ['CSC499', 'EC0499']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    return major.completion_percent()

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
    return major.completion_percent()

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
    return major.completion_percent()

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
    return major.completion_percent()

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
    return major.completion_percent()

def mathematical_economics():
    section1 = ['ECO112', 'ECO113', 'ECO312', 'ECO313', 'EC0416', 'EC0490', 'MAT145', 'MAT146', 'MAT245', 'MAT246', 'MAT373', 'MAT374']
    section2 = ['ECO315', 'ECO318', 'ECO350', 'ECO360', 'ECO365', 'ECO370', 'ECO399', 'EC0495', 'EC0499']
    section3 = ['MAT324', 'MAT369', 'MAT377']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some_upper(2, 2, section2)
    major.do_some(1, section3)
    return major.completion_percent()

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
    return major.completion_percent()

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
    return major.completion_percent()

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
    return major.completion_percent()

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
    return major.completion_percent()

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
    return major.completion_percent()

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
    return major.completion_percent()

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
    return major.completion_percent()

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
    return major.completion_percent()

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
    return major.completion_percent()

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
    return major.completion_percent()

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
    return major.completion_percent()

def enviormental_studies_HECUA():
    section1 = ['B10151', 'B10152', 'B10481', 'CHM115', 'CHM116', 'ENV100', 'HIS316', 'INS345', 'INS346', 'INS399', 'INS399', 'SWK210']
    section2 = ['C0M260', 'RLN333', 'WST313']
    section3 = ['ENV490', 'ENV492']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    return major.completion_percent()

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
    return major.completion_percent()

def english_second_language():
    section1 = ['EDC200', 'EDC220', 'EDC310', 'EDC410', 'EED325', 'EED326', 'ESE325', 'ESL310', 'ESL320', 'ESL330', 'ESL340', 'ESL410', 'ESL420', 'ESL490']
    section2 = ['EDC206', 'EDC210']
    section3 = ['EDC483', 'ESL489', 'ENL111', 'HPE115']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    return major.completion_percent()

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
    return major.completion_percent()

def film_production():
    section1 = ['FLM180', 'FLM216', 'FLM260', 'FLM420', 'FLM490', 'COM247', 'ENL241', 'ENL371']
    section2 = ['THR232', 'THR233', 'FLM372']
    section3 = ['ART132', 'ART215', 'ART315', 'ART340', 'COM243', 'ENL228', 'ENL229', 'FLM124', 'FLM240', 'FLM312', 'FLM348', 'FLM399', 'FLM495', 'FLM499', 'MUS130', 'PHY119', 'THR328']
    section4 = ['MAT163', 'MAT164', 'PHY119']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(3, section3)
    major.do_all(section4)
    return major.completion_percent()

def theory_culture():
    section1 = ['FLM180', 'FLM216', 'FLM260', 'FLM420', 'FLM490', 'COM247', 'ENL241', 'ENL371']
    section2 = ['THR232', 'THR233']
    section3 = ['A15264', 'A15364', 'A15208', 'ART240', 'ENL221', 'ENL228', 'ENL229', 'ENL240', 'ENL430', 'FLM124', 'FLM399', 'FLM495', 'FLM499', 'PHI120', 'PHY119', 'RLN319', 'SPA248']
    section4 = ['MAT163', 'MAT164', 'PHY119']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(3, section3)
    major.do_all(section4)
    return major.completion_percent()

def history():
    section1 = ['HIS280', 'HIS480']
    section2 = ['HIS101', 'HIS102', 'HIS360', 'HIS361', 'HIS369', 'HIS370', 'HIS374', 'HIS378', 'HUM120']
    section3 = ['HIS102, 103, 282, 348, 352, or 354']
    section4 = ['HIS120', 'HIS121', 'HIS122', 'HIS225', 'HIS234', 'HIS236', 'HIS241', 'HIS242', 'HIS243', 'HIS249', 'HIS349', 'HIS300', 'HIS316', 'HIS331', 'HIS332', 'HIS335', 'HIS336', 'HIS338', 'HIS343']
    section5 = ['HIS104', 'HIS140', 'HIS440', 'HIS150','HIS350', 'HIS155','HIS355', 'HIS162', 'HIS462', 'HIS323', 'HIS327', 'HIS346', 'HIS357', 'HIS474']
    section6 = ['HIS369', 'GST200', 'MAT111', 'MAT145', 'MAT146', 'MAT163', 'PHI230']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)
    major.do_some(1, section5)
    major.do_some(1, section6)
    return major.completion_percent()

def german():
    section1 = ['CCS100', 'KEY480']
    section2 = ['GER351', 'GER354', 'GER295', 'GER495']
    section3 = ['GST200', 'HIS369', 'MAT111', 'MAT145', 'MAT146', 'MAT163', 'MAT164', 'PHI230', 'PHY119', 'P0L483']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    return major.completion_percent()

def french():
    section1 = ['CCS100', 'KEY480']
    section2 = ['FRE351', 'FRE353', 'FRE295', 'FRE495']
    section3 = ['GST200', 'HIS369', 'MAT111', 'MAT145', 'MAT146', 'MAT163', 'MAT164', 'PHI230', 'PHY119', 'P0L483']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    return major.completion_percent()

def medieval_studies():
    section1 = ['HUM120', 'HIS369', 'HIS370', 'LAT101', 'LAT102', 'HUM490']
    section2 = ['ENL330', 'ENL332', 'ENL360', 'ENL361', 'SPA352']
    section3 = ['HIS378', 'PHI242', 'RLN342']
    section4 = ['ART386', 'ART387', 'MUS231', 'THR361']
    section5 = ['HIS374', 'HIS440', 'POL380', 'SPA331']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)
    major.do_some(2, section5)
    return major.completion_percent()

def mathematics_teaching():
    section1 = ['MAT145', 'MAT146', 'MAT245', 'MAT246', 'MAT252', 'MAT271', 'MAT287', 'MAT314', 'MAT324', 'ESE330']
    section2 = ['MAT163', 'MAT164', 'MAT373']
    section3 = ['MAT355', 'MAT369', 'MAT374', 'MAT377']
    section4 = ['MAT491']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)
    return major.completion_percent()

def mathematics_bs():
    section1 = ['MAT145', 'MAT146', 'MAT245', 'MAT246', 'MAT271']
    section2 = ['MAT304', 'MAT314', 'MAT324']
    section3 = ['MAT163', 'MAT164', 'MAT373', 'MAT394', 'MIS379', 'PSY215', 'S0C362']
    section4 = ['MAT355', 'MAT369', 'MAT374', 'MAT377']
    section5 = ['MAT491']
    section6 = ['MAT201', 'COM111', 'COM115']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)
    major.do_all(section5)
    major.do_some(1, section6)
    return major.completion_percent()

def mathematics_ba():
    section1 = ['MAT145', 'MAT146', 'MAT245', 'MAT246', 'MAT271']
    section2 = ['MAT304', 'MAT314', 'MAT324']
    section3 = ['MAT252', 'MAT273', 'MAT287', 'MAT304', 'MAT314', 'MAT324', 'MAT355', 'MAT363', 'MAT369', 'MAT373', 'MAT374', 'MAT377', 'MAT394', 'MAT395', 'MAT399', 'MAT499', 'EC0416', 'PHY327']
    section4 = ['MAT491']
    section5 = ['MAT201', 'COM111', 'COM115']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(3, section3)
    major.do_all(section4)
    major.do_some(1, section5)
    return major.completion_percent()

def music_business():
    section1 = ['ACC221', 'ECO113', 'MIS260', 'MUS113', 'MUS114', 'MUS162', 'MUS205', 'MUS213', 'MUS214', 'MUS231', 'MUS232', 'MUS335', 'MUS336', 'BUS339', 'MUS399', 'MUS408', 'MUS458']
    section2 = ['MUS331', 'MUS332', 'MUS333', 'MUS334']
    section3 = ['BUS200', 'BUS242', 'BUS254']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    return major.completion_percent()

def music():
    section1 = ['MUS113', 'MUS114', 'MUS213', 'MUS214', 'MUS231', 'MUS232', 'MUS341', 'MUS458']
    section2 = ['MUS331', 'MUS332', 'MUS333', 'MUS334']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    return major.completion_percent()

def music_therapy():
    section1 = ['MUS113', 'MUS114', 'MUS135', 'MUS136', 'MUS152', 'MUS158', 'MUS213', 'MUS214', 'MUS231', 'MUS232', 'MUS237', 'MUS238', 'MUS258', 'MUS271', 'MUS273', 'MUS315', 'MUS340', 'MUS345', 'MUS374', 'MUS375', 'MUS376', 'MUS385', 'MUS458', 'MUS474', 'MUS475', 'MUS480', 'MUS481', 'B10103', 'PSY105', 'PSY203', 'PSY215', 'PSY262']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    return major.completion_percent()

def music_performance():
    section1 = ['MUS113', 'MUS114', 'MUS213', 'MUS214', 'MUS231', 'MUS232', 'MUS358', 'MUS459']
    section2 = ['MUS331', 'MUS332', 'MUS333', 'MUS334']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    return major.completion_percent()

def music_education():
    section1 = ['MUS113', 'MUS114', 'MUS213', 'MUS214', 'MUS220', 'MUS231', 'MUS232', 'MUS303', 'MUS311', 'MUS341', 'MUS352', 'MUS353', 'MUS355', 'MUS356', 'MUS357', 'MUS358', 'MUS359', 'MUS459', 'HPE115', 'EDC200', 'EDC310', 'ESE300']
    section2 = ['EDC206', 'EDC210']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    return major.completion_percent()

def new_media_game_design():
    section1 = ['NMS220', 'NMS242', 'ENL242', 'C0M415', 'P0L371', 'NMS490', 'CSC240', 'CSC250']
    section2 = ['NMS399', 'NMS375']
    section3 = ['CSC373', 'CSC431', 'CSC495']
    section4 = ['MAT163', 'MAT164', 'PHY119']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(2, section3)
    major.do_some(1, section4)
    return major.completion_percent()

def new_media():
    section1 = ['NMS220', 'NMS242', 'ENL242', 'C0M415', 'P0L371', 'NMS490']
    section2 = ['NMS399', 'NMS375']
    section3 = ['ART102', 'ART124', 'ART125', 'ART126', 'ART133', 'ART180', 'ART201', 'ART202', 'ART215', 'ART226', 'ART315', 'ART340', 'C0M243', 'CSC250', 'CSC431', 'CSC495', 'EDC220', 'ENL221', 'ENL226', 'ENL228', 'ENL229', 'ENL241', 'ENL290', 'ENL324', 'ENL371', 'ENL427', 'FLM180', 'FLM240', 'FLM260', 'FLM495', 'INS330', 'INS331', 'MUS221', 'MUS272', 'MUS336', 'NMS230', 'NMS260', 'NMS295', 'NMS320', 'NSM495', 'NMS499', 'PHI260', 'PHY261', 'P0L342', 'P0L495', 'RLN216']
    section4 = ['MAT163', 'MAT164', 'PHY119']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(4, section3)
    major.do_some(1, section4)
    return major.completion_percent()

def new_media_web_design():
    section1 = ['NMS220', 'NMS242', 'ENL242', 'C0M415', 'P0L371', 'NMS490', 'ART124', 'ART127', 'ART201', 'ART202', 'ART215', 'ART315', 'P0L495']
    section2 = ['NMS399', 'NMS375']
    section3 = ['MAT163', 'MAT164', 'PHY119']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    return major.completion_percent()

def new_media_promotional_communication():
    section1 = ['NMS220', 'NMS242', 'ENL242', 'COM415', 'POL371', 'NMS490']
    section2 = ['NMS399', 'NMS375']
    section3 = ['NMS230', 'NMS260', 'NMS320', 'COM120', 'COM480', 'ENL228', 'ENL427']
    section4 = ['MAT163', 'MAT164', 'PHY119']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(4, section3)
    major.do_some(1, section4)
    return major.completion_percent()

def biophysics():
    section1 = ['PHY121', 'PHY122', 'PHY245', 'PHY261', 'PHY317', 'PHY351', 'PHY362', 'PHY363', 'PHY395', 'PHY396', 'CHM115', 'CHM116', 'MAT145', 'MAT146', 'MAT245']
    section2 = ['PHY327', 'MAT369']
    section3 = ['BI0499', 'CHM499', 'MAT499', 'PHY499']
    section4 = ['PHY320', 'PHY352', 'PHY420', 'PHY430', 'PHY486']
    section5 = ['BIO253', 'BIO255', 'BI0369', 'BI0471', 'BI0475', 'BI0476', 'BI0486', 'CHM280', 'CHM368', 'CHM464', 'CHM481', 'MAT369', 'PHY327', 'PHY430']
    section6 = ['COM115', 'HON130']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(2, section4)
    major.do_some(1, section5)
    major.do_some(1, section6)
    return major.completion_percent()

def physics_bs():
    section1 = ['PHY121', 'PHY122', 'PHY245', 'PHY261', 'PHY351', 'PHY362', 'PHY363', 'PHY395', 'PHY396', 'CHM115', 'CHM116', 'MAT145', 'MAT146', 'MAT245']
    section2 = ['PHY327', 'MAT369']
    section3 = ['PHY317', 'PHY320', 'PHY352', 'PHY420', 'PHY430', 'PHY486']
    section4 = ['COM115', 'HON130']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(2, section3)
    major.do_some(1, section4)
    return major.completion_percent()

def physics_ba():
    section1 = ['PHY121', 'PHY122', 'PHY245', 'PHY351', 'PHY362', 'PHY363', 'PHY395', 'PHY396', 'MAT145', 'MAT146', 'MAT245']
    section2 = ['PHY327', 'MAT369']
    section3 = ['PHY261', 'PHY299', 'PHY317', 'PHY320', 'PHY327', 'PHY352', 'PHY399', 'PHY420', 'PHY430', 'PHY486', 'PHY499']
    section4 = ['COM111', 'COM115', 'MAT201', 'HON130']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(2, section3)
    major.do_some(1, section4)
    return major.completion_percent()

def politcal_science():
    section1 = ['P0L158', 'P0L483', 'P0L484']
    section2 = ['POL121', 'P0L122', 'POL160', 'POL170']
    section3 = ['P0L325, POL326, POL342, POL421','P0L350', 'POL359', 'POL459', 'P0L368', 'POL461', 'POL490', 'P0L370', 'POl371', 'P0L380' , 'POL381']
    section4 = ['POL121', 'P0L122', 'P0L124', 'POL160', 'POL170', 'P0L241', 'P0L295', 'P0L299', 'POL310', 'P0L341', 'P0L353', 'P0L354', 'P0L357', 'P0L399', 'P0L495', 'P0L499']
    section5 = ['P0L325', 'POL326', 'POL380']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(5, section3)
    major.do_some(1, section4)
    major.do_some(1, section5)
    return major.completion_percent()

def political_science_and_economics():
    section1 = ['EDC200', 'ESE310', 'ECO112', 'ECO113', 'ECO313', 'POL121']
    section2 = ['ECO312', 'ECO315']
    section3 = ['ECO312', 'ECO315', 'ECO318', 'ECO350', 'ECO360', 'ECO365', 'ECO370', 'ECO399', 'EC0416', 'EC0490', 'EC0495', 'EC0499']
    section4 = ['P0L325, POL326, POL342, POL421','P0L350', 'POL359', 'POL459', 'P0L368', 'POL461', 'POL490', 'P0L370', 'POl371', 'P0L380' , 'POL381']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(2, section4)
    return major.completion_percent()

def political_science_public_policy():
    section1 = ['P0L399', 'P0L484']
    section2 = ['ECO112', 'ECO113']
    section3 = ['POL121', 'P0L122']
    section4 = ['POL325', 'P0L326']
    section5 = ['EC0490', 'P0L483', 'S0C362']
    section6 = ['POL121', 'P0L122', 'P0L124', 'P0L158', 'POL160', 'POL170']
    section7 = ['P0L241', 'P0L325', 'P0L326', 'P0L342', 'P0L370', 'P0L371', 'P0L381', 'P0L421', 'P0L461', 'ECO312', 'ECO313', 'S0C381']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)
    major.do_some(1, section5)
    major.do_some(1, section6)
    major.do_some(4, section7)
    return major.completion_percent()

def political_science_prelaw():
    section1 = ['POL121', 'POL170', 'P0L483', 'P0L484']
    section2 = ['COM111', 'ENL220', 'ENL223', 'PHI230']
    section3 = ['P0L350', 'P0L370', 'P0L371', 'P0L380', 'P0L381']
    section4 = ['P0L325', 'POL326', 'POL380', 'COM111']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(2, section2)
    major.do_some(3, section3)
    major.do_some(2, section4)
    return major.completion_percent()

def theater_performance():
    section1 = ['THR228', 'THR229', 'THR232', 'THR250']
    section2 = ['THR245', 'THR270', 'THR273', 'THR361', 'THR362']
    section3 = ['THR226', 'THR350', 'THR355', 'THR365']
    section4 = ['THR226', 'THR230', 'FLM230', 'THR233', 'THR235', 'THR237', 'THR245', 'THR255', 'THR265', 'THR270', 'THR273', 'THR275', 'THR280', 'THR295', 'THR325', 'ENL325', 'THR326','ENL326', 'THR350', 'THR355', 'THR361', 'THR362', 'THR365', 'THR366', 'THR367', 'THR490', 'ENL221', 'ENL330', 'ENL338', 'ENL358', 'ENL368']
    section5 = ['GST200', 'MAT111', 'MAT145', 'MAT146', 'MAT163', 'MAT164', 'PH1230', 'PHY119']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(3, section2)
    major.do_some(3, section3)
    major.do_some(2, section4)
    major.do_some(1, section5)
    return major.completion_percent()

def theater_directing():
    section1 = ['THR228', 'THR229', 'THR232', 'THR250']
    section2 = ['THR245', 'THR270', 'THR273', 'THR361', 'THR362']
    section3 = ['THR325', 'THR326', 'THR366', 'THR367']
    section4 = ['THR226', 'THR230', 'FLM230', 'THR233', 'THR235', 'THR237', 'THR245', 'THR255', 'THR265', 'THR270', 'THR273', 'THR275', 'THR280', 'THR295', 'THR325', 'ENL325', 'THR326','ENL326', 'THR350', 'THR355', 'THR361', 'THR362', 'THR365', 'THR366', 'THR367', 'THR490', 'ENL221', 'ENL330', 'ENL338', 'ENL358', 'ENL368']
    section5 = ['GST200', 'MAT111', 'MAT145', 'MAT146', 'MAT163', 'MAT164', 'PH1230', 'PHY119']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(3, section2)
    major.do_some(3, section3)
    major.do_some(2, section4)
    major.do_some(1, section5)
    return major.completion_percent()

def theater_design_technical():
    section1 = ['THR228', 'THR229', 'THR232', 'THR250']
    section2 = ['THR245', 'THR270', 'THR273', 'THR361', 'THR362']
    section3 = ['THR230', 'THR275', 'THR280', 'THR285']
    section4 = ['THR226', 'THR230', 'FLM230', 'THR233', 'THR235', 'THR237', 'THR245', 'THR255', 'THR265', 'THR270', 'THR273', 'THR275', 'THR280', 'THR295', 'THR325', 'ENL325', 'THR326','ENL326', 'THR350', 'THR355', 'THR361', 'THR362', 'THR365', 'THR366', 'THR367', 'THR490', 'ENL221', 'ENL330', 'ENL338', 'ENL358', 'ENL368']
    section5 = ['GST200', 'MAT111', 'MAT145', 'MAT146', 'MAT163', 'MAT164', 'PH1230', 'PHY119']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(3, section2)
    major.do_some(3, section3)
    major.do_some(2, section4)
    major.do_some(1, section5)
    return major.completion_percent()

def theater():
    section1 = ['THR228', 'THR229', 'THR232', 'THR250']
    section2 = ['THR245', 'THR270', 'THR273', 'THR361', 'THR362']
    section3 = ['THR226', 'THR230', 'FLM230', 'THR233', 'THR235', 'THR237', 'THR245', 'THR255', 'THR265', 'THR270', 'THR273', 'THR275', 'THR280', 'THR295', 'THR325', 'ENL325', 'THR326','ENL326', 'THR350', 'THR355', 'THR361', 'THR362', 'THR365', 'THR366', 'THR367', 'THR490', 'ENL221', 'ENL330', 'ENL338', 'ENL358', 'ENL368']
    section4 = ['GST200', 'MAT111', 'MAT145', 'MAT146', 'MAT163', 'MAT164', 'PH1230', 'PHY119']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(3, section2)
    major.do_some(2, section3)
    major.do_some(1, section4)
    return major.completion_percent()

def psychology():
    section1 = ['PSY105', 'PSY215', 'PSY315', 'PSY400']
    section2 = ['PSY325', 'PSY354', 'PSY355']
    section3 = ['PSY491', 'PSY493', 'PSY495']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(2, section2)
    major.do_some(1, section3)
    return major.completion_percent()

def social_psychology():
    section1 = ['PSY105', 'PSY215', 'PSY315', 'PSY325', 'PSY400', 'SOC121', 'S0C375']
    section2 = ['PSY354', 'PSY355']
    section3 = ['PSY491', 'PSY493', 'PSY495']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    return major.completion_percent()

def internation_relations():
    section1 = ['ECO112', 'ECO113']
    section2 = ['HIS103', 'HIS104']
    section3 = ['P0L158', 'POL160']
    section4 = ['P0L490', 'KEY480']
    section5 = ['HIS332', 'P0L368', 'P0L459', 'P0L461']
    section6 = ['ANT141', 'INS225', 'P0L241', 'SWK230', 'WST250']
    section7 = ['BUS362', 'BUS465', 'C0M329', 'ECO360', 'ECO365', 'ECO370', 'ENV310', 'FIN460', 'FRE332', 'GER332', 'HIS323', 'HIS346', 'HIS352', 'HIS354', 'HIS440', 'HIS474', 'MKT466', 'P0L350', 'P0L459', 'P0L483', 'RLN276', 'SPA331', 'SPA332']
    major = ConLib.ConLib(transcript)
    major.do_some(1, section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)
    major.do_some(2, section5)
    major.do_some(1, section6)
    major.do_some(5, section7)
    return major.completion_percent()

def international_relations_business():
    section1 = ['ECO112', 'ECO113']
    section2 = ['HIS103', 'HIS104']
    section3 = ['P0L158', 'POL160']
    section4 = ['P0L490', 'KEY480']
    section5 = ['BUS362', 'BUS465', 'FIN460', 'MKT466']
    section6 = ['ECO360', 'ECO365', 'ECO370']
    section7 = ['HIS332', 'P0L368', 'P0L459', 'P0L461']
    section8 = ['BUS362', 'BUS465', 'C0M329', 'ECO360', 'ECO365', 'ECO370', 'ENV310', 'FIN460', 'FRE332', 'GER332', 'HIS323', 'HIS346', 'HIS352', 'HIS354', 'HIS440', 'HIS474', 'MKT466', 'P0L350', 'P0L459', 'P0L483', 'RLN276', 'SPA331', 'SPA332']
    major = ConLib.ConLib(transcript)
    major.do_some(1, section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)
    major.do_some(3, section5)
    major.do_some(1, section6)
    major.do_some(2, section7)
    major.do_some(2, section8)
    return major.completion_percent()

def nursing():
    section1 = ['NUR300', 'NUR305', 'NUR306', 'NUR403', 'NUR410', 'NUR411', 'NUR490']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    return major.completion_percent()

def religion():
    section1 = ['RLN209', 'RLN400']
    section2 = ['GST200', 'MAT145', 'MAT146', 'MAT163', 'MAT164', 'PHI230']
    section3 = ['RLN342', 'RLN370', 'RLN441']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    return major.completion_percent()

def philosophy():
    section1 = ['PHI241', 'PHI242', 'PHI343', 'PHI344']
    section2 = ['PHI230', 'PHI385']
    section3 = ['PHI110', 'PHI120', 'PHI125', 'PHI175', 'PHI180', 'PHI230', 'PHI260', 'PHI315', 'PHI350', 'PHI370', 'PHI380', 'PHI385', 'PHI399', 'PHI410', 'PHI499']
    section4 = ['PHI230']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(2, section3)
    major.do_all(section4)
    return major.completion_percent()

def theology_and_public_leadership():
    section1 = ['RLN209', 'RLN251', 'RLN290', 'RLN295', 'RLN342', 'RLN390', 'RLN399', 'RLN400', 'RLN441']
    section2 = ['GST200', 'MAT145', 'MAT146', 'MAT163', 'MAT164', 'PHI230']
    section3 = ['RLN342', 'RLN370', 'RLN441']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    return major.completion_percent()

def spanish():
    section1 = ['CCS100', 'KEY480']
    section2 = ['SPA334', 'SPA352', 'SPA353', 'SPA354', 'SPA356', 'SPA357']
    section3 = ['GST200', 'HIS369', 'MAT111', 'MAT145', 'MAT146', 'MAT163', 'MAT164', 'PHL230', 'PHY119', 'P0L483']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    return major.completion_percent()

def special_education():
    section1 = ['EDC200', 'EDC220', 'EDC310', 'EDC330', 'EDC331', 'EDC332', 'EDC333', 'EDC410', 'EED225', 'EED325', 'EED326', 'EED336', 'EED350', 'EED360', 'SPE410', 'SPE411', 'SPE415', 'SPE425', 'SPE430', 'SPE490']
    section2 = ['EDC206', 'EDC210']
    section3 = ['EDC481', 'SPE489', 'ENL111', 'HPE115', 'MAT137']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_all(section3)
    return major.completion_percent()

def womens_studies():
    section1 = ['WST201', 'WST315', 'WST399', 'WST485']
    section2 = ['GST200', 'MAT163', 'MAT164']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    return major.completion_percent()

def spacephysics():
    section1 = ['PHY121', 'PHY122', 'PHY245', 'PHY261', 'PHY320', 'PHY351', 'PHY362', 'PHY363', 'PHY395', 'PHY396', 'PHY420', 'CHM115', 'CHM116', 'MAT145', 'MAT146', 'MAT245']
    section2 = ['PHY327', 'MAT369']
    section3 = ['PHY317', 'PHY352', 'PHY430', 'PHY486']
    section4 = ['COM115', 'HON130']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(2, section3)
    major.do_some(1, section4)
    return major.completion_percent()

def clinicalpsychology():
    section1 = ['PSY105', 'PSY215', 'PSY262', 'PSY315', 'PSY385', 'PSY400']
    section2 = ['PSY325', 'PSY354', 'PSY355']
    section3 = ['PSY491', 'PSY493', 'PSY495']
    section4 = ['PSY261', 'PSY359']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(2, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)
    return major.completion_percent()

def psychologyandlaw():
    section1 = ['PSY105', 'PSY215', 'PSY235', 'PSY262', 'PSY315', 'PSY325', 'PSY354', 'PSY360', 'PSY400', 'PSY491', 'S0C277']
    section2 = ['PSY359', 'PSY385', 'PSY410']
    section3 = ['POL170', 'P0L370']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    return major.completion_percent()
    
def sociology():
    section1 = ['SOC121', 'SOC362', 'SOC363', 'SOC485', 'SOC490']
    section2 = ['SOC111', 'SOC231' ,'SOC240', 'SOC265', 'SOC266', 'SOC277', 'SOC290', 'SOC295', 'SOC299', 'SOC300', 'SOC320', 'SOC349', 'SOC375' ,'SOC377', 'SOC380', 'SOC381', 'SOC387', 'SOC390', 'SOC399', 'URB399', 'SOC495', 'SOC499']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some_upper(5, 3, section2)
    return major.completion_percent()
    
def socialwork():
    section1 = ['SWK301', 'SWK303', 'SWK306', 'SWK307', 'SWK316', 'SWK317', 'SWK401', 'SWK406', 'SWK407', 'SWK417']
    section2 = ['BI0121', 'PSY105' ,'S0C121', 'SWK280']
    section3 = ['SWK100', 'SWK210', 'SWK230']
    section4 = ['ECO112', 'POL121', 'P0L122', 'P0L325']
    section5 = ['S0C362', 'MAT163', 'MAT164']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_all(section2)
    major.do_some(1, section3)
    major.do_some(1, section4)
    major.do_some(1, section5)
    return major.completion_percent()
    
def urbanstudies():
    section1 = ['ECO113', 'POL/URB122', 'SOC/URB111', 'URB/SOC381', 'SOC/URB399', 'URB492']
    section2 = ['HIS316', 'SOC380', 'ART249/349', 'HIS249/349']
    section3 = ['POL483', 'SOC362']
    section4 = ['POL484', 'SOC363']
    section5 = ['ART243', 'ART244', 'ART249/349', 'HIS249/349', 'ECO365', 'ENV100', 'HIS316', 'POL241', 'POL325', 'SOC265', 'SOC349', 'SOC380', 'URB199', 'URB295' ,'URB299', 'URB395']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)
    major.do_some(2, section5)
    return major.completion_percent()

def exercise_science_ba():
    section1 = ['HPE104', 'HPE110', 'HPE114', 'HPE115', ' HPE205', 'HPE215', 'HPE220', 'HPE275', 'HPE300', 'HPE304', 'HPE305', 'HPE315', 'HPE350', 'HPE351', 'HPE357','HPE450', 'HPE452', 'HPE490', 'B10103']
    section2 = ['HPE397', 'HPE399']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    return major.completion_percent()

def exercise_science_pre_health_bs():
    section1 = ['HPE104', 'HPE110', 'HPE114', 'HPE115', ' HPE205', 'HPE275', 'HPE300', 'HPE304', 'HPE315', 'HPE350', 'HPE351', 'HPE357', 'HPE490']
    section2 = ['HPE397', 'HPE399']
    section3 = ['BI0151', 'BI0152', 'CHM115', 'CHM115L', 'CHM116', 'CHM116L', 'PHY107','PHY108', 'PSY105']
    section4 = ['PSY215', 'MAT163', 'MAT164']
    section5 = ['PSY203', 'PSY262']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    major.do_some(1, section3)
    major.do_some(1, section4)
    major.do_some(1, section5)
    return major.completion_percent()
	
def health_education():
    section1 = ['HPE104', 'HPE110', 'HPE114', 'HPE115', 'HPE215', 'HPE316', 'HPE320', 'HPE357', 'HPE358', 'HPE390', 'HPE410', 'HPE450', 'B1]I0103' ]
    section2 = ['PSY250', 'PSY252']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    return major.completion_percent()

def physical_education():
    section1 = ['HPE104', 'HPE114','HPE115','HPE205','HPE220','HPE254','HPE275','HPE324','HPE334','HPE335','HPE340','HPE350','HPE351','HPE357','HPE358','HPE473','BI0103']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    return major.completion_percent()

def interdisciplinary_studies():
    section1 = ['GST200', 'MAT145', 'MAT146', 'MAT163', 'PHI230']
    section2 = ['KEY490']
    major = ConLib.ConLib(transcript)
    major.do_all(section1)
    major.do_some(1, section2)
    return major.completion_percent()
    
functions = {
    0 : american_indian_studies,
    1 : art_history,
    2 : art_education,
    3 : graphic_design,
    4 : studio_art,
    5 : biology_ba,
    6 : biology_bs,
    7 : biopsychology,
    8 : life_sciences,
    9 : accounting,
    10 : finance,
    11 : international_business,
    12 : managment,
    13 : marketing,
    14 : managment_information_systems,
    15 : music_business,
    16 : cross_cultural_studies,
    17 : chemistry_acs,
    18 : chemistry,
    19 : chemistry_non_acs,
    20 : communication_studies,
    21 : computational_economics,
    22 : computational_philosophy,
    23 : computer_science_ba,
    24 : computer_science_bs,
    25 : applied_economics,
    26 : business_economics,
    27 : economics,
    28 : mathematical_economics,
    29 : elementary_education,
    30 : elementary_education_comm_arts,
    31 : elementary_education_general_science,
    32 : elementary_education_math,
    33 : elementary_education_social_studies,
    34 : english_commication_arts,
    35 : english_creative_writing,
    36 : english_literature,
    37 : enviormental_studies,
    38 : enviormental_studies_HECUA,
    39 : secondary_education,
    40 : social_studies,
    41 : english_second_language,
    42 : film_production,
    43 : theory_culture,
    44 : french,
    45 : german,
    46 : history,
    47 : exercise_science_ba,
    48 : exercise_science_pre_health_bs,
    49 : health_education,
    50 : physical_education,
    51 : interdisciplinary_studies,
    52 : internation_relations,
    53 : international_relations_business,
    54 : mathematics_ba,
    55 : mathematics_bs,
    56 : mathematics_teaching,
    57 : medieval_studies,
    58 : music,
    59 : music_business,
    60 : music_education,
    61 : music_performance,
    62 : music_therapy,
    63 : new_media,
    64 : new_media_game_design,
    65 : new_media_promotional_communication,
    66 : new_media_web_design,
    67 : nursing,
    68 : philosophy,
    69 : biophysics,
    70 : physics_ba,
    71 : physics_bs,
    72 : spacephysics,
    73 : political_science_and_economics,
    74 : politcal_science,
    75 : political_science_prelaw,
    76 : political_science_public_policy,
    77 : clinicalpsychology,
    78 : psychology,
    79 : psychologyandlaw,
    80 : social_psychology,
    81 : religion,
    82 : theology_and_public_leadership,
    83 : sociology,
    84 : spanish,
    85 : special_education,
    86 : socialwork,
    87 : theater,
    88 : theater_design_technical,
    89 : theater_directing,
    90 : theater_performance,
    91 : urbanstudies,
    92 : womens_studies,
}

def main():
    majors = []
    top = []
    for x in range(0, len(functions)):
        majors.append(functions[x]())
    majors = sorted(set(majors))[-3:]
    for y in range(0, len(functions)):
        if functions[y]() in majors:
            top.append(y)
    top = sorted(top)
    for z in top:
        print(functions[z])
        print(functions[z]())

if __name__ == "__main__":
    main()
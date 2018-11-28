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
    section2 = []
    section3 = []
    section4 = []
    section5 = ['COM111','COM115','HON130']
    section6 = []
    section7 = []
    major = ConLib.ConLib(transcript)
    major.do_some(1, section5)

def exercise_science_ba():
	section1 = ['HPE104', 'HPE110', 'HPE114', 'HPE115', ' HPE205', 'HPE215', 'HPE220', 'HPE275', 'HPE300', 'HPE304', 'HPE305', 'HPE315', 'HPE350', 'HPE351', 'HPE357','HPE450', 'HPE452', 'HPE490', 'B10103']
		
	section2 = ['HPE397', 'HPE399']

def exercise_science_pre_health_bs():
	section1 = ['HPE104', 'HPE110', 'HPE114', 'HPE115', ' HPE205', 'HPE275', 'HPE300', 'HPE304', 'HPE315', 'HPE350', 'HPE351', 'HPE357', 'HPE490']
	section2 = ['HPE397', 'HPE399']
	section3 = ['BI0151', 'BI0152', 'CHM115', 'CHM115L', 'CHM116', 'CHM116L', 'PHY107','PHY108', 'PSY105']
	section4 = ['PSY215', 'MAT163', 'MAT164']
	section5 = ['PSY203', 'PSY262']
	
def health_education():
	section1 = ['HPE104', 'HPE110', 'HPE114', 'HPE115', 'HPE215', 'HPE316', 'HPE320', 'HPE357', 'HPE358', 'HPE390', 'HPE410', 'HPE450', 'B1]I0103' ]
	section2 = ['PSY250', 'PSY252']
                 
def physical_education():
	section1 = ['HPE104', 'HPE114','HPE115','HPE205','HPE220','HPE254','HPE275','HPE324','HPE334','HPE335','HPE340','HPE350','HPE351','HPE357','HPE358','HPE473','BI0103']

def interdisciplinary_studies():
	section1 = ['GST200', 'MAT145', 'MAT146', 'MAT163', 'PHI230']
	section2 = ['KEY490']
	
def international_relations():
	section1 = ['ECO112','ECO113']
	section2 = ['HIS103', 'HIS104']
	section3 = ['POL158', 'POL160']
	section4 = ['POL490', 'KEY480']
	section5 = ['HIS332','POL368','POL459','POL461']
	section6 = ['ANT141','INS225','POL241','SWK230','WST250',]
	section7 = ['BUS362', 'BUS465', 'COM329', 'ECO360', 'ECO365', 'ECO370', 'ENV310', 'FIN460', 'FRE332', 'GER332', 'HIS323', 'HIS346', 'HIS352', 'HIS354', 'HIS440', 'HIS474', 'MKT466', 'POL350', 'POL459', 'POL483', 'RLN276', 'SPA331', 'SPA332']
	section8 = ['FRE212', 'GER212', 'SPA212']
	
def international_relations_intl_business():
	section1 = ['ECO112','ECO113']
	section2 = ['HIS103', 'HIS104']
	section3 = ['POL158', 'POL160']
	section4 = ['POL490', 'KEY480']
	section5 = ['BUS362','BUS465','FIN460','MKT466']
	section6 = ['ECO360','ECO365','ECO370']
	section7 = ['HIS332','POL368','POL459','POL461']
	section8 = ['ANT141', 'INS225', 'POL241', 'SWK230', 'WST250', 'COM329', 'ENV310', 'FRE332', 'GER332', 'HIS323', 'HIS346', 'HIS352', 'HIS354', 'HIS440', 'HIS474', 'POL350', 'POL459', 'POL483', 'RLN276', 'SPA331', 'SPA332']
	section9 = ['FRE212', 'GER212', 'SPA212']
	             
def mathematics_ba():
	section1 = ['MAT145','MAT146','MAT245','MAT246','MAT271']
	section2 = ['MAT304','MAT314','MAT324']
	section3 = ['MAT252','MAT273','MAT287','MAT304','MAT314','MAT324','MAT355','MAT363','MAT369','MAT373','MAT374','MAT377','MAT394','MAT395','MAT399','MAT499','EC0416','PHY327']
	section4 = ['MAT491']
	section5 = ['MAT201','COM111','COM115']

def mathematics_bs():
	section1 = ['MAT145','MAT146','MAT245','MAT246','MAT271']
	section2 = ['MAT304','MAT314','MAT324']
	section3 = ['MAT163', 'MAT164', 'MAT373', 'MAT394', 'MIS379', 'PSY215', 'SOC362']
	section4 = ['MAT355', 'MAT369', 'MAT374', 'MAT377']
	section5 = ['MAT491']
	section6 = ['MAT201','COM111','COM115']
	
def mathematics_teaching():
	section1 = ['MAT145','MAT146','MAT245', 'MAT246','MAT252','MAT271','MAT287','MAT314','MAT324',  'ESE330']
	section2 = ['MAT163','MAT164','MAT373']
	section3 = ['MAT355', 'MAT369', 'MAT374', 'MAT377']
	section4 = ['MAT491']
				
def medieval_studies():
	section1 = ['HUM120','HIS369','HIS370','LAT101','LAT102','HUM490']
	section2 = ['ENL330','ENL332', 'ENL360','ENL361','SPA352']
	section3 = ['HIS378','PHI242','RLN342']
	section4 = ['ART386','ART387','MUS231','THR361']
	section5 = ['HIS374','HIS440','POL380','SPA331']

def music_ba():
	section1 = ['MUS113','MUS114','MUS213','MUS214','MUS231','MUS232','MUS341','MUS458','MUS238']
	section2 = ['MUS331','MUS332','MUS333', 'MUS334']
	section3 = ['MUE111', 'MUE112', 'MUE114', 'MUE115', 'MUE121','MUE141']
	
				 
				 
				
				 
				 
	             
				 
				 
				 
				 
				 
				 
				 
				 
				 
	             
functions = {    
    0 : american_indian_studies,
    1 : american_history
}                
                 
def main():       
                 
    functions[1]()
if __name__ == "__main__":
    main()       
                 
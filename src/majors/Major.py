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


functions = {
    0 : american_indian_studies,
    1 : american_history
}

def main():

    functions[1]()
if __name__ == "__main__":
    main()
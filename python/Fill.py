class Fill:
    def __init__(self, file, runlist=[]):

        self.fillN = self.getFillNumber(file)
        self.runs = runlist
        self.isoBXs    = []
        self.firstBXs  = []
        self.lastBXs   = []
        self.middleBXs = []
        self.nonisoBXs = []
        self.allBXs    = []
        self.emptyBXs  = []

        scheme = self.readFile(file)
        self.getBXs(scheme)

    def readFile(self, filepath):    
        scheme = []
        with open(filepath,'r') as input:
            for line in input:
                if line.strip() == '1':
                    scheme.append(1)
                else:
                    scheme.append(0)

        return scheme

    def getBXs(self, scheme):
        
        # Loop over BXs between between [1,3562], the last two require special treatment
        for ibx in range(1,3563):
            prevBX = scheme[ibx-1]
            bx = scheme[ibx]
            nextBX = scheme[ibx+1]

            if bx:                               self.allBXs.append(ibx)
            if bx and not prevBX and not nextBX: self.isoBXs.append(ibx)
            if bx and not prevBX and     nextBX: self.firstBXs.append(ibx)
            if bx and     prevBX and not nextBX: self.lastBXs.append(ibx)
            if bx and     prevBX and     nextBX: self.middleBXs.append(ibx)
            if not bx:                           self.emptyBXs.append(ibx)
    
        #Add BX 3563, which is part of the abort gap and is always empty
        self.emptyBXs.append(3563)

        #Add last BX, which is the last bunch of the abort gap and is always empty
        #In the CMS numbering scheme this is BX=0, but HCAL PFG tuples follows the LHC numbering scheme in which this is BX=3564
        self.emptyBXs.append(3564)

    def getFillNumber(self, file):
        return int(file.split("/")[-1].split("bunchpattern")[-1].split(".txt")[0])

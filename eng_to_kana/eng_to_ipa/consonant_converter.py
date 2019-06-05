class ConsonantConverter:
    def __init__(self):
        self.vowels = 'aeiou'
        self.consonants = 'dgklmnptvʧŋɹʃðθ'

    def d_rule(self, word, ph, p_idx):
        # d, dz -- dd, z
        if p_idx+1 < len(ph) and ph[p_idx+1] == 'z':
            return 'z'
        elif p_idx >= 1 and ph[p_idx-1] in self.vowels and \
            (len(ph) <= 2 or ph[p_idx-2] not in self.vowels):
            return 'dd'
        else:
            return 'd'

    def gkpt_rule(self, word, ph, p_idx):
        # k, g, p, t -- kk, gg, pp, tt
        if p_idx >= 1 and ph[p_idx-1] in self.vowels and \
            (len(ph) <= 2 or ph[p_idx-2] not in self.vowels):
            return ph[p_idx]*2
        else:
            return  ph[p_idx]

    def l_rule(self, word, ph, p_idx):
        # l -- r
        return 'r'

    def mn_rule(self, word, ph, p_idx):
        # m, n not followed by vowel -- N
        # m, n at the end -- N
        if p_idx+1 < len(ph) and ph[p_idx+1] not in self.vowels:
            return 'N'
        elif p_idx == len(ph)-1 and ph[p_idx] == 'n':
            return 'N'
        else:
            return ph[p_idx]

    def v_rule(self, word, ph, p_idx):
        # v -- b
        return 'b'

    def tsh_rule(self, word, ph, p_idx):
        # ʧ -- ch or cch
        if p_idx >= 1 and ph[p_idx-1] in self.vowels and \
            (len(ph) <= 2 or ph[p_idx-2] not in self.vowels):
            return 'cch'
        else:
            return 'ch'

    def ng_rule(self, word, ph, p_idx):
        # ŋ -- N or Ng
        # TODO: darling --> daariN
        if 'ng' in word:
            return 'Ng'
        else:
            return 'N'

    def r_rule(self, word, ph, p_idx):
        # ɹ
        return 'r'

    def sh_rule(self, word, ph, p_idx):
        # ʃ
        if p_idx >= 1 and ph[p_idx-1] in self.vowels and \
            (len(ph) <= 2 or ph[p_idx-2] not in self.vowels):
            return 'ssh'
        else:
            return 'sh'

    def th_hakuon_rule(self, word, ph, p_idx):
        # ð -- z
        return 'z'

    def th_clear_rule(self, word, ph, i_idx):
        # θ
        return 's'

    def convertConsonant(self, word, ph):
        consonant_map = {
            'd': self.d_rule,
            'g': self.gkpt_rule,
            'k': self.gkpt_rule,
            'l': self.l_rule,
            'm': self.mn_rule,
            'n': self.mn_rule,
            'p': self.gkpt_rule,
            't': self.gkpt_rule,
            'v': self.v_rule,
            'ʧ': self.tsh_rule,
            'ŋ': self.ng_rule,
            'ɹ': self.r_rule,
            'ʃ': self.sh_rule,
            'ð': self.th_hakuon_rule,
            'θ': self.th_clear_rule
        }
        result = ''
        p_idx = 0
        while p_idx < len(ph):
            # adds a vowel char as is
            while p_idx < len(ph) and ph[p_idx] not in self.consonants:
                result += ph[p_idx]
                p_idx +=1 

            # converts a consonant
            if p_idx < len(ph) and ph[p_idx] in self.consonants:
                result += consonant_map[ph[p_idx]](word, ph, p_idx)
                p_idx += 1
        return result
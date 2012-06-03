# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 ../src/checkjs/parsers/antlr/JavaScript.g 2012-06-03 14:51:55

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
FUNCTION=4
LT=22
FUNCTION_BODY=7
DecimalDigit=37
EOF=-1
Identifier=23
SingleStringCharacter=30
T__93=93
T__94=94
T__91=91
T__92=92
T__90=90
Comment=49
SingleEscapeCharacter=34
UnicodeLetter=44
ExponentPart=41
MEMBER_EXPR=21
WhiteSpace=51
T__99=99
ASSIGNMENT_EXPR=14
T__98=98
ARRAY=11
T__97=97
T__96=96
UnicodeCombiningMark=47
T__95=95
UnicodeDigit=45
T__80=80
NumericLiteral=25
T__81=81
T__82=82
T__83=83
IdentifierStart=42
DoubleStringCharacter=29
T__85=85
T__84=84
T__87=87
T__86=86
T__89=89
T__88=88
FUNCTION_EXPR=5
T__71=71
T__72=72
T__70=70
PROPERTY=10
FUNCTION_PARAMETERS=6
CALL=17
CharacterEscapeSequence=31
T__76=76
T__75=75
T__74=74
EscapeSequence=26
T__73=73
T__79=79
UnicodeConnectorPunctuation=46
T__78=78
T__77=77
T__68=68
T__69=69
T__66=66
T__67=67
T__64=64
MEMBER=12
T__65=65
T__62=62
HexEscapeSequence=32
T__63=63
T__118=118
T__119=119
T__116=116
SingleSlash=48
T__117=117
T__114=114
T__115=115
LineComment=50
T__61=61
T__60=60
HexDigit=38
T__55=55
T__56=56
INDEX=20
T__57=57
T__58=58
T__52=52
T__53=53
T__54=54
T__107=107
OBJECT=9
T__108=108
T__109=109
T__59=59
T__103=103
T__104=104
T__105=105
T__106=106
T__111=111
T__110=110
T__113=113
EscapeCharacter=36
T__112=112
IdentifierPart=43
CALL_IDENTIFIER=18
OPERATOR_ARGS=16
UnicodeEscapeSequence=33
T__102=102
T__101=101
T__100=100
DecimalLiteral=39
RegexpFlags=28
RegexpCharacter=27
StringLiteral=24
OPERATOR_ARG=15
CALL_ARGUMENTS=19
HexIntegerLiteral=40
NonEscapeCharacter=35
ASSIGNMENT=13
VARIABLE_DECL=8

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "FUNCTION", "FUNCTION_EXPR", "FUNCTION_PARAMETERS", "FUNCTION_BODY", 
    "VARIABLE_DECL", "OBJECT", "PROPERTY", "ARRAY", "MEMBER", "ASSIGNMENT", 
    "ASSIGNMENT_EXPR", "OPERATOR_ARG", "OPERATOR_ARGS", "CALL", "CALL_IDENTIFIER", 
    "CALL_ARGUMENTS", "INDEX", "MEMBER_EXPR", "LT", "Identifier", "StringLiteral", 
    "NumericLiteral", "EscapeSequence", "RegexpCharacter", "RegexpFlags", 
    "DoubleStringCharacter", "SingleStringCharacter", "CharacterEscapeSequence", 
    "HexEscapeSequence", "UnicodeEscapeSequence", "SingleEscapeCharacter", 
    "NonEscapeCharacter", "EscapeCharacter", "DecimalDigit", "HexDigit", 
    "DecimalLiteral", "HexIntegerLiteral", "ExponentPart", "IdentifierStart", 
    "IdentifierPart", "UnicodeLetter", "UnicodeDigit", "UnicodeConnectorPunctuation", 
    "UnicodeCombiningMark", "SingleSlash", "Comment", "LineComment", "WhiteSpace", 
    "'function'", "';'", "'('", "','", "')'", "'{'", "'}'", "'var'", "'='", 
    "'if'", "'else'", "'do'", "'while'", "'for'", "'in'", "'continue'", 
    "'break'", "'return'", "'with'", "':'", "'switch'", "'case'", "'default'", 
    "'throw'", "'try'", "'catch'", "'finally'", "'new'", "'['", "']'", "'.'", 
    "'*='", "'/='", "'%='", "'+='", "'-='", "'<<='", "'>>='", "'>>>='", 
    "'&='", "'^='", "'|='", "'?'", "'*'", "'-'", "'+'", "'&'", "'&&'", "'|'", 
    "'||'", "'<'", "'<='", "'>'", "'>='", "'=='", "'!='", "'delete'", "'void'", 
    "'typeof'", "'++'", "'--'", "'~'", "'!'", "'this'", "'null'", "'true'", 
    "'false'", "'\\/'"
]




class JavaScriptParser(Parser):
    grammarFileName = "../src/checkjs/parsers/antlr/JavaScript.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(JavaScriptParser, self).__init__(input, state, *args, **kwargs)

        self._state.ruleMemo = {}
        self.dfa4 = self.DFA4(
            self, 4,
            eot = self.DFA4_eot,
            eof = self.DFA4_eof,
            min = self.DFA4_min,
            max = self.DFA4_max,
            accept = self.DFA4_accept,
            special = self.DFA4_special,
            transition = self.DFA4_transition
            )

        self.dfa5 = self.DFA5(
            self, 5,
            eot = self.DFA5_eot,
            eof = self.DFA5_eof,
            min = self.DFA5_min,
            max = self.DFA5_max,
            accept = self.DFA5_accept,
            special = self.DFA5_special,
            transition = self.DFA5_transition
            )

        self.dfa18 = self.DFA18(
            self, 18,
            eot = self.DFA18_eot,
            eof = self.DFA18_eof,
            min = self.DFA18_min,
            max = self.DFA18_max,
            accept = self.DFA18_accept,
            special = self.DFA18_special,
            transition = self.DFA18_transition
            )

        self.dfa17 = self.DFA17(
            self, 17,
            eot = self.DFA17_eot,
            eof = self.DFA17_eof,
            min = self.DFA17_min,
            max = self.DFA17_max,
            accept = self.DFA17_accept,
            special = self.DFA17_special,
            transition = self.DFA17_transition
            )

        self.dfa24 = self.DFA24(
            self, 24,
            eot = self.DFA24_eot,
            eof = self.DFA24_eof,
            min = self.DFA24_min,
            max = self.DFA24_max,
            accept = self.DFA24_accept,
            special = self.DFA24_special,
            transition = self.DFA24_transition
            )

        self.dfa29 = self.DFA29(
            self, 29,
            eot = self.DFA29_eot,
            eof = self.DFA29_eof,
            min = self.DFA29_min,
            max = self.DFA29_max,
            accept = self.DFA29_accept,
            special = self.DFA29_special,
            transition = self.DFA29_transition
            )

        self.dfa34 = self.DFA34(
            self, 34,
            eot = self.DFA34_eot,
            eof = self.DFA34_eof,
            min = self.DFA34_min,
            max = self.DFA34_max,
            accept = self.DFA34_accept,
            special = self.DFA34_special,
            transition = self.DFA34_transition
            )

        self.dfa37 = self.DFA37(
            self, 37,
            eot = self.DFA37_eot,
            eof = self.DFA37_eof,
            min = self.DFA37_min,
            max = self.DFA37_max,
            accept = self.DFA37_accept,
            special = self.DFA37_special,
            transition = self.DFA37_transition
            )

        self.dfa40 = self.DFA40(
            self, 40,
            eot = self.DFA40_eot,
            eof = self.DFA40_eof,
            min = self.DFA40_min,
            max = self.DFA40_max,
            accept = self.DFA40_accept,
            special = self.DFA40_special,
            transition = self.DFA40_transition
            )

        self.dfa50 = self.DFA50(
            self, 50,
            eot = self.DFA50_eot,
            eof = self.DFA50_eof,
            min = self.DFA50_min,
            max = self.DFA50_max,
            accept = self.DFA50_accept,
            special = self.DFA50_special,
            transition = self.DFA50_transition
            )

        self.dfa53 = self.DFA53(
            self, 53,
            eot = self.DFA53_eot,
            eof = self.DFA53_eof,
            min = self.DFA53_min,
            max = self.DFA53_max,
            accept = self.DFA53_accept,
            special = self.DFA53_special,
            transition = self.DFA53_transition
            )

        self.dfa57 = self.DFA57(
            self, 57,
            eot = self.DFA57_eot,
            eof = self.DFA57_eof,
            min = self.DFA57_min,
            max = self.DFA57_max,
            accept = self.DFA57_accept,
            special = self.DFA57_special,
            transition = self.DFA57_transition
            )

        self.dfa65 = self.DFA65(
            self, 65,
            eot = self.DFA65_eot,
            eof = self.DFA65_eof,
            min = self.DFA65_min,
            max = self.DFA65_max,
            accept = self.DFA65_accept,
            special = self.DFA65_special,
            transition = self.DFA65_transition
            )

        self.dfa68 = self.DFA68(
            self, 68,
            eot = self.DFA68_eot,
            eof = self.DFA68_eof,
            min = self.DFA68_min,
            max = self.DFA68_max,
            accept = self.DFA68_accept,
            special = self.DFA68_special,
            transition = self.DFA68_transition
            )

        self.dfa71 = self.DFA71(
            self, 71,
            eot = self.DFA71_eot,
            eof = self.DFA71_eof,
            min = self.DFA71_min,
            max = self.DFA71_max,
            accept = self.DFA71_accept,
            special = self.DFA71_special,
            transition = self.DFA71_transition
            )

        self.dfa74 = self.DFA74(
            self, 74,
            eot = self.DFA74_eot,
            eof = self.DFA74_eof,
            min = self.DFA74_min,
            max = self.DFA74_max,
            accept = self.DFA74_accept,
            special = self.DFA74_special,
            transition = self.DFA74_transition
            )

        self.dfa77 = self.DFA77(
            self, 77,
            eot = self.DFA77_eot,
            eof = self.DFA77_eof,
            min = self.DFA77_min,
            max = self.DFA77_max,
            accept = self.DFA77_accept,
            special = self.DFA77_special,
            transition = self.DFA77_transition
            )

        self.dfa86 = self.DFA86(
            self, 86,
            eot = self.DFA86_eot,
            eof = self.DFA86_eof,
            min = self.DFA86_min,
            max = self.DFA86_max,
            accept = self.DFA86_accept,
            special = self.DFA86_special,
            transition = self.DFA86_transition
            )

        self.dfa99 = self.DFA99(
            self, 99,
            eot = self.DFA99_eot,
            eof = self.DFA99_eof,
            min = self.DFA99_min,
            max = self.DFA99_max,
            accept = self.DFA99_accept,
            special = self.DFA99_special,
            transition = self.DFA99_transition
            )

        self.dfa107 = self.DFA107(
            self, 107,
            eot = self.DFA107_eot,
            eof = self.DFA107_eof,
            min = self.DFA107_min,
            max = self.DFA107_max,
            accept = self.DFA107_accept,
            special = self.DFA107_special,
            transition = self.DFA107_transition
            )

        self.dfa111 = self.DFA111(
            self, 111,
            eot = self.DFA111_eot,
            eof = self.DFA111_eof,
            min = self.DFA111_min,
            max = self.DFA111_max,
            accept = self.DFA111_accept,
            special = self.DFA111_special,
            transition = self.DFA111_transition
            )

        self.dfa110 = self.DFA110(
            self, 110,
            eot = self.DFA110_eot,
            eof = self.DFA110_eof,
            min = self.DFA110_min,
            max = self.DFA110_max,
            accept = self.DFA110_accept,
            special = self.DFA110_special,
            transition = self.DFA110_transition
            )

        self.dfa124 = self.DFA124(
            self, 124,
            eot = self.DFA124_eot,
            eof = self.DFA124_eof,
            min = self.DFA124_min,
            max = self.DFA124_max,
            accept = self.DFA124_accept,
            special = self.DFA124_special,
            transition = self.DFA124_transition
            )

        self.dfa133 = self.DFA133(
            self, 133,
            eot = self.DFA133_eot,
            eof = self.DFA133_eof,
            min = self.DFA133_min,
            max = self.DFA133_max,
            accept = self.DFA133_accept,
            special = self.DFA133_special,
            transition = self.DFA133_transition
            )

        self.dfa136 = self.DFA136(
            self, 136,
            eot = self.DFA136_eot,
            eof = self.DFA136_eof,
            min = self.DFA136_min,
            max = self.DFA136_max,
            accept = self.DFA136_accept,
            special = self.DFA136_special,
            transition = self.DFA136_transition
            )

        self.dfa141 = self.DFA141(
            self, 141,
            eot = self.DFA141_eot,
            eof = self.DFA141_eof,
            min = self.DFA141_min,
            max = self.DFA141_max,
            accept = self.DFA141_accept,
            special = self.DFA141_special,
            transition = self.DFA141_transition
            )

        self.dfa144 = self.DFA144(
            self, 144,
            eot = self.DFA144_eot,
            eof = self.DFA144_eof,
            min = self.DFA144_min,
            max = self.DFA144_max,
            accept = self.DFA144_accept,
            special = self.DFA144_special,
            transition = self.DFA144_transition
            )

        self.dfa146 = self.DFA146(
            self, 146,
            eot = self.DFA146_eot,
            eof = self.DFA146_eof,
            min = self.DFA146_min,
            max = self.DFA146_max,
            accept = self.DFA146_accept,
            special = self.DFA146_special,
            transition = self.DFA146_transition
            )

        self.dfa151 = self.DFA151(
            self, 151,
            eot = self.DFA151_eot,
            eof = self.DFA151_eof,
            min = self.DFA151_min,
            max = self.DFA151_max,
            accept = self.DFA151_accept,
            special = self.DFA151_special,
            transition = self.DFA151_transition
            )

        self.dfa155 = self.DFA155(
            self, 155,
            eot = self.DFA155_eot,
            eof = self.DFA155_eof,
            min = self.DFA155_min,
            max = self.DFA155_max,
            accept = self.DFA155_accept,
            special = self.DFA155_special,
            transition = self.DFA155_transition
            )

        self.dfa161 = self.DFA161(
            self, 161,
            eot = self.DFA161_eot,
            eof = self.DFA161_eof,
            min = self.DFA161_min,
            max = self.DFA161_max,
            accept = self.DFA161_accept,
            special = self.DFA161_special,
            transition = self.DFA161_transition
            )

        self.dfa160 = self.DFA160(
            self, 160,
            eot = self.DFA160_eot,
            eof = self.DFA160_eof,
            min = self.DFA160_min,
            max = self.DFA160_max,
            accept = self.DFA160_accept,
            special = self.DFA160_special,
            transition = self.DFA160_transition
            )

        self.dfa170 = self.DFA170(
            self, 170,
            eot = self.DFA170_eot,
            eof = self.DFA170_eof,
            min = self.DFA170_min,
            max = self.DFA170_max,
            accept = self.DFA170_accept,
            special = self.DFA170_special,
            transition = self.DFA170_transition
            )

        self.dfa173 = self.DFA173(
            self, 173,
            eot = self.DFA173_eot,
            eof = self.DFA173_eof,
            min = self.DFA173_min,
            max = self.DFA173_max,
            accept = self.DFA173_accept,
            special = self.DFA173_special,
            transition = self.DFA173_transition
            )

        self.dfa184 = self.DFA184(
            self, 184,
            eot = self.DFA184_eot,
            eof = self.DFA184_eof,
            min = self.DFA184_min,
            max = self.DFA184_max,
            accept = self.DFA184_accept,
            special = self.DFA184_special,
            transition = self.DFA184_transition
            )

        self.dfa183 = self.DFA183(
            self, 183,
            eot = self.DFA183_eot,
            eof = self.DFA183_eof,
            min = self.DFA183_min,
            max = self.DFA183_max,
            accept = self.DFA183_accept,
            special = self.DFA183_special,
            transition = self.DFA183_transition
            )

        self.dfa189 = self.DFA189(
            self, 189,
            eot = self.DFA189_eot,
            eof = self.DFA189_eof,
            min = self.DFA189_min,
            max = self.DFA189_max,
            accept = self.DFA189_accept,
            special = self.DFA189_special,
            transition = self.DFA189_transition
            )

        self.dfa210 = self.DFA210(
            self, 210,
            eot = self.DFA210_eot,
            eof = self.DFA210_eof,
            min = self.DFA210_min,
            max = self.DFA210_max,
            accept = self.DFA210_accept,
            special = self.DFA210_special,
            transition = self.DFA210_transition
            )






        self._adaptor = None
        self.adaptor = CommonTreeAdaptor()
                


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class program_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.program_return, self).__init__()

            self.tree = None




    # $ANTLR start "program"
    # ../src/checkjs/parsers/antlr/JavaScript.g:45:1: program : ( LT )* sourceElements ( LT )* EOF ;
    def program(self, ):

        retval = self.program_return()
        retval.start = self.input.LT(1)
        program_StartIndex = self.input.index()
        root_0 = None

        LT1 = None
        LT3 = None
        EOF4 = None
        sourceElements2 = None


        LT1_tree = None
        LT3_tree = None
        EOF4_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 1):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:46:2: ( ( LT )* sourceElements ( LT )* EOF )
                # ../src/checkjs/parsers/antlr/JavaScript.g:46:4: ( LT )* sourceElements ( LT )* EOF
                pass 
                root_0 = self._adaptor.nil()

                # ../src/checkjs/parsers/antlr/JavaScript.g:46:6: ( LT )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == LT) :
                        alt1 = 1


                    if alt1 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT1=self.match(self.input, LT, self.FOLLOW_LT_in_program187)


                    else:
                        break #loop1
                self._state.following.append(self.FOLLOW_sourceElements_in_program191)
                sourceElements2 = self.sourceElements()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, sourceElements2.tree)
                # ../src/checkjs/parsers/antlr/JavaScript.g:46:26: ( LT )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == LT) :
                        alt2 = 1


                    if alt2 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT3=self.match(self.input, LT, self.FOLLOW_LT_in_program193)


                    else:
                        break #loop2
                EOF4=self.match(self.input, EOF, self.FOLLOW_EOF_in_program197)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 1, program_StartIndex, success)

            pass
        return retval

    # $ANTLR end "program"

    class sourceElements_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.sourceElements_return, self).__init__()

            self.tree = None




    # $ANTLR start "sourceElements"
    # ../src/checkjs/parsers/antlr/JavaScript.g:49:1: sourceElements : sourceElement ( ( LT )* sourceElement )* ;
    def sourceElements(self, ):

        retval = self.sourceElements_return()
        retval.start = self.input.LT(1)
        sourceElements_StartIndex = self.input.index()
        root_0 = None

        LT6 = None
        sourceElement5 = None

        sourceElement7 = None


        LT6_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 2):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:50:2: ( sourceElement ( ( LT )* sourceElement )* )
                # ../src/checkjs/parsers/antlr/JavaScript.g:50:4: sourceElement ( ( LT )* sourceElement )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_sourceElement_in_sourceElements209)
                sourceElement5 = self.sourceElement()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, sourceElement5.tree)
                # ../src/checkjs/parsers/antlr/JavaScript.g:50:18: ( ( LT )* sourceElement )*
                while True: #loop4
                    alt4 = 2
                    alt4 = self.dfa4.predict(self.input)
                    if alt4 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:50:19: ( LT )* sourceElement
                        pass 
                        # ../src/checkjs/parsers/antlr/JavaScript.g:50:21: ( LT )*
                        while True: #loop3
                            alt3 = 2
                            LA3_0 = self.input.LA(1)

                            if (LA3_0 == LT) :
                                alt3 = 1


                            if alt3 == 1:
                                # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                                pass 
                                LT6=self.match(self.input, LT, self.FOLLOW_LT_in_sourceElements212)


                            else:
                                break #loop3
                        self._state.following.append(self.FOLLOW_sourceElement_in_sourceElements216)
                        sourceElement7 = self.sourceElement()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, sourceElement7.tree)


                    else:
                        break #loop4



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 2, sourceElements_StartIndex, success)

            pass
        return retval

    # $ANTLR end "sourceElements"

    class sourceElement_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.sourceElement_return, self).__init__()

            self.tree = None




    # $ANTLR start "sourceElement"
    # ../src/checkjs/parsers/antlr/JavaScript.g:53:1: sourceElement : ( functionDeclaration | statement );
    def sourceElement(self, ):

        retval = self.sourceElement_return()
        retval.start = self.input.LT(1)
        sourceElement_StartIndex = self.input.index()
        root_0 = None

        functionDeclaration8 = None

        statement9 = None



        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 3):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:54:2: ( functionDeclaration | statement )
                alt5 = 2
                alt5 = self.dfa5.predict(self.input)
                if alt5 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:54:4: functionDeclaration
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_functionDeclaration_in_sourceElement229)
                    functionDeclaration8 = self.functionDeclaration()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, functionDeclaration8.tree)


                elif alt5 == 2:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:55:4: statement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_statement_in_sourceElement234)
                    statement9 = self.statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, statement9.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 3, sourceElement_StartIndex, success)

            pass
        return retval

    # $ANTLR end "sourceElement"

    class functionDeclaration_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.functionDeclaration_return, self).__init__()

            self.tree = None




    # $ANTLR start "functionDeclaration"
    # ../src/checkjs/parsers/antlr/JavaScript.g:59:1: functionDeclaration : 'function' ( LT )* Identifier ( LT )* formalParameterList ( LT )* functionBody ( ';' )? -> ^( FUNCTION Identifier formalParameterList functionBody ) ;
    def functionDeclaration(self, ):

        retval = self.functionDeclaration_return()
        retval.start = self.input.LT(1)
        functionDeclaration_StartIndex = self.input.index()
        root_0 = None

        string_literal10 = None
        LT11 = None
        Identifier12 = None
        LT13 = None
        LT15 = None
        char_literal17 = None
        formalParameterList14 = None

        functionBody16 = None


        string_literal10_tree = None
        LT11_tree = None
        Identifier12_tree = None
        LT13_tree = None
        LT15_tree = None
        char_literal17_tree = None
        stream_LT = RewriteRuleTokenStream(self._adaptor, "token LT")
        stream_52 = RewriteRuleTokenStream(self._adaptor, "token 52")
        stream_53 = RewriteRuleTokenStream(self._adaptor, "token 53")
        stream_Identifier = RewriteRuleTokenStream(self._adaptor, "token Identifier")
        stream_functionBody = RewriteRuleSubtreeStream(self._adaptor, "rule functionBody")
        stream_formalParameterList = RewriteRuleSubtreeStream(self._adaptor, "rule formalParameterList")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 4):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:60:2: ( 'function' ( LT )* Identifier ( LT )* formalParameterList ( LT )* functionBody ( ';' )? -> ^( FUNCTION Identifier formalParameterList functionBody ) )
                # ../src/checkjs/parsers/antlr/JavaScript.g:60:4: 'function' ( LT )* Identifier ( LT )* formalParameterList ( LT )* functionBody ( ';' )?
                pass 
                string_literal10=self.match(self.input, 52, self.FOLLOW_52_in_functionDeclaration246) 
                if self._state.backtracking == 0:
                    stream_52.add(string_literal10)
                # ../src/checkjs/parsers/antlr/JavaScript.g:60:15: ( LT )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == LT) :
                        alt6 = 1


                    if alt6 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT11=self.match(self.input, LT, self.FOLLOW_LT_in_functionDeclaration248) 
                        if self._state.backtracking == 0:
                            stream_LT.add(LT11)


                    else:
                        break #loop6
                Identifier12=self.match(self.input, Identifier, self.FOLLOW_Identifier_in_functionDeclaration251) 
                if self._state.backtracking == 0:
                    stream_Identifier.add(Identifier12)
                # ../src/checkjs/parsers/antlr/JavaScript.g:60:30: ( LT )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == LT) :
                        alt7 = 1


                    if alt7 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT13=self.match(self.input, LT, self.FOLLOW_LT_in_functionDeclaration253) 
                        if self._state.backtracking == 0:
                            stream_LT.add(LT13)


                    else:
                        break #loop7
                self._state.following.append(self.FOLLOW_formalParameterList_in_functionDeclaration256)
                formalParameterList14 = self.formalParameterList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_formalParameterList.add(formalParameterList14.tree)
                # ../src/checkjs/parsers/antlr/JavaScript.g:60:54: ( LT )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == LT) :
                        alt8 = 1


                    if alt8 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT15=self.match(self.input, LT, self.FOLLOW_LT_in_functionDeclaration258) 
                        if self._state.backtracking == 0:
                            stream_LT.add(LT15)


                    else:
                        break #loop8
                self._state.following.append(self.FOLLOW_functionBody_in_functionDeclaration261)
                functionBody16 = self.functionBody()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_functionBody.add(functionBody16.tree)
                # ../src/checkjs/parsers/antlr/JavaScript.g:60:71: ( ';' )?
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == 53) :
                    alt9 = 1
                if alt9 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: ';'
                    pass 
                    char_literal17=self.match(self.input, 53, self.FOLLOW_53_in_functionDeclaration263) 
                    if self._state.backtracking == 0:
                        stream_53.add(char_literal17)




                # AST Rewrite
                # elements: formalParameterList, Identifier, functionBody
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 60:76: -> ^( FUNCTION Identifier formalParameterList functionBody )
                    # ../src/checkjs/parsers/antlr/JavaScript.g:61:9: ^( FUNCTION Identifier formalParameterList functionBody )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FUNCTION, "FUNCTION"), root_1)

                    self._adaptor.addChild(root_1, stream_Identifier.nextNode())
                    self._adaptor.addChild(root_1, stream_formalParameterList.nextTree())
                    self._adaptor.addChild(root_1, stream_functionBody.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 4, functionDeclaration_StartIndex, success)

            pass
        return retval

    # $ANTLR end "functionDeclaration"

    class functionExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.functionExpression_return, self).__init__()

            self.tree = None




    # $ANTLR start "functionExpression"
    # ../src/checkjs/parsers/antlr/JavaScript.g:64:1: functionExpression : 'function' ( LT )* ( Identifier )? ( LT )* formalParameterList ( LT )* functionBody -> ^( FUNCTION_EXPR formalParameterList functionBody ) ;
    def functionExpression(self, ):

        retval = self.functionExpression_return()
        retval.start = self.input.LT(1)
        functionExpression_StartIndex = self.input.index()
        root_0 = None

        string_literal18 = None
        LT19 = None
        Identifier20 = None
        LT21 = None
        LT23 = None
        formalParameterList22 = None

        functionBody24 = None


        string_literal18_tree = None
        LT19_tree = None
        Identifier20_tree = None
        LT21_tree = None
        LT23_tree = None
        stream_LT = RewriteRuleTokenStream(self._adaptor, "token LT")
        stream_52 = RewriteRuleTokenStream(self._adaptor, "token 52")
        stream_Identifier = RewriteRuleTokenStream(self._adaptor, "token Identifier")
        stream_functionBody = RewriteRuleSubtreeStream(self._adaptor, "rule functionBody")
        stream_formalParameterList = RewriteRuleSubtreeStream(self._adaptor, "rule formalParameterList")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 5):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:65:2: ( 'function' ( LT )* ( Identifier )? ( LT )* formalParameterList ( LT )* functionBody -> ^( FUNCTION_EXPR formalParameterList functionBody ) )
                # ../src/checkjs/parsers/antlr/JavaScript.g:65:4: 'function' ( LT )* ( Identifier )? ( LT )* formalParameterList ( LT )* functionBody
                pass 
                string_literal18=self.match(self.input, 52, self.FOLLOW_52_in_functionExpression299) 
                if self._state.backtracking == 0:
                    stream_52.add(string_literal18)
                # ../src/checkjs/parsers/antlr/JavaScript.g:65:15: ( LT )*
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == LT) :
                        LA10_2 = self.input.LA(2)

                        if (self.synpred10_JavaScript()) :
                            alt10 = 1




                    if alt10 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT19=self.match(self.input, LT, self.FOLLOW_LT_in_functionExpression301) 
                        if self._state.backtracking == 0:
                            stream_LT.add(LT19)


                    else:
                        break #loop10
                # ../src/checkjs/parsers/antlr/JavaScript.g:65:19: ( Identifier )?
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == Identifier) :
                    alt11 = 1
                if alt11 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: Identifier
                    pass 
                    Identifier20=self.match(self.input, Identifier, self.FOLLOW_Identifier_in_functionExpression304) 
                    if self._state.backtracking == 0:
                        stream_Identifier.add(Identifier20)



                # ../src/checkjs/parsers/antlr/JavaScript.g:65:31: ( LT )*
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == LT) :
                        alt12 = 1


                    if alt12 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT21=self.match(self.input, LT, self.FOLLOW_LT_in_functionExpression307) 
                        if self._state.backtracking == 0:
                            stream_LT.add(LT21)


                    else:
                        break #loop12
                self._state.following.append(self.FOLLOW_formalParameterList_in_functionExpression310)
                formalParameterList22 = self.formalParameterList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_formalParameterList.add(formalParameterList22.tree)
                # ../src/checkjs/parsers/antlr/JavaScript.g:65:55: ( LT )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == LT) :
                        alt13 = 1


                    if alt13 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT23=self.match(self.input, LT, self.FOLLOW_LT_in_functionExpression312) 
                        if self._state.backtracking == 0:
                            stream_LT.add(LT23)


                    else:
                        break #loop13
                self._state.following.append(self.FOLLOW_functionBody_in_functionExpression315)
                functionBody24 = self.functionBody()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_functionBody.add(functionBody24.tree)

                # AST Rewrite
                # elements: functionBody, formalParameterList
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 65:72: -> ^( FUNCTION_EXPR formalParameterList functionBody )
                    # ../src/checkjs/parsers/antlr/JavaScript.g:66:9: ^( FUNCTION_EXPR formalParameterList functionBody )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FUNCTION_EXPR, "FUNCTION_EXPR"), root_1)

                    self._adaptor.addChild(root_1, stream_formalParameterList.nextTree())
                    self._adaptor.addChild(root_1, stream_functionBody.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 5, functionExpression_StartIndex, success)

            pass
        return retval

    # $ANTLR end "functionExpression"

    class formalParameterList_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.formalParameterList_return, self).__init__()

            self.tree = None




    # $ANTLR start "formalParameterList"
    # ../src/checkjs/parsers/antlr/JavaScript.g:69:1: formalParameterList : '(' ( ( LT )* Identifier ( ( LT )* ',' ( LT )* Identifier )* )? ( LT )* ')' -> ^( FUNCTION_PARAMETERS ( Identifier )* ) ;
    def formalParameterList(self, ):

        retval = self.formalParameterList_return()
        retval.start = self.input.LT(1)
        formalParameterList_StartIndex = self.input.index()
        root_0 = None

        char_literal25 = None
        LT26 = None
        Identifier27 = None
        LT28 = None
        char_literal29 = None
        LT30 = None
        Identifier31 = None
        LT32 = None
        char_literal33 = None

        char_literal25_tree = None
        LT26_tree = None
        Identifier27_tree = None
        LT28_tree = None
        char_literal29_tree = None
        LT30_tree = None
        Identifier31_tree = None
        LT32_tree = None
        char_literal33_tree = None
        stream_LT = RewriteRuleTokenStream(self._adaptor, "token LT")
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_55 = RewriteRuleTokenStream(self._adaptor, "token 55")
        stream_54 = RewriteRuleTokenStream(self._adaptor, "token 54")
        stream_Identifier = RewriteRuleTokenStream(self._adaptor, "token Identifier")

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 6):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:70:2: ( '(' ( ( LT )* Identifier ( ( LT )* ',' ( LT )* Identifier )* )? ( LT )* ')' -> ^( FUNCTION_PARAMETERS ( Identifier )* ) )
                # ../src/checkjs/parsers/antlr/JavaScript.g:70:4: '(' ( ( LT )* Identifier ( ( LT )* ',' ( LT )* Identifier )* )? ( LT )* ')'
                pass 
                char_literal25=self.match(self.input, 54, self.FOLLOW_54_in_formalParameterList345) 
                if self._state.backtracking == 0:
                    stream_54.add(char_literal25)
                # ../src/checkjs/parsers/antlr/JavaScript.g:70:8: ( ( LT )* Identifier ( ( LT )* ',' ( LT )* Identifier )* )?
                alt18 = 2
                alt18 = self.dfa18.predict(self.input)
                if alt18 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:70:9: ( LT )* Identifier ( ( LT )* ',' ( LT )* Identifier )*
                    pass 
                    # ../src/checkjs/parsers/antlr/JavaScript.g:70:9: ( LT )*
                    while True: #loop14
                        alt14 = 2
                        LA14_0 = self.input.LA(1)

                        if (LA14_0 == LT) :
                            alt14 = 1


                        if alt14 == 1:
                            # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                            pass 
                            LT26=self.match(self.input, LT, self.FOLLOW_LT_in_formalParameterList348) 
                            if self._state.backtracking == 0:
                                stream_LT.add(LT26)


                        else:
                            break #loop14
                    Identifier27=self.match(self.input, Identifier, self.FOLLOW_Identifier_in_formalParameterList351) 
                    if self._state.backtracking == 0:
                        stream_Identifier.add(Identifier27)
                    # ../src/checkjs/parsers/antlr/JavaScript.g:70:24: ( ( LT )* ',' ( LT )* Identifier )*
                    while True: #loop17
                        alt17 = 2
                        alt17 = self.dfa17.predict(self.input)
                        if alt17 == 1:
                            # ../src/checkjs/parsers/antlr/JavaScript.g:70:25: ( LT )* ',' ( LT )* Identifier
                            pass 
                            # ../src/checkjs/parsers/antlr/JavaScript.g:70:25: ( LT )*
                            while True: #loop15
                                alt15 = 2
                                LA15_0 = self.input.LA(1)

                                if (LA15_0 == LT) :
                                    alt15 = 1


                                if alt15 == 1:
                                    # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                                    pass 
                                    LT28=self.match(self.input, LT, self.FOLLOW_LT_in_formalParameterList354) 
                                    if self._state.backtracking == 0:
                                        stream_LT.add(LT28)


                                else:
                                    break #loop15
                            char_literal29=self.match(self.input, 55, self.FOLLOW_55_in_formalParameterList357) 
                            if self._state.backtracking == 0:
                                stream_55.add(char_literal29)
                            # ../src/checkjs/parsers/antlr/JavaScript.g:70:33: ( LT )*
                            while True: #loop16
                                alt16 = 2
                                LA16_0 = self.input.LA(1)

                                if (LA16_0 == LT) :
                                    alt16 = 1


                                if alt16 == 1:
                                    # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                                    pass 
                                    LT30=self.match(self.input, LT, self.FOLLOW_LT_in_formalParameterList359) 
                                    if self._state.backtracking == 0:
                                        stream_LT.add(LT30)


                                else:
                                    break #loop16
                            Identifier31=self.match(self.input, Identifier, self.FOLLOW_Identifier_in_formalParameterList362) 
                            if self._state.backtracking == 0:
                                stream_Identifier.add(Identifier31)


                        else:
                            break #loop17



                # ../src/checkjs/parsers/antlr/JavaScript.g:70:52: ( LT )*
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == LT) :
                        alt19 = 1


                    if alt19 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT32=self.match(self.input, LT, self.FOLLOW_LT_in_formalParameterList368) 
                        if self._state.backtracking == 0:
                            stream_LT.add(LT32)


                    else:
                        break #loop19
                char_literal33=self.match(self.input, 56, self.FOLLOW_56_in_formalParameterList371) 
                if self._state.backtracking == 0:
                    stream_56.add(char_literal33)

                # AST Rewrite
                # elements: Identifier
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 71:9: -> ^( FUNCTION_PARAMETERS ( Identifier )* )
                    # ../src/checkjs/parsers/antlr/JavaScript.g:71:12: ^( FUNCTION_PARAMETERS ( Identifier )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FUNCTION_PARAMETERS, "FUNCTION_PARAMETERS"), root_1)

                    # ../src/checkjs/parsers/antlr/JavaScript.g:71:35: ( Identifier )*
                    while stream_Identifier.hasNext():
                        self._adaptor.addChild(root_1, stream_Identifier.nextNode())


                    stream_Identifier.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 6, formalParameterList_StartIndex, success)

            pass
        return retval

    # $ANTLR end "formalParameterList"

    class functionBody_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.functionBody_return, self).__init__()

            self.tree = None




    # $ANTLR start "functionBody"
    # ../src/checkjs/parsers/antlr/JavaScript.g:74:1: functionBody : '{' ( LT )* ( sourceElements )? ( LT )* '}' -> ^( FUNCTION_BODY ( sourceElements )? ) ;
    def functionBody(self, ):

        retval = self.functionBody_return()
        retval.start = self.input.LT(1)
        functionBody_StartIndex = self.input.index()
        root_0 = None

        char_literal34 = None
        LT35 = None
        LT37 = None
        char_literal38 = None
        sourceElements36 = None


        char_literal34_tree = None
        LT35_tree = None
        LT37_tree = None
        char_literal38_tree = None
        stream_LT = RewriteRuleTokenStream(self._adaptor, "token LT")
        stream_58 = RewriteRuleTokenStream(self._adaptor, "token 58")
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_sourceElements = RewriteRuleSubtreeStream(self._adaptor, "rule sourceElements")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 7):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:75:2: ( '{' ( LT )* ( sourceElements )? ( LT )* '}' -> ^( FUNCTION_BODY ( sourceElements )? ) )
                # ../src/checkjs/parsers/antlr/JavaScript.g:75:4: '{' ( LT )* ( sourceElements )? ( LT )* '}'
                pass 
                char_literal34=self.match(self.input, 57, self.FOLLOW_57_in_functionBody400) 
                if self._state.backtracking == 0:
                    stream_57.add(char_literal34)
                # ../src/checkjs/parsers/antlr/JavaScript.g:75:8: ( LT )*
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == LT) :
                        LA20_2 = self.input.LA(2)

                        if (self.synpred20_JavaScript()) :
                            alt20 = 1




                    if alt20 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT35=self.match(self.input, LT, self.FOLLOW_LT_in_functionBody402) 
                        if self._state.backtracking == 0:
                            stream_LT.add(LT35)


                    else:
                        break #loop20
                # ../src/checkjs/parsers/antlr/JavaScript.g:75:12: ( sourceElements )?
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if ((Identifier <= LA21_0 <= NumericLiteral) or LA21_0 == 52 or LA21_0 == 54 or LA21_0 == 57 or LA21_0 == 59 or LA21_0 == 61 or (63 <= LA21_0 <= 65) or (67 <= LA21_0 <= 70) or LA21_0 == 72 or (75 <= LA21_0 <= 76) or (79 <= LA21_0 <= 80) or (96 <= LA21_0 <= 97) or (108 <= LA21_0 <= 119)) :
                    alt21 = 1
                if alt21 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: sourceElements
                    pass 
                    self._state.following.append(self.FOLLOW_sourceElements_in_functionBody405)
                    sourceElements36 = self.sourceElements()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_sourceElements.add(sourceElements36.tree)



                # ../src/checkjs/parsers/antlr/JavaScript.g:75:28: ( LT )*
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if (LA22_0 == LT) :
                        alt22 = 1


                    if alt22 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT37=self.match(self.input, LT, self.FOLLOW_LT_in_functionBody408) 
                        if self._state.backtracking == 0:
                            stream_LT.add(LT37)


                    else:
                        break #loop22
                char_literal38=self.match(self.input, 58, self.FOLLOW_58_in_functionBody411) 
                if self._state.backtracking == 0:
                    stream_58.add(char_literal38)

                # AST Rewrite
                # elements: sourceElements
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 75:36: -> ^( FUNCTION_BODY ( sourceElements )? )
                    # ../src/checkjs/parsers/antlr/JavaScript.g:75:39: ^( FUNCTION_BODY ( sourceElements )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FUNCTION_BODY, "FUNCTION_BODY"), root_1)

                    # ../src/checkjs/parsers/antlr/JavaScript.g:75:56: ( sourceElements )?
                    if stream_sourceElements.hasNext():
                        self._adaptor.addChild(root_1, stream_sourceElements.nextTree())


                    stream_sourceElements.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 7, functionBody_StartIndex, success)

            pass
        return retval

    # $ANTLR end "functionBody"

    class djangoVariable_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.djangoVariable_return, self).__init__()

            self.tree = None




    # $ANTLR start "djangoVariable"
    # ../src/checkjs/parsers/antlr/JavaScript.g:84:1: djangoVariable : '{' '{' ( '}' '}' | . ) ;
    def djangoVariable(self, ):

        retval = self.djangoVariable_return()
        retval.start = self.input.LT(1)
        djangoVariable_StartIndex = self.input.index()
        root_0 = None

        char_literal39 = None
        char_literal40 = None
        char_literal41 = None
        char_literal42 = None
        wildcard43 = None

        char_literal39_tree = None
        char_literal40_tree = None
        char_literal41_tree = None
        char_literal42_tree = None
        wildcard43_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 8):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:85:5: ( '{' '{' ( '}' '}' | . ) )
                # ../src/checkjs/parsers/antlr/JavaScript.g:85:7: '{' '{' ( '}' '}' | . )
                pass 
                root_0 = self._adaptor.nil()

                char_literal39=self.match(self.input, 57, self.FOLLOW_57_in_djangoVariable441)
                if self._state.backtracking == 0:

                    char_literal39_tree = self._adaptor.createWithPayload(char_literal39)
                    self._adaptor.addChild(root_0, char_literal39_tree)

                char_literal40=self.match(self.input, 57, self.FOLLOW_57_in_djangoVariable443)
                if self._state.backtracking == 0:

                    char_literal40_tree = self._adaptor.createWithPayload(char_literal40)
                    self._adaptor.addChild(root_0, char_literal40_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:85:15: ( '}' '}' | . )
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if (LA23_0 == 58) :
                    LA23_1 = self.input.LA(2)

                    if (LA23_1 == 58) :
                        alt23 = 1
                    elif (LA23_1 == EOF) :
                        alt23 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 23, 1, self.input)

                        raise nvae

                elif ((FUNCTION <= LA23_0 <= 57) or (59 <= LA23_0 <= 119)) :
                    alt23 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 23, 0, self.input)

                    raise nvae

                if alt23 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:85:16: '}' '}'
                    pass 
                    char_literal41=self.match(self.input, 58, self.FOLLOW_58_in_djangoVariable446)
                    if self._state.backtracking == 0:

                        char_literal41_tree = self._adaptor.createWithPayload(char_literal41)
                        self._adaptor.addChild(root_0, char_literal41_tree)

                    char_literal42=self.match(self.input, 58, self.FOLLOW_58_in_djangoVariable448)
                    if self._state.backtracking == 0:

                        char_literal42_tree = self._adaptor.createWithPayload(char_literal42)
                        self._adaptor.addChild(root_0, char_literal42_tree)



                elif alt23 == 2:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:85:26: .
                    pass 
                    wildcard43 = self.input.LT(1)
                    self.matchAny(self.input)
                    if self._state.backtracking == 0:

                        wildcard43_tree = self._adaptor.createWithPayload(wildcard43)
                        self._adaptor.addChild(root_0, wildcard43_tree)







                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 8, djangoVariable_StartIndex, success)

            pass
        return retval

    # $ANTLR end "djangoVariable"

    class statement_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.statement_return, self).__init__()

            self.tree = None




    # $ANTLR start "statement"
    # ../src/checkjs/parsers/antlr/JavaScript.g:94:1: statement : ( variableStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement );
    def statement(self, ):

        retval = self.statement_return()
        retval.start = self.input.LT(1)
        statement_StartIndex = self.input.index()
        root_0 = None

        variableStatement44 = None

        expressionStatement45 = None

        ifStatement46 = None

        iterationStatement47 = None

        continueStatement48 = None

        breakStatement49 = None

        returnStatement50 = None

        withStatement51 = None

        labelledStatement52 = None

        switchStatement53 = None

        throwStatement54 = None

        tryStatement55 = None



        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 9):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:95:2: ( variableStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement )
                alt24 = 12
                alt24 = self.dfa24.predict(self.input)
                if alt24 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:95:4: variableStatement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_variableStatement_in_statement474)
                    variableStatement44 = self.variableStatement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, variableStatement44.tree)


                elif alt24 == 2:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:97:4: expressionStatement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_expressionStatement_in_statement481)
                    expressionStatement45 = self.expressionStatement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expressionStatement45.tree)


                elif alt24 == 3:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:99:4: ifStatement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_ifStatement_in_statement491)
                    ifStatement46 = self.ifStatement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, ifStatement46.tree)


                elif alt24 == 4:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:100:4: iterationStatement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_iterationStatement_in_statement496)
                    iterationStatement47 = self.iterationStatement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, iterationStatement47.tree)


                elif alt24 == 5:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:101:4: continueStatement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_continueStatement_in_statement501)
                    continueStatement48 = self.continueStatement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, continueStatement48.tree)


                elif alt24 == 6:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:102:4: breakStatement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_breakStatement_in_statement506)
                    breakStatement49 = self.breakStatement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, breakStatement49.tree)


                elif alt24 == 7:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:103:4: returnStatement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_returnStatement_in_statement511)
                    returnStatement50 = self.returnStatement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, returnStatement50.tree)


                elif alt24 == 8:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:104:4: withStatement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_withStatement_in_statement516)
                    withStatement51 = self.withStatement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, withStatement51.tree)


                elif alt24 == 9:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:105:4: labelledStatement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_labelledStatement_in_statement521)
                    labelledStatement52 = self.labelledStatement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, labelledStatement52.tree)


                elif alt24 == 10:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:106:4: switchStatement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_switchStatement_in_statement526)
                    switchStatement53 = self.switchStatement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, switchStatement53.tree)


                elif alt24 == 11:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:107:4: throwStatement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_throwStatement_in_statement531)
                    throwStatement54 = self.throwStatement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, throwStatement54.tree)


                elif alt24 == 12:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:108:4: tryStatement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_tryStatement_in_statement536)
                    tryStatement55 = self.tryStatement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, tryStatement55.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 9, statement_StartIndex, success)

            pass
        return retval

    # $ANTLR end "statement"

    class statementBlock_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.statementBlock_return, self).__init__()

            self.tree = None




    # $ANTLR start "statementBlock"
    # ../src/checkjs/parsers/antlr/JavaScript.g:111:1: statementBlock : '{' ( LT )* ( statementList )? ( LT )* '}' ;
    def statementBlock(self, ):

        retval = self.statementBlock_return()
        retval.start = self.input.LT(1)
        statementBlock_StartIndex = self.input.index()
        root_0 = None

        char_literal56 = None
        LT57 = None
        LT59 = None
        char_literal60 = None
        statementList58 = None


        char_literal56_tree = None
        LT57_tree = None
        LT59_tree = None
        char_literal60_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 10):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:112:2: ( '{' ( LT )* ( statementList )? ( LT )* '}' )
                # ../src/checkjs/parsers/antlr/JavaScript.g:112:4: '{' ( LT )* ( statementList )? ( LT )* '}'
                pass 
                root_0 = self._adaptor.nil()

                char_literal56=self.match(self.input, 57, self.FOLLOW_57_in_statementBlock547)
                if self._state.backtracking == 0:

                    char_literal56_tree = self._adaptor.createWithPayload(char_literal56)
                    self._adaptor.addChild(root_0, char_literal56_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:112:10: ( LT )*
                while True: #loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == LT) :
                        LA25_2 = self.input.LA(2)

                        if (self.synpred35_JavaScript()) :
                            alt25 = 1




                    if alt25 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT57=self.match(self.input, LT, self.FOLLOW_LT_in_statementBlock549)


                    else:
                        break #loop25
                # ../src/checkjs/parsers/antlr/JavaScript.g:112:13: ( statementList )?
                alt26 = 2
                LA26_0 = self.input.LA(1)

                if ((Identifier <= LA26_0 <= NumericLiteral) or LA26_0 == 52 or LA26_0 == 54 or LA26_0 == 57 or LA26_0 == 59 or LA26_0 == 61 or (63 <= LA26_0 <= 65) or (67 <= LA26_0 <= 70) or LA26_0 == 72 or (75 <= LA26_0 <= 76) or (79 <= LA26_0 <= 80) or (96 <= LA26_0 <= 97) or (108 <= LA26_0 <= 119)) :
                    alt26 = 1
                if alt26 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: statementList
                    pass 
                    self._state.following.append(self.FOLLOW_statementList_in_statementBlock553)
                    statementList58 = self.statementList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, statementList58.tree)



                # ../src/checkjs/parsers/antlr/JavaScript.g:112:30: ( LT )*
                while True: #loop27
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == LT) :
                        alt27 = 1


                    if alt27 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT59=self.match(self.input, LT, self.FOLLOW_LT_in_statementBlock556)


                    else:
                        break #loop27
                char_literal60=self.match(self.input, 58, self.FOLLOW_58_in_statementBlock560)
                if self._state.backtracking == 0:

                    char_literal60_tree = self._adaptor.createWithPayload(char_literal60)
                    self._adaptor.addChild(root_0, char_literal60_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 10, statementBlock_StartIndex, success)

            pass
        return retval

    # $ANTLR end "statementBlock"

    class statementList_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.statementList_return, self).__init__()

            self.tree = None




    # $ANTLR start "statementList"
    # ../src/checkjs/parsers/antlr/JavaScript.g:115:1: statementList : statement ( ( LT )* statement )* ;
    def statementList(self, ):

        retval = self.statementList_return()
        retval.start = self.input.LT(1)
        statementList_StartIndex = self.input.index()
        root_0 = None

        LT62 = None
        statement61 = None

        statement63 = None


        LT62_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 11):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:116:2: ( statement ( ( LT )* statement )* )
                # ../src/checkjs/parsers/antlr/JavaScript.g:116:4: statement ( ( LT )* statement )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_statement_in_statementList571)
                statement61 = self.statement()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, statement61.tree)
                # ../src/checkjs/parsers/antlr/JavaScript.g:116:14: ( ( LT )* statement )*
                while True: #loop29
                    alt29 = 2
                    alt29 = self.dfa29.predict(self.input)
                    if alt29 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:116:15: ( LT )* statement
                        pass 
                        # ../src/checkjs/parsers/antlr/JavaScript.g:116:17: ( LT )*
                        while True: #loop28
                            alt28 = 2
                            LA28_0 = self.input.LA(1)

                            if (LA28_0 == LT) :
                                alt28 = 1


                            if alt28 == 1:
                                # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                                pass 
                                LT62=self.match(self.input, LT, self.FOLLOW_LT_in_statementList574)


                            else:
                                break #loop28
                        self._state.following.append(self.FOLLOW_statement_in_statementList578)
                        statement63 = self.statement()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, statement63.tree)


                    else:
                        break #loop29



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 11, statementList_StartIndex, success)

            pass
        return retval

    # $ANTLR end "statementList"

    class variableStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.variableStatement_return, self).__init__()

            self.tree = None




    # $ANTLR start "variableStatement"
    # ../src/checkjs/parsers/antlr/JavaScript.g:119:1: variableStatement : 'var' ( LT )* variableDeclarationList ( LT )* ';' ;
    def variableStatement(self, ):

        retval = self.variableStatement_return()
        retval.start = self.input.LT(1)
        variableStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal64 = None
        LT65 = None
        LT67 = None
        char_literal68 = None
        variableDeclarationList66 = None


        string_literal64_tree = None
        LT65_tree = None
        LT67_tree = None
        char_literal68_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 12):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:120:2: ( 'var' ( LT )* variableDeclarationList ( LT )* ';' )
                # ../src/checkjs/parsers/antlr/JavaScript.g:120:4: 'var' ( LT )* variableDeclarationList ( LT )* ';'
                pass 
                root_0 = self._adaptor.nil()

                string_literal64=self.match(self.input, 59, self.FOLLOW_59_in_variableStatement591)
                # ../src/checkjs/parsers/antlr/JavaScript.g:120:13: ( LT )*
                while True: #loop30
                    alt30 = 2
                    LA30_0 = self.input.LA(1)

                    if (LA30_0 == LT) :
                        alt30 = 1


                    if alt30 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT65=self.match(self.input, LT, self.FOLLOW_LT_in_variableStatement594)


                    else:
                        break #loop30
                self._state.following.append(self.FOLLOW_variableDeclarationList_in_variableStatement598)
                variableDeclarationList66 = self.variableDeclarationList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, variableDeclarationList66.tree)
                # ../src/checkjs/parsers/antlr/JavaScript.g:120:42: ( LT )*
                while True: #loop31
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if (LA31_0 == LT) :
                        alt31 = 1


                    if alt31 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT67=self.match(self.input, LT, self.FOLLOW_LT_in_variableStatement600)


                    else:
                        break #loop31
                char_literal68=self.match(self.input, 53, self.FOLLOW_53_in_variableStatement604)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 12, variableStatement_StartIndex, success)

            pass
        return retval

    # $ANTLR end "variableStatement"

    class variableDeclarationList_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.variableDeclarationList_return, self).__init__()

            self.tree = None




    # $ANTLR start "variableDeclarationList"
    # ../src/checkjs/parsers/antlr/JavaScript.g:123:1: variableDeclarationList : variableDeclaration ( ( LT )* ',' ( LT )* variableDeclaration )* ;
    def variableDeclarationList(self, ):

        retval = self.variableDeclarationList_return()
        retval.start = self.input.LT(1)
        variableDeclarationList_StartIndex = self.input.index()
        root_0 = None

        LT70 = None
        char_literal71 = None
        LT72 = None
        variableDeclaration69 = None

        variableDeclaration73 = None


        LT70_tree = None
        char_literal71_tree = None
        LT72_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 13):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:124:2: ( variableDeclaration ( ( LT )* ',' ( LT )* variableDeclaration )* )
                # ../src/checkjs/parsers/antlr/JavaScript.g:124:4: variableDeclaration ( ( LT )* ',' ( LT )* variableDeclaration )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_variableDeclaration_in_variableDeclarationList616)
                variableDeclaration69 = self.variableDeclaration()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, variableDeclaration69.tree)
                # ../src/checkjs/parsers/antlr/JavaScript.g:124:24: ( ( LT )* ',' ( LT )* variableDeclaration )*
                while True: #loop34
                    alt34 = 2
                    alt34 = self.dfa34.predict(self.input)
                    if alt34 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:124:25: ( LT )* ',' ( LT )* variableDeclaration
                        pass 
                        # ../src/checkjs/parsers/antlr/JavaScript.g:124:27: ( LT )*
                        while True: #loop32
                            alt32 = 2
                            LA32_0 = self.input.LA(1)

                            if (LA32_0 == LT) :
                                alt32 = 1


                            if alt32 == 1:
                                # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                                pass 
                                LT70=self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationList619)


                            else:
                                break #loop32
                        char_literal71=self.match(self.input, 55, self.FOLLOW_55_in_variableDeclarationList623)
                        # ../src/checkjs/parsers/antlr/JavaScript.g:124:37: ( LT )*
                        while True: #loop33
                            alt33 = 2
                            LA33_0 = self.input.LA(1)

                            if (LA33_0 == LT) :
                                alt33 = 1


                            if alt33 == 1:
                                # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                                pass 
                                LT72=self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationList626)


                            else:
                                break #loop33
                        self._state.following.append(self.FOLLOW_variableDeclaration_in_variableDeclarationList630)
                        variableDeclaration73 = self.variableDeclaration()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, variableDeclaration73.tree)


                    else:
                        break #loop34



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 13, variableDeclarationList_StartIndex, success)

            pass
        return retval

    # $ANTLR end "variableDeclarationList"

    class variableDeclarationListNoIn_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.variableDeclarationListNoIn_return, self).__init__()

            self.tree = None




    # $ANTLR start "variableDeclarationListNoIn"
    # ../src/checkjs/parsers/antlr/JavaScript.g:127:1: variableDeclarationListNoIn : variableDeclarationNoIn ( ( LT )* ',' ( LT )* variableDeclarationNoIn )* ;
    def variableDeclarationListNoIn(self, ):

        retval = self.variableDeclarationListNoIn_return()
        retval.start = self.input.LT(1)
        variableDeclarationListNoIn_StartIndex = self.input.index()
        root_0 = None

        LT75 = None
        char_literal76 = None
        LT77 = None
        variableDeclarationNoIn74 = None

        variableDeclarationNoIn78 = None


        LT75_tree = None
        char_literal76_tree = None
        LT77_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 14):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:128:2: ( variableDeclarationNoIn ( ( LT )* ',' ( LT )* variableDeclarationNoIn )* )
                # ../src/checkjs/parsers/antlr/JavaScript.g:128:4: variableDeclarationNoIn ( ( LT )* ',' ( LT )* variableDeclarationNoIn )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_variableDeclarationNoIn_in_variableDeclarationListNoIn643)
                variableDeclarationNoIn74 = self.variableDeclarationNoIn()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, variableDeclarationNoIn74.tree)
                # ../src/checkjs/parsers/antlr/JavaScript.g:128:28: ( ( LT )* ',' ( LT )* variableDeclarationNoIn )*
                while True: #loop37
                    alt37 = 2
                    alt37 = self.dfa37.predict(self.input)
                    if alt37 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:128:29: ( LT )* ',' ( LT )* variableDeclarationNoIn
                        pass 
                        # ../src/checkjs/parsers/antlr/JavaScript.g:128:31: ( LT )*
                        while True: #loop35
                            alt35 = 2
                            LA35_0 = self.input.LA(1)

                            if (LA35_0 == LT) :
                                alt35 = 1


                            if alt35 == 1:
                                # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                                pass 
                                LT75=self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationListNoIn646)


                            else:
                                break #loop35
                        char_literal76=self.match(self.input, 55, self.FOLLOW_55_in_variableDeclarationListNoIn650)
                        # ../src/checkjs/parsers/antlr/JavaScript.g:128:41: ( LT )*
                        while True: #loop36
                            alt36 = 2
                            LA36_0 = self.input.LA(1)

                            if (LA36_0 == LT) :
                                alt36 = 1


                            if alt36 == 1:
                                # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                                pass 
                                LT77=self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationListNoIn653)


                            else:
                                break #loop36
                        self._state.following.append(self.FOLLOW_variableDeclarationNoIn_in_variableDeclarationListNoIn657)
                        variableDeclarationNoIn78 = self.variableDeclarationNoIn()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, variableDeclarationNoIn78.tree)


                    else:
                        break #loop37



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 14, variableDeclarationListNoIn_StartIndex, success)

            pass
        return retval

    # $ANTLR end "variableDeclarationListNoIn"

    class variableDeclaration_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.variableDeclaration_return, self).__init__()

            self.tree = None




    # $ANTLR start "variableDeclaration"
    # ../src/checkjs/parsers/antlr/JavaScript.g:131:1: variableDeclaration : ( Identifier ( LT )* initialiser -> ^( VARIABLE_DECL Identifier initialiser ) | Identifier ( LT )* -> ^( VARIABLE_DECL Identifier ) );
    def variableDeclaration(self, ):

        retval = self.variableDeclaration_return()
        retval.start = self.input.LT(1)
        variableDeclaration_StartIndex = self.input.index()
        root_0 = None

        Identifier79 = None
        LT80 = None
        Identifier82 = None
        LT83 = None
        initialiser81 = None


        Identifier79_tree = None
        LT80_tree = None
        Identifier82_tree = None
        LT83_tree = None
        stream_LT = RewriteRuleTokenStream(self._adaptor, "token LT")
        stream_Identifier = RewriteRuleTokenStream(self._adaptor, "token Identifier")
        stream_initialiser = RewriteRuleSubtreeStream(self._adaptor, "rule initialiser")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 15):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:132:2: ( Identifier ( LT )* initialiser -> ^( VARIABLE_DECL Identifier initialiser ) | Identifier ( LT )* -> ^( VARIABLE_DECL Identifier ) )
                alt40 = 2
                alt40 = self.dfa40.predict(self.input)
                if alt40 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:132:4: Identifier ( LT )* initialiser
                    pass 
                    Identifier79=self.match(self.input, Identifier, self.FOLLOW_Identifier_in_variableDeclaration670) 
                    if self._state.backtracking == 0:
                        stream_Identifier.add(Identifier79)
                    # ../src/checkjs/parsers/antlr/JavaScript.g:132:15: ( LT )*
                    while True: #loop38
                        alt38 = 2
                        LA38_0 = self.input.LA(1)

                        if (LA38_0 == LT) :
                            alt38 = 1


                        if alt38 == 1:
                            # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                            pass 
                            LT80=self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclaration672) 
                            if self._state.backtracking == 0:
                                stream_LT.add(LT80)


                        else:
                            break #loop38
                    self._state.following.append(self.FOLLOW_initialiser_in_variableDeclaration675)
                    initialiser81 = self.initialiser()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_initialiser.add(initialiser81.tree)

                    # AST Rewrite
                    # elements: Identifier, initialiser
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 132:31: -> ^( VARIABLE_DECL Identifier initialiser )
                        # ../src/checkjs/parsers/antlr/JavaScript.g:132:34: ^( VARIABLE_DECL Identifier initialiser )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VARIABLE_DECL, "VARIABLE_DECL"), root_1)

                        self._adaptor.addChild(root_1, stream_Identifier.nextNode())
                        self._adaptor.addChild(root_1, stream_initialiser.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt40 == 2:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:133:4: Identifier ( LT )*
                    pass 
                    Identifier82=self.match(self.input, Identifier, self.FOLLOW_Identifier_in_variableDeclaration691) 
                    if self._state.backtracking == 0:
                        stream_Identifier.add(Identifier82)
                    # ../src/checkjs/parsers/antlr/JavaScript.g:133:15: ( LT )*
                    while True: #loop39
                        alt39 = 2
                        LA39_0 = self.input.LA(1)

                        if (LA39_0 == LT) :
                            LA39_1 = self.input.LA(2)

                            if (self.synpred50_JavaScript()) :
                                alt39 = 1




                        if alt39 == 1:
                            # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                            pass 
                            LT83=self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclaration693) 
                            if self._state.backtracking == 0:
                                stream_LT.add(LT83)


                        else:
                            break #loop39

                    # AST Rewrite
                    # elements: Identifier
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 133:19: -> ^( VARIABLE_DECL Identifier )
                        # ../src/checkjs/parsers/antlr/JavaScript.g:133:22: ^( VARIABLE_DECL Identifier )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VARIABLE_DECL, "VARIABLE_DECL"), root_1)

                        self._adaptor.addChild(root_1, stream_Identifier.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 15, variableDeclaration_StartIndex, success)

            pass
        return retval

    # $ANTLR end "variableDeclaration"

    class variableDeclarationNoIn_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.variableDeclarationNoIn_return, self).__init__()

            self.tree = None




    # $ANTLR start "variableDeclarationNoIn"
    # ../src/checkjs/parsers/antlr/JavaScript.g:136:1: variableDeclarationNoIn : Identifier ( LT )* ( initialiserNoIn )? -> ^( VARIABLE_DECL Identifier initialiserNoIn ) ;
    def variableDeclarationNoIn(self, ):

        retval = self.variableDeclarationNoIn_return()
        retval.start = self.input.LT(1)
        variableDeclarationNoIn_StartIndex = self.input.index()
        root_0 = None

        Identifier84 = None
        LT85 = None
        initialiserNoIn86 = None


        Identifier84_tree = None
        LT85_tree = None
        stream_LT = RewriteRuleTokenStream(self._adaptor, "token LT")
        stream_Identifier = RewriteRuleTokenStream(self._adaptor, "token Identifier")
        stream_initialiserNoIn = RewriteRuleSubtreeStream(self._adaptor, "rule initialiserNoIn")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 16):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:137:2: ( Identifier ( LT )* ( initialiserNoIn )? -> ^( VARIABLE_DECL Identifier initialiserNoIn ) )
                # ../src/checkjs/parsers/antlr/JavaScript.g:137:4: Identifier ( LT )* ( initialiserNoIn )?
                pass 
                Identifier84=self.match(self.input, Identifier, self.FOLLOW_Identifier_in_variableDeclarationNoIn714) 
                if self._state.backtracking == 0:
                    stream_Identifier.add(Identifier84)
                # ../src/checkjs/parsers/antlr/JavaScript.g:137:15: ( LT )*
                while True: #loop41
                    alt41 = 2
                    LA41_0 = self.input.LA(1)

                    if (LA41_0 == LT) :
                        LA41_2 = self.input.LA(2)

                        if (self.synpred51_JavaScript()) :
                            alt41 = 1




                    if alt41 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT85=self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationNoIn716) 
                        if self._state.backtracking == 0:
                            stream_LT.add(LT85)


                    else:
                        break #loop41
                # ../src/checkjs/parsers/antlr/JavaScript.g:137:19: ( initialiserNoIn )?
                alt42 = 2
                LA42_0 = self.input.LA(1)

                if (LA42_0 == 60) :
                    alt42 = 1
                if alt42 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: initialiserNoIn
                    pass 
                    self._state.following.append(self.FOLLOW_initialiserNoIn_in_variableDeclarationNoIn719)
                    initialiserNoIn86 = self.initialiserNoIn()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_initialiserNoIn.add(initialiserNoIn86.tree)




                # AST Rewrite
                # elements: Identifier, initialiserNoIn
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 137:36: -> ^( VARIABLE_DECL Identifier initialiserNoIn )
                    # ../src/checkjs/parsers/antlr/JavaScript.g:138:9: ^( VARIABLE_DECL Identifier initialiserNoIn )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VARIABLE_DECL, "VARIABLE_DECL"), root_1)

                    self._adaptor.addChild(root_1, stream_Identifier.nextNode())
                    self._adaptor.addChild(root_1, stream_initialiserNoIn.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 16, variableDeclarationNoIn_StartIndex, success)

            pass
        return retval

    # $ANTLR end "variableDeclarationNoIn"

    class initialiser_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.initialiser_return, self).__init__()

            self.tree = None




    # $ANTLR start "initialiser"
    # ../src/checkjs/parsers/antlr/JavaScript.g:141:1: initialiser : '=' ( LT )* assignmentExpression ;
    def initialiser(self, ):

        retval = self.initialiser_return()
        retval.start = self.input.LT(1)
        initialiser_StartIndex = self.input.index()
        root_0 = None

        char_literal87 = None
        LT88 = None
        assignmentExpression89 = None


        char_literal87_tree = None
        LT88_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 17):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:142:2: ( '=' ( LT )* assignmentExpression )
                # ../src/checkjs/parsers/antlr/JavaScript.g:142:4: '=' ( LT )* assignmentExpression
                pass 
                root_0 = self._adaptor.nil()

                char_literal87=self.match(self.input, 60, self.FOLLOW_60_in_initialiser750)
                # ../src/checkjs/parsers/antlr/JavaScript.g:142:11: ( LT )*
                while True: #loop43
                    alt43 = 2
                    LA43_0 = self.input.LA(1)

                    if (LA43_0 == LT) :
                        alt43 = 1


                    if alt43 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT88=self.match(self.input, LT, self.FOLLOW_LT_in_initialiser753)


                    else:
                        break #loop43
                self._state.following.append(self.FOLLOW_assignmentExpression_in_initialiser757)
                assignmentExpression89 = self.assignmentExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, assignmentExpression89.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 17, initialiser_StartIndex, success)

            pass
        return retval

    # $ANTLR end "initialiser"

    class initialiserNoIn_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.initialiserNoIn_return, self).__init__()

            self.tree = None




    # $ANTLR start "initialiserNoIn"
    # ../src/checkjs/parsers/antlr/JavaScript.g:145:1: initialiserNoIn : '=' ( LT )* assignmentExpressionNoIn ;
    def initialiserNoIn(self, ):

        retval = self.initialiserNoIn_return()
        retval.start = self.input.LT(1)
        initialiserNoIn_StartIndex = self.input.index()
        root_0 = None

        char_literal90 = None
        LT91 = None
        assignmentExpressionNoIn92 = None


        char_literal90_tree = None
        LT91_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 18):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:146:2: ( '=' ( LT )* assignmentExpressionNoIn )
                # ../src/checkjs/parsers/antlr/JavaScript.g:146:4: '=' ( LT )* assignmentExpressionNoIn
                pass 
                root_0 = self._adaptor.nil()

                char_literal90=self.match(self.input, 60, self.FOLLOW_60_in_initialiserNoIn768)
                # ../src/checkjs/parsers/antlr/JavaScript.g:146:11: ( LT )*
                while True: #loop44
                    alt44 = 2
                    LA44_0 = self.input.LA(1)

                    if (LA44_0 == LT) :
                        alt44 = 1


                    if alt44 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT91=self.match(self.input, LT, self.FOLLOW_LT_in_initialiserNoIn771)


                    else:
                        break #loop44
                self._state.following.append(self.FOLLOW_assignmentExpressionNoIn_in_initialiserNoIn775)
                assignmentExpressionNoIn92 = self.assignmentExpressionNoIn()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, assignmentExpressionNoIn92.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 18, initialiserNoIn_StartIndex, success)

            pass
        return retval

    # $ANTLR end "initialiserNoIn"

    class emptyStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.emptyStatement_return, self).__init__()

            self.tree = None




    # $ANTLR start "emptyStatement"
    # ../src/checkjs/parsers/antlr/JavaScript.g:149:1: emptyStatement : ';' ;
    def emptyStatement(self, ):

        retval = self.emptyStatement_return()
        retval.start = self.input.LT(1)
        emptyStatement_StartIndex = self.input.index()
        root_0 = None

        char_literal93 = None

        char_literal93_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 19):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:150:2: ( ';' )
                # ../src/checkjs/parsers/antlr/JavaScript.g:150:4: ';'
                pass 
                root_0 = self._adaptor.nil()

                char_literal93=self.match(self.input, 53, self.FOLLOW_53_in_emptyStatement786)
                if self._state.backtracking == 0:

                    char_literal93_tree = self._adaptor.createWithPayload(char_literal93)
                    self._adaptor.addChild(root_0, char_literal93_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 19, emptyStatement_StartIndex, success)

            pass
        return retval

    # $ANTLR end "emptyStatement"

    class expressionStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.expressionStatement_return, self).__init__()

            self.tree = None




    # $ANTLR start "expressionStatement"
    # ../src/checkjs/parsers/antlr/JavaScript.g:153:1: expressionStatement : expression ( LT )* ';' ;
    def expressionStatement(self, ):

        retval = self.expressionStatement_return()
        retval.start = self.input.LT(1)
        expressionStatement_StartIndex = self.input.index()
        root_0 = None

        LT95 = None
        char_literal96 = None
        expression94 = None


        LT95_tree = None
        char_literal96_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 20):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:154:2: ( expression ( LT )* ';' )
                # ../src/checkjs/parsers/antlr/JavaScript.g:154:4: expression ( LT )* ';'
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_expression_in_expressionStatement797)
                expression94 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expression94.tree)
                # ../src/checkjs/parsers/antlr/JavaScript.g:154:17: ( LT )*
                while True: #loop45
                    alt45 = 2
                    LA45_0 = self.input.LA(1)

                    if (LA45_0 == LT) :
                        alt45 = 1


                    if alt45 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT95=self.match(self.input, LT, self.FOLLOW_LT_in_expressionStatement799)


                    else:
                        break #loop45
                char_literal96=self.match(self.input, 53, self.FOLLOW_53_in_expressionStatement803)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 20, expressionStatement_StartIndex, success)

            pass
        return retval

    # $ANTLR end "expressionStatement"

    class ifStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.ifStatement_return, self).__init__()

            self.tree = None




    # $ANTLR start "ifStatement"
    # ../src/checkjs/parsers/antlr/JavaScript.g:157:1: ifStatement : 'if' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* ( statement | statementBlock ) ( ( LT )* 'else' ( LT )* ( statement | statementBlock ) )? ;
    def ifStatement(self, ):

        retval = self.ifStatement_return()
        retval.start = self.input.LT(1)
        ifStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal97 = None
        LT98 = None
        char_literal99 = None
        LT100 = None
        LT102 = None
        char_literal103 = None
        LT104 = None
        LT107 = None
        string_literal108 = None
        LT109 = None
        expression101 = None

        statement105 = None

        statementBlock106 = None

        statement110 = None

        statementBlock111 = None


        string_literal97_tree = None
        LT98_tree = None
        char_literal99_tree = None
        LT100_tree = None
        LT102_tree = None
        char_literal103_tree = None
        LT104_tree = None
        LT107_tree = None
        string_literal108_tree = None
        LT109_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 21):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:158:2: ( 'if' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* ( statement | statementBlock ) ( ( LT )* 'else' ( LT )* ( statement | statementBlock ) )? )
                # ../src/checkjs/parsers/antlr/JavaScript.g:158:4: 'if' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* ( statement | statementBlock ) ( ( LT )* 'else' ( LT )* ( statement | statementBlock ) )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal97=self.match(self.input, 61, self.FOLLOW_61_in_ifStatement815)
                if self._state.backtracking == 0:

                    string_literal97_tree = self._adaptor.createWithPayload(string_literal97)
                    self._adaptor.addChild(root_0, string_literal97_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:158:11: ( LT )*
                while True: #loop46
                    alt46 = 2
                    LA46_0 = self.input.LA(1)

                    if (LA46_0 == LT) :
                        alt46 = 1


                    if alt46 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT98=self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement817)


                    else:
                        break #loop46
                char_literal99=self.match(self.input, 54, self.FOLLOW_54_in_ifStatement821)
                if self._state.backtracking == 0:

                    char_literal99_tree = self._adaptor.createWithPayload(char_literal99)
                    self._adaptor.addChild(root_0, char_literal99_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:158:20: ( LT )*
                while True: #loop47
                    alt47 = 2
                    LA47_0 = self.input.LA(1)

                    if (LA47_0 == LT) :
                        alt47 = 1


                    if alt47 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT100=self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement823)


                    else:
                        break #loop47
                self._state.following.append(self.FOLLOW_expression_in_ifStatement827)
                expression101 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expression101.tree)
                # ../src/checkjs/parsers/antlr/JavaScript.g:158:36: ( LT )*
                while True: #loop48
                    alt48 = 2
                    LA48_0 = self.input.LA(1)

                    if (LA48_0 == LT) :
                        alt48 = 1


                    if alt48 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT102=self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement829)


                    else:
                        break #loop48
                char_literal103=self.match(self.input, 56, self.FOLLOW_56_in_ifStatement833)
                if self._state.backtracking == 0:

                    char_literal103_tree = self._adaptor.createWithPayload(char_literal103)
                    self._adaptor.addChild(root_0, char_literal103_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:158:45: ( LT )*
                while True: #loop49
                    alt49 = 2
                    LA49_0 = self.input.LA(1)

                    if (LA49_0 == LT) :
                        alt49 = 1


                    if alt49 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT104=self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement835)


                    else:
                        break #loop49
                # ../src/checkjs/parsers/antlr/JavaScript.g:158:48: ( statement | statementBlock )
                alt50 = 2
                alt50 = self.dfa50.predict(self.input)
                if alt50 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:158:49: statement
                    pass 
                    self._state.following.append(self.FOLLOW_statement_in_ifStatement840)
                    statement105 = self.statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, statement105.tree)


                elif alt50 == 2:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:158:61: statementBlock
                    pass 
                    self._state.following.append(self.FOLLOW_statementBlock_in_ifStatement844)
                    statementBlock106 = self.statementBlock()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, statementBlock106.tree)



                # ../src/checkjs/parsers/antlr/JavaScript.g:158:77: ( ( LT )* 'else' ( LT )* ( statement | statementBlock ) )?
                alt54 = 2
                LA54_0 = self.input.LA(1)

                if (LA54_0 == LT) :
                    LA54_1 = self.input.LA(2)

                    if (self.synpred64_JavaScript()) :
                        alt54 = 1
                elif (LA54_0 == 62) :
                    LA54_2 = self.input.LA(2)

                    if (self.synpred64_JavaScript()) :
                        alt54 = 1
                if alt54 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:158:78: ( LT )* 'else' ( LT )* ( statement | statementBlock )
                    pass 
                    # ../src/checkjs/parsers/antlr/JavaScript.g:158:80: ( LT )*
                    while True: #loop51
                        alt51 = 2
                        LA51_0 = self.input.LA(1)

                        if (LA51_0 == LT) :
                            alt51 = 1


                        if alt51 == 1:
                            # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                            pass 
                            LT107=self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement848)


                        else:
                            break #loop51
                    string_literal108=self.match(self.input, 62, self.FOLLOW_62_in_ifStatement852)
                    if self._state.backtracking == 0:

                        string_literal108_tree = self._adaptor.createWithPayload(string_literal108)
                        self._adaptor.addChild(root_0, string_literal108_tree)

                    # ../src/checkjs/parsers/antlr/JavaScript.g:158:92: ( LT )*
                    while True: #loop52
                        alt52 = 2
                        LA52_0 = self.input.LA(1)

                        if (LA52_0 == LT) :
                            alt52 = 1


                        if alt52 == 1:
                            # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                            pass 
                            LT109=self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement854)


                        else:
                            break #loop52
                    # ../src/checkjs/parsers/antlr/JavaScript.g:158:95: ( statement | statementBlock )
                    alt53 = 2
                    alt53 = self.dfa53.predict(self.input)
                    if alt53 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:158:96: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_ifStatement859)
                        statement110 = self.statement()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, statement110.tree)


                    elif alt53 == 2:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:158:108: statementBlock
                        pass 
                        self._state.following.append(self.FOLLOW_statementBlock_in_ifStatement863)
                        statementBlock111 = self.statementBlock()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, statementBlock111.tree)









                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 21, ifStatement_StartIndex, success)

            pass
        return retval

    # $ANTLR end "ifStatement"

    class iterationStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.iterationStatement_return, self).__init__()

            self.tree = None




    # $ANTLR start "iterationStatement"
    # ../src/checkjs/parsers/antlr/JavaScript.g:161:1: iterationStatement : ( doWhileStatement | whileStatement | forStatement | forInStatement );
    def iterationStatement(self, ):

        retval = self.iterationStatement_return()
        retval.start = self.input.LT(1)
        iterationStatement_StartIndex = self.input.index()
        root_0 = None

        doWhileStatement112 = None

        whileStatement113 = None

        forStatement114 = None

        forInStatement115 = None



        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 22):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:162:2: ( doWhileStatement | whileStatement | forStatement | forInStatement )
                alt55 = 4
                LA55 = self.input.LA(1)
                if LA55 == 63:
                    alt55 = 1
                elif LA55 == 64:
                    alt55 = 2
                elif LA55 == 65:
                    LA55_3 = self.input.LA(2)

                    if (self.synpred67_JavaScript()) :
                        alt55 = 3
                    elif (True) :
                        alt55 = 4
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 55, 3, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 55, 0, self.input)

                    raise nvae

                if alt55 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:162:4: doWhileStatement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_doWhileStatement_in_iterationStatement877)
                    doWhileStatement112 = self.doWhileStatement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, doWhileStatement112.tree)


                elif alt55 == 2:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:163:4: whileStatement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_whileStatement_in_iterationStatement882)
                    whileStatement113 = self.whileStatement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, whileStatement113.tree)


                elif alt55 == 3:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:164:4: forStatement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_forStatement_in_iterationStatement887)
                    forStatement114 = self.forStatement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, forStatement114.tree)


                elif alt55 == 4:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:165:4: forInStatement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_forInStatement_in_iterationStatement892)
                    forInStatement115 = self.forInStatement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, forInStatement115.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 22, iterationStatement_StartIndex, success)

            pass
        return retval

    # $ANTLR end "iterationStatement"

    class doWhileStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.doWhileStatement_return, self).__init__()

            self.tree = None




    # $ANTLR start "doWhileStatement"
    # ../src/checkjs/parsers/antlr/JavaScript.g:168:1: doWhileStatement : 'do' ( LT )* ( statement | statementBlock ) ( LT )* 'while' ( LT )* '(' expression ')' ( LT )* ';' ;
    def doWhileStatement(self, ):

        retval = self.doWhileStatement_return()
        retval.start = self.input.LT(1)
        doWhileStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal116 = None
        LT117 = None
        LT120 = None
        string_literal121 = None
        LT122 = None
        char_literal123 = None
        char_literal125 = None
        LT126 = None
        char_literal127 = None
        statement118 = None

        statementBlock119 = None

        expression124 = None


        string_literal116_tree = None
        LT117_tree = None
        LT120_tree = None
        string_literal121_tree = None
        LT122_tree = None
        char_literal123_tree = None
        char_literal125_tree = None
        LT126_tree = None
        char_literal127_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 23):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:169:2: ( 'do' ( LT )* ( statement | statementBlock ) ( LT )* 'while' ( LT )* '(' expression ')' ( LT )* ';' )
                # ../src/checkjs/parsers/antlr/JavaScript.g:169:4: 'do' ( LT )* ( statement | statementBlock ) ( LT )* 'while' ( LT )* '(' expression ')' ( LT )* ';'
                pass 
                root_0 = self._adaptor.nil()

                string_literal116=self.match(self.input, 63, self.FOLLOW_63_in_doWhileStatement903)
                if self._state.backtracking == 0:

                    string_literal116_tree = self._adaptor.createWithPayload(string_literal116)
                    self._adaptor.addChild(root_0, string_literal116_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:169:11: ( LT )*
                while True: #loop56
                    alt56 = 2
                    LA56_0 = self.input.LA(1)

                    if (LA56_0 == LT) :
                        alt56 = 1


                    if alt56 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT117=self.match(self.input, LT, self.FOLLOW_LT_in_doWhileStatement905)


                    else:
                        break #loop56
                # ../src/checkjs/parsers/antlr/JavaScript.g:169:14: ( statement | statementBlock )
                alt57 = 2
                alt57 = self.dfa57.predict(self.input)
                if alt57 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:169:15: statement
                    pass 
                    self._state.following.append(self.FOLLOW_statement_in_doWhileStatement910)
                    statement118 = self.statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, statement118.tree)


                elif alt57 == 2:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:169:27: statementBlock
                    pass 
                    self._state.following.append(self.FOLLOW_statementBlock_in_doWhileStatement914)
                    statementBlock119 = self.statementBlock()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, statementBlock119.tree)



                # ../src/checkjs/parsers/antlr/JavaScript.g:169:45: ( LT )*
                while True: #loop58
                    alt58 = 2
                    LA58_0 = self.input.LA(1)

                    if (LA58_0 == LT) :
                        alt58 = 1


                    if alt58 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT120=self.match(self.input, LT, self.FOLLOW_LT_in_doWhileStatement917)


                    else:
                        break #loop58
                string_literal121=self.match(self.input, 64, self.FOLLOW_64_in_doWhileStatement921)
                if self._state.backtracking == 0:

                    string_literal121_tree = self._adaptor.createWithPayload(string_literal121)
                    self._adaptor.addChild(root_0, string_literal121_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:169:58: ( LT )*
                while True: #loop59
                    alt59 = 2
                    LA59_0 = self.input.LA(1)

                    if (LA59_0 == LT) :
                        alt59 = 1


                    if alt59 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT122=self.match(self.input, LT, self.FOLLOW_LT_in_doWhileStatement923)


                    else:
                        break #loop59
                char_literal123=self.match(self.input, 54, self.FOLLOW_54_in_doWhileStatement927)
                if self._state.backtracking == 0:

                    char_literal123_tree = self._adaptor.createWithPayload(char_literal123)
                    self._adaptor.addChild(root_0, char_literal123_tree)

                self._state.following.append(self.FOLLOW_expression_in_doWhileStatement929)
                expression124 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expression124.tree)
                char_literal125=self.match(self.input, 56, self.FOLLOW_56_in_doWhileStatement931)
                if self._state.backtracking == 0:

                    char_literal125_tree = self._adaptor.createWithPayload(char_literal125)
                    self._adaptor.addChild(root_0, char_literal125_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:169:82: ( LT )*
                while True: #loop60
                    alt60 = 2
                    LA60_0 = self.input.LA(1)

                    if (LA60_0 == LT) :
                        alt60 = 1


                    if alt60 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT126=self.match(self.input, LT, self.FOLLOW_LT_in_doWhileStatement933)


                    else:
                        break #loop60
                char_literal127=self.match(self.input, 53, self.FOLLOW_53_in_doWhileStatement937)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 23, doWhileStatement_StartIndex, success)

            pass
        return retval

    # $ANTLR end "doWhileStatement"

    class whileStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.whileStatement_return, self).__init__()

            self.tree = None




    # $ANTLR start "whileStatement"
    # ../src/checkjs/parsers/antlr/JavaScript.g:172:1: whileStatement : 'while' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* ( statement | statementBlock ) ;
    def whileStatement(self, ):

        retval = self.whileStatement_return()
        retval.start = self.input.LT(1)
        whileStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal128 = None
        LT129 = None
        char_literal130 = None
        LT131 = None
        LT133 = None
        char_literal134 = None
        LT135 = None
        expression132 = None

        statement136 = None

        statementBlock137 = None


        string_literal128_tree = None
        LT129_tree = None
        char_literal130_tree = None
        LT131_tree = None
        LT133_tree = None
        char_literal134_tree = None
        LT135_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 24):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:173:2: ( 'while' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* ( statement | statementBlock ) )
                # ../src/checkjs/parsers/antlr/JavaScript.g:173:4: 'while' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* ( statement | statementBlock )
                pass 
                root_0 = self._adaptor.nil()

                string_literal128=self.match(self.input, 64, self.FOLLOW_64_in_whileStatement949)
                if self._state.backtracking == 0:

                    string_literal128_tree = self._adaptor.createWithPayload(string_literal128)
                    self._adaptor.addChild(root_0, string_literal128_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:173:14: ( LT )*
                while True: #loop61
                    alt61 = 2
                    LA61_0 = self.input.LA(1)

                    if (LA61_0 == LT) :
                        alt61 = 1


                    if alt61 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT129=self.match(self.input, LT, self.FOLLOW_LT_in_whileStatement951)


                    else:
                        break #loop61
                char_literal130=self.match(self.input, 54, self.FOLLOW_54_in_whileStatement955)
                if self._state.backtracking == 0:

                    char_literal130_tree = self._adaptor.createWithPayload(char_literal130)
                    self._adaptor.addChild(root_0, char_literal130_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:173:23: ( LT )*
                while True: #loop62
                    alt62 = 2
                    LA62_0 = self.input.LA(1)

                    if (LA62_0 == LT) :
                        alt62 = 1


                    if alt62 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT131=self.match(self.input, LT, self.FOLLOW_LT_in_whileStatement957)


                    else:
                        break #loop62
                self._state.following.append(self.FOLLOW_expression_in_whileStatement961)
                expression132 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expression132.tree)
                # ../src/checkjs/parsers/antlr/JavaScript.g:173:39: ( LT )*
                while True: #loop63
                    alt63 = 2
                    LA63_0 = self.input.LA(1)

                    if (LA63_0 == LT) :
                        alt63 = 1


                    if alt63 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT133=self.match(self.input, LT, self.FOLLOW_LT_in_whileStatement963)


                    else:
                        break #loop63
                char_literal134=self.match(self.input, 56, self.FOLLOW_56_in_whileStatement967)
                if self._state.backtracking == 0:

                    char_literal134_tree = self._adaptor.createWithPayload(char_literal134)
                    self._adaptor.addChild(root_0, char_literal134_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:173:48: ( LT )*
                while True: #loop64
                    alt64 = 2
                    LA64_0 = self.input.LA(1)

                    if (LA64_0 == LT) :
                        alt64 = 1


                    if alt64 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT135=self.match(self.input, LT, self.FOLLOW_LT_in_whileStatement969)


                    else:
                        break #loop64
                # ../src/checkjs/parsers/antlr/JavaScript.g:173:51: ( statement | statementBlock )
                alt65 = 2
                alt65 = self.dfa65.predict(self.input)
                if alt65 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:173:52: statement
                    pass 
                    self._state.following.append(self.FOLLOW_statement_in_whileStatement974)
                    statement136 = self.statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, statement136.tree)


                elif alt65 == 2:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:173:64: statementBlock
                    pass 
                    self._state.following.append(self.FOLLOW_statementBlock_in_whileStatement978)
                    statementBlock137 = self.statementBlock()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, statementBlock137.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 24, whileStatement_StartIndex, success)

            pass
        return retval

    # $ANTLR end "whileStatement"

    class forStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.forStatement_return, self).__init__()

            self.tree = None




    # $ANTLR start "forStatement"
    # ../src/checkjs/parsers/antlr/JavaScript.g:176:1: forStatement : 'for' ( LT )* '(' ( ( LT )* forStatementInitialiserPart )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ')' ( LT )* ( statement | statementBlock ) ;
    def forStatement(self, ):

        retval = self.forStatement_return()
        retval.start = self.input.LT(1)
        forStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal138 = None
        LT139 = None
        char_literal140 = None
        LT141 = None
        LT143 = None
        char_literal144 = None
        LT145 = None
        LT147 = None
        char_literal148 = None
        LT149 = None
        LT151 = None
        char_literal152 = None
        LT153 = None
        forStatementInitialiserPart142 = None

        expression146 = None

        expression150 = None

        statement154 = None

        statementBlock155 = None


        string_literal138_tree = None
        LT139_tree = None
        char_literal140_tree = None
        LT141_tree = None
        LT143_tree = None
        char_literal144_tree = None
        LT145_tree = None
        LT147_tree = None
        char_literal148_tree = None
        LT149_tree = None
        LT151_tree = None
        char_literal152_tree = None
        LT153_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 25):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:177:2: ( 'for' ( LT )* '(' ( ( LT )* forStatementInitialiserPart )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ')' ( LT )* ( statement | statementBlock ) )
                # ../src/checkjs/parsers/antlr/JavaScript.g:177:4: 'for' ( LT )* '(' ( ( LT )* forStatementInitialiserPart )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ')' ( LT )* ( statement | statementBlock )
                pass 
                root_0 = self._adaptor.nil()

                string_literal138=self.match(self.input, 65, self.FOLLOW_65_in_forStatement990)
                if self._state.backtracking == 0:

                    string_literal138_tree = self._adaptor.createWithPayload(string_literal138)
                    self._adaptor.addChild(root_0, string_literal138_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:177:12: ( LT )*
                while True: #loop66
                    alt66 = 2
                    LA66_0 = self.input.LA(1)

                    if (LA66_0 == LT) :
                        alt66 = 1


                    if alt66 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT139=self.match(self.input, LT, self.FOLLOW_LT_in_forStatement992)


                    else:
                        break #loop66
                char_literal140=self.match(self.input, 54, self.FOLLOW_54_in_forStatement996)
                if self._state.backtracking == 0:

                    char_literal140_tree = self._adaptor.createWithPayload(char_literal140)
                    self._adaptor.addChild(root_0, char_literal140_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:177:19: ( ( LT )* forStatementInitialiserPart )?
                alt68 = 2
                alt68 = self.dfa68.predict(self.input)
                if alt68 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:177:20: ( LT )* forStatementInitialiserPart
                    pass 
                    # ../src/checkjs/parsers/antlr/JavaScript.g:177:22: ( LT )*
                    while True: #loop67
                        alt67 = 2
                        LA67_0 = self.input.LA(1)

                        if (LA67_0 == LT) :
                            alt67 = 1


                        if alt67 == 1:
                            # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                            pass 
                            LT141=self.match(self.input, LT, self.FOLLOW_LT_in_forStatement999)


                        else:
                            break #loop67
                    self._state.following.append(self.FOLLOW_forStatementInitialiserPart_in_forStatement1003)
                    forStatementInitialiserPart142 = self.forStatementInitialiserPart()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, forStatementInitialiserPart142.tree)



                # ../src/checkjs/parsers/antlr/JavaScript.g:177:57: ( LT )*
                while True: #loop69
                    alt69 = 2
                    LA69_0 = self.input.LA(1)

                    if (LA69_0 == LT) :
                        alt69 = 1


                    if alt69 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT143=self.match(self.input, LT, self.FOLLOW_LT_in_forStatement1007)


                    else:
                        break #loop69
                char_literal144=self.match(self.input, 53, self.FOLLOW_53_in_forStatement1011)
                # ../src/checkjs/parsers/antlr/JavaScript.g:177:65: ( ( LT )* expression )?
                alt71 = 2
                alt71 = self.dfa71.predict(self.input)
                if alt71 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:177:66: ( LT )* expression
                    pass 
                    # ../src/checkjs/parsers/antlr/JavaScript.g:177:68: ( LT )*
                    while True: #loop70
                        alt70 = 2
                        LA70_0 = self.input.LA(1)

                        if (LA70_0 == LT) :
                            alt70 = 1


                        if alt70 == 1:
                            # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                            pass 
                            LT145=self.match(self.input, LT, self.FOLLOW_LT_in_forStatement1015)


                        else:
                            break #loop70
                    self._state.following.append(self.FOLLOW_expression_in_forStatement1019)
                    expression146 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression146.tree)



                # ../src/checkjs/parsers/antlr/JavaScript.g:177:86: ( LT )*
                while True: #loop72
                    alt72 = 2
                    LA72_0 = self.input.LA(1)

                    if (LA72_0 == LT) :
                        alt72 = 1


                    if alt72 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT147=self.match(self.input, LT, self.FOLLOW_LT_in_forStatement1023)


                    else:
                        break #loop72
                char_literal148=self.match(self.input, 53, self.FOLLOW_53_in_forStatement1027)
                # ../src/checkjs/parsers/antlr/JavaScript.g:177:94: ( ( LT )* expression )?
                alt74 = 2
                alt74 = self.dfa74.predict(self.input)
                if alt74 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:177:95: ( LT )* expression
                    pass 
                    # ../src/checkjs/parsers/antlr/JavaScript.g:177:97: ( LT )*
                    while True: #loop73
                        alt73 = 2
                        LA73_0 = self.input.LA(1)

                        if (LA73_0 == LT) :
                            alt73 = 1


                        if alt73 == 1:
                            # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                            pass 
                            LT149=self.match(self.input, LT, self.FOLLOW_LT_in_forStatement1031)


                        else:
                            break #loop73
                    self._state.following.append(self.FOLLOW_expression_in_forStatement1035)
                    expression150 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression150.tree)



                # ../src/checkjs/parsers/antlr/JavaScript.g:177:115: ( LT )*
                while True: #loop75
                    alt75 = 2
                    LA75_0 = self.input.LA(1)

                    if (LA75_0 == LT) :
                        alt75 = 1


                    if alt75 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT151=self.match(self.input, LT, self.FOLLOW_LT_in_forStatement1039)


                    else:
                        break #loop75
                char_literal152=self.match(self.input, 56, self.FOLLOW_56_in_forStatement1043)
                if self._state.backtracking == 0:

                    char_literal152_tree = self._adaptor.createWithPayload(char_literal152)
                    self._adaptor.addChild(root_0, char_literal152_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:177:124: ( LT )*
                while True: #loop76
                    alt76 = 2
                    LA76_0 = self.input.LA(1)

                    if (LA76_0 == LT) :
                        alt76 = 1


                    if alt76 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT153=self.match(self.input, LT, self.FOLLOW_LT_in_forStatement1045)


                    else:
                        break #loop76
                # ../src/checkjs/parsers/antlr/JavaScript.g:177:127: ( statement | statementBlock )
                alt77 = 2
                alt77 = self.dfa77.predict(self.input)
                if alt77 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:177:128: statement
                    pass 
                    self._state.following.append(self.FOLLOW_statement_in_forStatement1050)
                    statement154 = self.statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, statement154.tree)


                elif alt77 == 2:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:177:140: statementBlock
                    pass 
                    self._state.following.append(self.FOLLOW_statementBlock_in_forStatement1054)
                    statementBlock155 = self.statementBlock()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, statementBlock155.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 25, forStatement_StartIndex, success)

            pass
        return retval

    # $ANTLR end "forStatement"

    class forStatementInitialiserPart_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.forStatementInitialiserPart_return, self).__init__()

            self.tree = None




    # $ANTLR start "forStatementInitialiserPart"
    # ../src/checkjs/parsers/antlr/JavaScript.g:180:1: forStatementInitialiserPart : ( expressionNoIn | 'var' ( LT )* variableDeclarationListNoIn );
    def forStatementInitialiserPart(self, ):

        retval = self.forStatementInitialiserPart_return()
        retval.start = self.input.LT(1)
        forStatementInitialiserPart_StartIndex = self.input.index()
        root_0 = None

        string_literal157 = None
        LT158 = None
        expressionNoIn156 = None

        variableDeclarationListNoIn159 = None


        string_literal157_tree = None
        LT158_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 26):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:181:2: ( expressionNoIn | 'var' ( LT )* variableDeclarationListNoIn )
                alt79 = 2
                LA79_0 = self.input.LA(1)

                if ((Identifier <= LA79_0 <= NumericLiteral) or LA79_0 == 52 or LA79_0 == 54 or LA79_0 == 57 or (79 <= LA79_0 <= 80) or (96 <= LA79_0 <= 97) or (108 <= LA79_0 <= 119)) :
                    alt79 = 1
                elif (LA79_0 == 59) :
                    alt79 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 79, 0, self.input)

                    raise nvae

                if alt79 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:181:4: expressionNoIn
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_expressionNoIn_in_forStatementInitialiserPart1066)
                    expressionNoIn156 = self.expressionNoIn()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expressionNoIn156.tree)


                elif alt79 == 2:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:182:4: 'var' ( LT )* variableDeclarationListNoIn
                    pass 
                    root_0 = self._adaptor.nil()

                    string_literal157=self.match(self.input, 59, self.FOLLOW_59_in_forStatementInitialiserPart1071)
                    if self._state.backtracking == 0:

                        string_literal157_tree = self._adaptor.createWithPayload(string_literal157)
                        self._adaptor.addChild(root_0, string_literal157_tree)

                    # ../src/checkjs/parsers/antlr/JavaScript.g:182:12: ( LT )*
                    while True: #loop78
                        alt78 = 2
                        LA78_0 = self.input.LA(1)

                        if (LA78_0 == LT) :
                            alt78 = 1


                        if alt78 == 1:
                            # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                            pass 
                            LT158=self.match(self.input, LT, self.FOLLOW_LT_in_forStatementInitialiserPart1073)


                        else:
                            break #loop78
                    self._state.following.append(self.FOLLOW_variableDeclarationListNoIn_in_forStatementInitialiserPart1077)
                    variableDeclarationListNoIn159 = self.variableDeclarationListNoIn()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, variableDeclarationListNoIn159.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 26, forStatementInitialiserPart_StartIndex, success)

            pass
        return retval

    # $ANTLR end "forStatementInitialiserPart"

    class forInStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.forInStatement_return, self).__init__()

            self.tree = None




    # $ANTLR start "forInStatement"
    # ../src/checkjs/parsers/antlr/JavaScript.g:185:1: forInStatement : 'for' ( LT )* '(' ( LT )* forInStatementInitialiserPart ( LT )* 'in' ( LT )* expression ( LT )* ')' ( LT )* ( statement | statementBlock ) ;
    def forInStatement(self, ):

        retval = self.forInStatement_return()
        retval.start = self.input.LT(1)
        forInStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal160 = None
        LT161 = None
        char_literal162 = None
        LT163 = None
        LT165 = None
        string_literal166 = None
        LT167 = None
        LT169 = None
        char_literal170 = None
        LT171 = None
        forInStatementInitialiserPart164 = None

        expression168 = None

        statement172 = None

        statementBlock173 = None


        string_literal160_tree = None
        LT161_tree = None
        char_literal162_tree = None
        LT163_tree = None
        LT165_tree = None
        string_literal166_tree = None
        LT167_tree = None
        LT169_tree = None
        char_literal170_tree = None
        LT171_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 27):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:186:2: ( 'for' ( LT )* '(' ( LT )* forInStatementInitialiserPart ( LT )* 'in' ( LT )* expression ( LT )* ')' ( LT )* ( statement | statementBlock ) )
                # ../src/checkjs/parsers/antlr/JavaScript.g:186:4: 'for' ( LT )* '(' ( LT )* forInStatementInitialiserPart ( LT )* 'in' ( LT )* expression ( LT )* ')' ( LT )* ( statement | statementBlock )
                pass 
                root_0 = self._adaptor.nil()

                string_literal160=self.match(self.input, 65, self.FOLLOW_65_in_forInStatement1088)
                if self._state.backtracking == 0:

                    string_literal160_tree = self._adaptor.createWithPayload(string_literal160)
                    self._adaptor.addChild(root_0, string_literal160_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:186:12: ( LT )*
                while True: #loop80
                    alt80 = 2
                    LA80_0 = self.input.LA(1)

                    if (LA80_0 == LT) :
                        alt80 = 1


                    if alt80 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT161=self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement1090)


                    else:
                        break #loop80
                char_literal162=self.match(self.input, 54, self.FOLLOW_54_in_forInStatement1094)
                if self._state.backtracking == 0:

                    char_literal162_tree = self._adaptor.createWithPayload(char_literal162)
                    self._adaptor.addChild(root_0, char_literal162_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:186:21: ( LT )*
                while True: #loop81
                    alt81 = 2
                    LA81_0 = self.input.LA(1)

                    if (LA81_0 == LT) :
                        alt81 = 1


                    if alt81 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT163=self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement1096)


                    else:
                        break #loop81
                self._state.following.append(self.FOLLOW_forInStatementInitialiserPart_in_forInStatement1100)
                forInStatementInitialiserPart164 = self.forInStatementInitialiserPart()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, forInStatementInitialiserPart164.tree)
                # ../src/checkjs/parsers/antlr/JavaScript.g:186:56: ( LT )*
                while True: #loop82
                    alt82 = 2
                    LA82_0 = self.input.LA(1)

                    if (LA82_0 == LT) :
                        alt82 = 1


                    if alt82 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT165=self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement1102)


                    else:
                        break #loop82
                string_literal166=self.match(self.input, 66, self.FOLLOW_66_in_forInStatement1106)
                if self._state.backtracking == 0:

                    string_literal166_tree = self._adaptor.createWithPayload(string_literal166)
                    self._adaptor.addChild(root_0, string_literal166_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:186:66: ( LT )*
                while True: #loop83
                    alt83 = 2
                    LA83_0 = self.input.LA(1)

                    if (LA83_0 == LT) :
                        alt83 = 1


                    if alt83 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT167=self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement1108)


                    else:
                        break #loop83
                self._state.following.append(self.FOLLOW_expression_in_forInStatement1112)
                expression168 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expression168.tree)
                # ../src/checkjs/parsers/antlr/JavaScript.g:186:82: ( LT )*
                while True: #loop84
                    alt84 = 2
                    LA84_0 = self.input.LA(1)

                    if (LA84_0 == LT) :
                        alt84 = 1


                    if alt84 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT169=self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement1114)


                    else:
                        break #loop84
                char_literal170=self.match(self.input, 56, self.FOLLOW_56_in_forInStatement1118)
                if self._state.backtracking == 0:

                    char_literal170_tree = self._adaptor.createWithPayload(char_literal170)
                    self._adaptor.addChild(root_0, char_literal170_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:186:91: ( LT )*
                while True: #loop85
                    alt85 = 2
                    LA85_0 = self.input.LA(1)

                    if (LA85_0 == LT) :
                        alt85 = 1


                    if alt85 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT171=self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement1120)


                    else:
                        break #loop85
                # ../src/checkjs/parsers/antlr/JavaScript.g:186:94: ( statement | statementBlock )
                alt86 = 2
                alt86 = self.dfa86.predict(self.input)
                if alt86 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:186:95: statement
                    pass 
                    self._state.following.append(self.FOLLOW_statement_in_forInStatement1125)
                    statement172 = self.statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, statement172.tree)


                elif alt86 == 2:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:186:107: statementBlock
                    pass 
                    self._state.following.append(self.FOLLOW_statementBlock_in_forInStatement1129)
                    statementBlock173 = self.statementBlock()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, statementBlock173.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 27, forInStatement_StartIndex, success)

            pass
        return retval

    # $ANTLR end "forInStatement"

    class forInStatementInitialiserPart_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.forInStatementInitialiserPart_return, self).__init__()

            self.tree = None




    # $ANTLR start "forInStatementInitialiserPart"
    # ../src/checkjs/parsers/antlr/JavaScript.g:189:1: forInStatementInitialiserPart : ( leftHandSideExpression | 'var' ( LT )* variableDeclarationNoIn );
    def forInStatementInitialiserPart(self, ):

        retval = self.forInStatementInitialiserPart_return()
        retval.start = self.input.LT(1)
        forInStatementInitialiserPart_StartIndex = self.input.index()
        root_0 = None

        string_literal175 = None
        LT176 = None
        leftHandSideExpression174 = None

        variableDeclarationNoIn177 = None


        string_literal175_tree = None
        LT176_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 28):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:190:2: ( leftHandSideExpression | 'var' ( LT )* variableDeclarationNoIn )
                alt88 = 2
                LA88_0 = self.input.LA(1)

                if ((Identifier <= LA88_0 <= NumericLiteral) or LA88_0 == 52 or LA88_0 == 54 or LA88_0 == 57 or (79 <= LA88_0 <= 80) or (115 <= LA88_0 <= 119)) :
                    alt88 = 1
                elif (LA88_0 == 59) :
                    alt88 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 88, 0, self.input)

                    raise nvae

                if alt88 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:190:4: leftHandSideExpression
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_leftHandSideExpression_in_forInStatementInitialiserPart1141)
                    leftHandSideExpression174 = self.leftHandSideExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, leftHandSideExpression174.tree)


                elif alt88 == 2:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:191:4: 'var' ( LT )* variableDeclarationNoIn
                    pass 
                    root_0 = self._adaptor.nil()

                    string_literal175=self.match(self.input, 59, self.FOLLOW_59_in_forInStatementInitialiserPart1146)
                    if self._state.backtracking == 0:

                        string_literal175_tree = self._adaptor.createWithPayload(string_literal175)
                        self._adaptor.addChild(root_0, string_literal175_tree)

                    # ../src/checkjs/parsers/antlr/JavaScript.g:191:12: ( LT )*
                    while True: #loop87
                        alt87 = 2
                        LA87_0 = self.input.LA(1)

                        if (LA87_0 == LT) :
                            alt87 = 1


                        if alt87 == 1:
                            # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                            pass 
                            LT176=self.match(self.input, LT, self.FOLLOW_LT_in_forInStatementInitialiserPart1148)


                        else:
                            break #loop87
                    self._state.following.append(self.FOLLOW_variableDeclarationNoIn_in_forInStatementInitialiserPart1152)
                    variableDeclarationNoIn177 = self.variableDeclarationNoIn()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, variableDeclarationNoIn177.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 28, forInStatementInitialiserPart_StartIndex, success)

            pass
        return retval

    # $ANTLR end "forInStatementInitialiserPart"

    class continueStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.continueStatement_return, self).__init__()

            self.tree = None




    # $ANTLR start "continueStatement"
    # ../src/checkjs/parsers/antlr/JavaScript.g:194:1: continueStatement : 'continue' ( Identifier )? ( LT )* ';' ;
    def continueStatement(self, ):

        retval = self.continueStatement_return()
        retval.start = self.input.LT(1)
        continueStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal178 = None
        Identifier179 = None
        LT180 = None
        char_literal181 = None

        string_literal178_tree = None
        Identifier179_tree = None
        LT180_tree = None
        char_literal181_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 29):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:195:2: ( 'continue' ( Identifier )? ( LT )* ';' )
                # ../src/checkjs/parsers/antlr/JavaScript.g:195:4: 'continue' ( Identifier )? ( LT )* ';'
                pass 
                root_0 = self._adaptor.nil()

                string_literal178=self.match(self.input, 67, self.FOLLOW_67_in_continueStatement1163)
                if self._state.backtracking == 0:

                    string_literal178_tree = self._adaptor.createWithPayload(string_literal178)
                    self._adaptor.addChild(root_0, string_literal178_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:195:15: ( Identifier )?
                alt89 = 2
                LA89_0 = self.input.LA(1)

                if (LA89_0 == Identifier) :
                    alt89 = 1
                if alt89 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: Identifier
                    pass 
                    Identifier179=self.match(self.input, Identifier, self.FOLLOW_Identifier_in_continueStatement1165)
                    if self._state.backtracking == 0:

                        Identifier179_tree = self._adaptor.createWithPayload(Identifier179)
                        self._adaptor.addChild(root_0, Identifier179_tree)




                # ../src/checkjs/parsers/antlr/JavaScript.g:195:29: ( LT )*
                while True: #loop90
                    alt90 = 2
                    LA90_0 = self.input.LA(1)

                    if (LA90_0 == LT) :
                        alt90 = 1


                    if alt90 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT180=self.match(self.input, LT, self.FOLLOW_LT_in_continueStatement1168)


                    else:
                        break #loop90
                char_literal181=self.match(self.input, 53, self.FOLLOW_53_in_continueStatement1172)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 29, continueStatement_StartIndex, success)

            pass
        return retval

    # $ANTLR end "continueStatement"

    class breakStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.breakStatement_return, self).__init__()

            self.tree = None




    # $ANTLR start "breakStatement"
    # ../src/checkjs/parsers/antlr/JavaScript.g:198:1: breakStatement : 'break' ( Identifier )? ( LT )* ';' ;
    def breakStatement(self, ):

        retval = self.breakStatement_return()
        retval.start = self.input.LT(1)
        breakStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal182 = None
        Identifier183 = None
        LT184 = None
        char_literal185 = None

        string_literal182_tree = None
        Identifier183_tree = None
        LT184_tree = None
        char_literal185_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 30):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:199:2: ( 'break' ( Identifier )? ( LT )* ';' )
                # ../src/checkjs/parsers/antlr/JavaScript.g:199:4: 'break' ( Identifier )? ( LT )* ';'
                pass 
                root_0 = self._adaptor.nil()

                string_literal182=self.match(self.input, 68, self.FOLLOW_68_in_breakStatement1184)
                if self._state.backtracking == 0:

                    string_literal182_tree = self._adaptor.createWithPayload(string_literal182)
                    self._adaptor.addChild(root_0, string_literal182_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:199:12: ( Identifier )?
                alt91 = 2
                LA91_0 = self.input.LA(1)

                if (LA91_0 == Identifier) :
                    alt91 = 1
                if alt91 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: Identifier
                    pass 
                    Identifier183=self.match(self.input, Identifier, self.FOLLOW_Identifier_in_breakStatement1186)
                    if self._state.backtracking == 0:

                        Identifier183_tree = self._adaptor.createWithPayload(Identifier183)
                        self._adaptor.addChild(root_0, Identifier183_tree)




                # ../src/checkjs/parsers/antlr/JavaScript.g:199:26: ( LT )*
                while True: #loop92
                    alt92 = 2
                    LA92_0 = self.input.LA(1)

                    if (LA92_0 == LT) :
                        alt92 = 1


                    if alt92 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT184=self.match(self.input, LT, self.FOLLOW_LT_in_breakStatement1189)


                    else:
                        break #loop92
                char_literal185=self.match(self.input, 53, self.FOLLOW_53_in_breakStatement1193)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 30, breakStatement_StartIndex, success)

            pass
        return retval

    # $ANTLR end "breakStatement"

    class returnStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.returnStatement_return, self).__init__()

            self.tree = None




    # $ANTLR start "returnStatement"
    # ../src/checkjs/parsers/antlr/JavaScript.g:202:1: returnStatement : 'return' ( expression )? ( LT )* ';' ;
    def returnStatement(self, ):

        retval = self.returnStatement_return()
        retval.start = self.input.LT(1)
        returnStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal186 = None
        LT188 = None
        char_literal189 = None
        expression187 = None


        string_literal186_tree = None
        LT188_tree = None
        char_literal189_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 31):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:203:2: ( 'return' ( expression )? ( LT )* ';' )
                # ../src/checkjs/parsers/antlr/JavaScript.g:203:4: 'return' ( expression )? ( LT )* ';'
                pass 
                root_0 = self._adaptor.nil()

                string_literal186=self.match(self.input, 69, self.FOLLOW_69_in_returnStatement1205)
                if self._state.backtracking == 0:

                    string_literal186_tree = self._adaptor.createWithPayload(string_literal186)
                    self._adaptor.addChild(root_0, string_literal186_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:203:13: ( expression )?
                alt93 = 2
                LA93_0 = self.input.LA(1)

                if ((Identifier <= LA93_0 <= NumericLiteral) or LA93_0 == 52 or LA93_0 == 54 or LA93_0 == 57 or (79 <= LA93_0 <= 80) or (96 <= LA93_0 <= 97) or (108 <= LA93_0 <= 119)) :
                    alt93 = 1
                if alt93 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: expression
                    pass 
                    self._state.following.append(self.FOLLOW_expression_in_returnStatement1207)
                    expression187 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression187.tree)



                # ../src/checkjs/parsers/antlr/JavaScript.g:203:27: ( LT )*
                while True: #loop94
                    alt94 = 2
                    LA94_0 = self.input.LA(1)

                    if (LA94_0 == LT) :
                        alt94 = 1


                    if alt94 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT188=self.match(self.input, LT, self.FOLLOW_LT_in_returnStatement1210)


                    else:
                        break #loop94
                char_literal189=self.match(self.input, 53, self.FOLLOW_53_in_returnStatement1214)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 31, returnStatement_StartIndex, success)

            pass
        return retval

    # $ANTLR end "returnStatement"

    class withStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.withStatement_return, self).__init__()

            self.tree = None




    # $ANTLR start "withStatement"
    # ../src/checkjs/parsers/antlr/JavaScript.g:206:1: withStatement : 'with' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* ( statement | statementBlock ) ;
    def withStatement(self, ):

        retval = self.withStatement_return()
        retval.start = self.input.LT(1)
        withStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal190 = None
        LT191 = None
        char_literal192 = None
        LT193 = None
        LT195 = None
        char_literal196 = None
        LT197 = None
        expression194 = None

        statement198 = None

        statementBlock199 = None


        string_literal190_tree = None
        LT191_tree = None
        char_literal192_tree = None
        LT193_tree = None
        LT195_tree = None
        char_literal196_tree = None
        LT197_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 32):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:207:2: ( 'with' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* ( statement | statementBlock ) )
                # ../src/checkjs/parsers/antlr/JavaScript.g:207:4: 'with' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* ( statement | statementBlock )
                pass 
                root_0 = self._adaptor.nil()

                string_literal190=self.match(self.input, 70, self.FOLLOW_70_in_withStatement1226)
                if self._state.backtracking == 0:

                    string_literal190_tree = self._adaptor.createWithPayload(string_literal190)
                    self._adaptor.addChild(root_0, string_literal190_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:207:13: ( LT )*
                while True: #loop95
                    alt95 = 2
                    LA95_0 = self.input.LA(1)

                    if (LA95_0 == LT) :
                        alt95 = 1


                    if alt95 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT191=self.match(self.input, LT, self.FOLLOW_LT_in_withStatement1228)


                    else:
                        break #loop95
                char_literal192=self.match(self.input, 54, self.FOLLOW_54_in_withStatement1232)
                if self._state.backtracking == 0:

                    char_literal192_tree = self._adaptor.createWithPayload(char_literal192)
                    self._adaptor.addChild(root_0, char_literal192_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:207:22: ( LT )*
                while True: #loop96
                    alt96 = 2
                    LA96_0 = self.input.LA(1)

                    if (LA96_0 == LT) :
                        alt96 = 1


                    if alt96 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT193=self.match(self.input, LT, self.FOLLOW_LT_in_withStatement1234)


                    else:
                        break #loop96
                self._state.following.append(self.FOLLOW_expression_in_withStatement1238)
                expression194 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expression194.tree)
                # ../src/checkjs/parsers/antlr/JavaScript.g:207:38: ( LT )*
                while True: #loop97
                    alt97 = 2
                    LA97_0 = self.input.LA(1)

                    if (LA97_0 == LT) :
                        alt97 = 1


                    if alt97 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT195=self.match(self.input, LT, self.FOLLOW_LT_in_withStatement1240)


                    else:
                        break #loop97
                char_literal196=self.match(self.input, 56, self.FOLLOW_56_in_withStatement1244)
                if self._state.backtracking == 0:

                    char_literal196_tree = self._adaptor.createWithPayload(char_literal196)
                    self._adaptor.addChild(root_0, char_literal196_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:207:47: ( LT )*
                while True: #loop98
                    alt98 = 2
                    LA98_0 = self.input.LA(1)

                    if (LA98_0 == LT) :
                        alt98 = 1


                    if alt98 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT197=self.match(self.input, LT, self.FOLLOW_LT_in_withStatement1246)


                    else:
                        break #loop98
                # ../src/checkjs/parsers/antlr/JavaScript.g:207:50: ( statement | statementBlock )
                alt99 = 2
                alt99 = self.dfa99.predict(self.input)
                if alt99 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:207:51: statement
                    pass 
                    self._state.following.append(self.FOLLOW_statement_in_withStatement1251)
                    statement198 = self.statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, statement198.tree)


                elif alt99 == 2:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:207:63: statementBlock
                    pass 
                    self._state.following.append(self.FOLLOW_statementBlock_in_withStatement1255)
                    statementBlock199 = self.statementBlock()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, statementBlock199.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 32, withStatement_StartIndex, success)

            pass
        return retval

    # $ANTLR end "withStatement"

    class labelledStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.labelledStatement_return, self).__init__()

            self.tree = None




    # $ANTLR start "labelledStatement"
    # ../src/checkjs/parsers/antlr/JavaScript.g:210:1: labelledStatement : Identifier ( LT )* ':' ( LT )* statement ;
    def labelledStatement(self, ):

        retval = self.labelledStatement_return()
        retval.start = self.input.LT(1)
        labelledStatement_StartIndex = self.input.index()
        root_0 = None

        Identifier200 = None
        LT201 = None
        char_literal202 = None
        LT203 = None
        statement204 = None


        Identifier200_tree = None
        LT201_tree = None
        char_literal202_tree = None
        LT203_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 33):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:211:2: ( Identifier ( LT )* ':' ( LT )* statement )
                # ../src/checkjs/parsers/antlr/JavaScript.g:211:4: Identifier ( LT )* ':' ( LT )* statement
                pass 
                root_0 = self._adaptor.nil()

                Identifier200=self.match(self.input, Identifier, self.FOLLOW_Identifier_in_labelledStatement1267)
                if self._state.backtracking == 0:

                    Identifier200_tree = self._adaptor.createWithPayload(Identifier200)
                    self._adaptor.addChild(root_0, Identifier200_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:211:17: ( LT )*
                while True: #loop100
                    alt100 = 2
                    LA100_0 = self.input.LA(1)

                    if (LA100_0 == LT) :
                        alt100 = 1


                    if alt100 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT201=self.match(self.input, LT, self.FOLLOW_LT_in_labelledStatement1269)


                    else:
                        break #loop100
                char_literal202=self.match(self.input, 71, self.FOLLOW_71_in_labelledStatement1273)
                if self._state.backtracking == 0:

                    char_literal202_tree = self._adaptor.createWithPayload(char_literal202)
                    self._adaptor.addChild(root_0, char_literal202_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:211:26: ( LT )*
                while True: #loop101
                    alt101 = 2
                    LA101_0 = self.input.LA(1)

                    if (LA101_0 == LT) :
                        alt101 = 1


                    if alt101 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT203=self.match(self.input, LT, self.FOLLOW_LT_in_labelledStatement1275)


                    else:
                        break #loop101
                self._state.following.append(self.FOLLOW_statement_in_labelledStatement1279)
                statement204 = self.statement()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, statement204.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 33, labelledStatement_StartIndex, success)

            pass
        return retval

    # $ANTLR end "labelledStatement"

    class switchStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.switchStatement_return, self).__init__()

            self.tree = None




    # $ANTLR start "switchStatement"
    # ../src/checkjs/parsers/antlr/JavaScript.g:214:1: switchStatement : 'switch' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* caseBlock ;
    def switchStatement(self, ):

        retval = self.switchStatement_return()
        retval.start = self.input.LT(1)
        switchStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal205 = None
        LT206 = None
        char_literal207 = None
        LT208 = None
        LT210 = None
        char_literal211 = None
        LT212 = None
        expression209 = None

        caseBlock213 = None


        string_literal205_tree = None
        LT206_tree = None
        char_literal207_tree = None
        LT208_tree = None
        LT210_tree = None
        char_literal211_tree = None
        LT212_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 34):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:215:2: ( 'switch' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* caseBlock )
                # ../src/checkjs/parsers/antlr/JavaScript.g:215:4: 'switch' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* caseBlock
                pass 
                root_0 = self._adaptor.nil()

                string_literal205=self.match(self.input, 72, self.FOLLOW_72_in_switchStatement1290)
                if self._state.backtracking == 0:

                    string_literal205_tree = self._adaptor.createWithPayload(string_literal205)
                    self._adaptor.addChild(root_0, string_literal205_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:215:15: ( LT )*
                while True: #loop102
                    alt102 = 2
                    LA102_0 = self.input.LA(1)

                    if (LA102_0 == LT) :
                        alt102 = 1


                    if alt102 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT206=self.match(self.input, LT, self.FOLLOW_LT_in_switchStatement1292)


                    else:
                        break #loop102
                char_literal207=self.match(self.input, 54, self.FOLLOW_54_in_switchStatement1296)
                if self._state.backtracking == 0:

                    char_literal207_tree = self._adaptor.createWithPayload(char_literal207)
                    self._adaptor.addChild(root_0, char_literal207_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:215:24: ( LT )*
                while True: #loop103
                    alt103 = 2
                    LA103_0 = self.input.LA(1)

                    if (LA103_0 == LT) :
                        alt103 = 1


                    if alt103 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT208=self.match(self.input, LT, self.FOLLOW_LT_in_switchStatement1298)


                    else:
                        break #loop103
                self._state.following.append(self.FOLLOW_expression_in_switchStatement1302)
                expression209 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expression209.tree)
                # ../src/checkjs/parsers/antlr/JavaScript.g:215:40: ( LT )*
                while True: #loop104
                    alt104 = 2
                    LA104_0 = self.input.LA(1)

                    if (LA104_0 == LT) :
                        alt104 = 1


                    if alt104 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT210=self.match(self.input, LT, self.FOLLOW_LT_in_switchStatement1304)


                    else:
                        break #loop104
                char_literal211=self.match(self.input, 56, self.FOLLOW_56_in_switchStatement1308)
                if self._state.backtracking == 0:

                    char_literal211_tree = self._adaptor.createWithPayload(char_literal211)
                    self._adaptor.addChild(root_0, char_literal211_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:215:49: ( LT )*
                while True: #loop105
                    alt105 = 2
                    LA105_0 = self.input.LA(1)

                    if (LA105_0 == LT) :
                        alt105 = 1


                    if alt105 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT212=self.match(self.input, LT, self.FOLLOW_LT_in_switchStatement1310)


                    else:
                        break #loop105
                self._state.following.append(self.FOLLOW_caseBlock_in_switchStatement1314)
                caseBlock213 = self.caseBlock()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, caseBlock213.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 34, switchStatement_StartIndex, success)

            pass
        return retval

    # $ANTLR end "switchStatement"

    class caseBlock_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.caseBlock_return, self).__init__()

            self.tree = None




    # $ANTLR start "caseBlock"
    # ../src/checkjs/parsers/antlr/JavaScript.g:218:1: caseBlock : '{' ( ( LT )* caseClause )* ( ( LT )* defaultClause ( ( LT )* caseClause )* )? ( LT )* '}' ;
    def caseBlock(self, ):

        retval = self.caseBlock_return()
        retval.start = self.input.LT(1)
        caseBlock_StartIndex = self.input.index()
        root_0 = None

        char_literal214 = None
        LT215 = None
        LT217 = None
        LT219 = None
        LT221 = None
        char_literal222 = None
        caseClause216 = None

        defaultClause218 = None

        caseClause220 = None


        char_literal214_tree = None
        LT215_tree = None
        LT217_tree = None
        LT219_tree = None
        LT221_tree = None
        char_literal222_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 35):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:219:2: ( '{' ( ( LT )* caseClause )* ( ( LT )* defaultClause ( ( LT )* caseClause )* )? ( LT )* '}' )
                # ../src/checkjs/parsers/antlr/JavaScript.g:219:4: '{' ( ( LT )* caseClause )* ( ( LT )* defaultClause ( ( LT )* caseClause )* )? ( LT )* '}'
                pass 
                root_0 = self._adaptor.nil()

                char_literal214=self.match(self.input, 57, self.FOLLOW_57_in_caseBlock1325)
                if self._state.backtracking == 0:

                    char_literal214_tree = self._adaptor.createWithPayload(char_literal214)
                    self._adaptor.addChild(root_0, char_literal214_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:219:8: ( ( LT )* caseClause )*
                while True: #loop107
                    alt107 = 2
                    alt107 = self.dfa107.predict(self.input)
                    if alt107 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:219:9: ( LT )* caseClause
                        pass 
                        # ../src/checkjs/parsers/antlr/JavaScript.g:219:11: ( LT )*
                        while True: #loop106
                            alt106 = 2
                            LA106_0 = self.input.LA(1)

                            if (LA106_0 == LT) :
                                alt106 = 1


                            if alt106 == 1:
                                # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                                pass 
                                LT215=self.match(self.input, LT, self.FOLLOW_LT_in_caseBlock1328)


                            else:
                                break #loop106
                        self._state.following.append(self.FOLLOW_caseClause_in_caseBlock1332)
                        caseClause216 = self.caseClause()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, caseClause216.tree)


                    else:
                        break #loop107
                # ../src/checkjs/parsers/antlr/JavaScript.g:219:27: ( ( LT )* defaultClause ( ( LT )* caseClause )* )?
                alt111 = 2
                alt111 = self.dfa111.predict(self.input)
                if alt111 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:219:28: ( LT )* defaultClause ( ( LT )* caseClause )*
                    pass 
                    # ../src/checkjs/parsers/antlr/JavaScript.g:219:30: ( LT )*
                    while True: #loop108
                        alt108 = 2
                        LA108_0 = self.input.LA(1)

                        if (LA108_0 == LT) :
                            alt108 = 1


                        if alt108 == 1:
                            # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                            pass 
                            LT217=self.match(self.input, LT, self.FOLLOW_LT_in_caseBlock1337)


                        else:
                            break #loop108
                    self._state.following.append(self.FOLLOW_defaultClause_in_caseBlock1341)
                    defaultClause218 = self.defaultClause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, defaultClause218.tree)
                    # ../src/checkjs/parsers/antlr/JavaScript.g:219:47: ( ( LT )* caseClause )*
                    while True: #loop110
                        alt110 = 2
                        alt110 = self.dfa110.predict(self.input)
                        if alt110 == 1:
                            # ../src/checkjs/parsers/antlr/JavaScript.g:219:48: ( LT )* caseClause
                            pass 
                            # ../src/checkjs/parsers/antlr/JavaScript.g:219:50: ( LT )*
                            while True: #loop109
                                alt109 = 2
                                LA109_0 = self.input.LA(1)

                                if (LA109_0 == LT) :
                                    alt109 = 1


                                if alt109 == 1:
                                    # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                                    pass 
                                    LT219=self.match(self.input, LT, self.FOLLOW_LT_in_caseBlock1344)


                                else:
                                    break #loop109
                            self._state.following.append(self.FOLLOW_caseClause_in_caseBlock1348)
                            caseClause220 = self.caseClause()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, caseClause220.tree)


                        else:
                            break #loop110



                # ../src/checkjs/parsers/antlr/JavaScript.g:219:70: ( LT )*
                while True: #loop112
                    alt112 = 2
                    LA112_0 = self.input.LA(1)

                    if (LA112_0 == LT) :
                        alt112 = 1


                    if alt112 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT221=self.match(self.input, LT, self.FOLLOW_LT_in_caseBlock1354)


                    else:
                        break #loop112
                char_literal222=self.match(self.input, 58, self.FOLLOW_58_in_caseBlock1358)
                if self._state.backtracking == 0:

                    char_literal222_tree = self._adaptor.createWithPayload(char_literal222)
                    self._adaptor.addChild(root_0, char_literal222_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 35, caseBlock_StartIndex, success)

            pass
        return retval

    # $ANTLR end "caseBlock"

    class caseClause_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.caseClause_return, self).__init__()

            self.tree = None




    # $ANTLR start "caseClause"
    # ../src/checkjs/parsers/antlr/JavaScript.g:222:1: caseClause : 'case' ( LT )* expression ( LT )* ':' ( LT )* ( statementList )? ;
    def caseClause(self, ):

        retval = self.caseClause_return()
        retval.start = self.input.LT(1)
        caseClause_StartIndex = self.input.index()
        root_0 = None

        string_literal223 = None
        LT224 = None
        LT226 = None
        char_literal227 = None
        LT228 = None
        expression225 = None

        statementList229 = None


        string_literal223_tree = None
        LT224_tree = None
        LT226_tree = None
        char_literal227_tree = None
        LT228_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 36):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:223:2: ( 'case' ( LT )* expression ( LT )* ':' ( LT )* ( statementList )? )
                # ../src/checkjs/parsers/antlr/JavaScript.g:223:4: 'case' ( LT )* expression ( LT )* ':' ( LT )* ( statementList )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal223=self.match(self.input, 73, self.FOLLOW_73_in_caseClause1369)
                if self._state.backtracking == 0:

                    string_literal223_tree = self._adaptor.createWithPayload(string_literal223)
                    self._adaptor.addChild(root_0, string_literal223_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:223:13: ( LT )*
                while True: #loop113
                    alt113 = 2
                    LA113_0 = self.input.LA(1)

                    if (LA113_0 == LT) :
                        alt113 = 1


                    if alt113 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT224=self.match(self.input, LT, self.FOLLOW_LT_in_caseClause1371)


                    else:
                        break #loop113
                self._state.following.append(self.FOLLOW_expression_in_caseClause1375)
                expression225 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expression225.tree)
                # ../src/checkjs/parsers/antlr/JavaScript.g:223:29: ( LT )*
                while True: #loop114
                    alt114 = 2
                    LA114_0 = self.input.LA(1)

                    if (LA114_0 == LT) :
                        alt114 = 1


                    if alt114 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT226=self.match(self.input, LT, self.FOLLOW_LT_in_caseClause1377)


                    else:
                        break #loop114
                char_literal227=self.match(self.input, 71, self.FOLLOW_71_in_caseClause1381)
                if self._state.backtracking == 0:

                    char_literal227_tree = self._adaptor.createWithPayload(char_literal227)
                    self._adaptor.addChild(root_0, char_literal227_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:223:38: ( LT )*
                while True: #loop115
                    alt115 = 2
                    LA115_0 = self.input.LA(1)

                    if (LA115_0 == LT) :
                        LA115_2 = self.input.LA(2)

                        if (self.synpred127_JavaScript()) :
                            alt115 = 1




                    if alt115 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT228=self.match(self.input, LT, self.FOLLOW_LT_in_caseClause1383)


                    else:
                        break #loop115
                # ../src/checkjs/parsers/antlr/JavaScript.g:223:41: ( statementList )?
                alt116 = 2
                LA116_0 = self.input.LA(1)

                if ((Identifier <= LA116_0 <= NumericLiteral) or LA116_0 == 52 or LA116_0 == 54 or LA116_0 == 57 or LA116_0 == 59 or LA116_0 == 61 or (63 <= LA116_0 <= 65) or (67 <= LA116_0 <= 70) or LA116_0 == 72 or (75 <= LA116_0 <= 76) or (79 <= LA116_0 <= 80) or (96 <= LA116_0 <= 97) or (108 <= LA116_0 <= 119)) :
                    alt116 = 1
                if alt116 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: statementList
                    pass 
                    self._state.following.append(self.FOLLOW_statementList_in_caseClause1387)
                    statementList229 = self.statementList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, statementList229.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 36, caseClause_StartIndex, success)

            pass
        return retval

    # $ANTLR end "caseClause"

    class defaultClause_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.defaultClause_return, self).__init__()

            self.tree = None




    # $ANTLR start "defaultClause"
    # ../src/checkjs/parsers/antlr/JavaScript.g:226:1: defaultClause : 'default' ( LT )* ':' ( LT )* ( statementList )? ;
    def defaultClause(self, ):

        retval = self.defaultClause_return()
        retval.start = self.input.LT(1)
        defaultClause_StartIndex = self.input.index()
        root_0 = None

        string_literal230 = None
        LT231 = None
        char_literal232 = None
        LT233 = None
        statementList234 = None


        string_literal230_tree = None
        LT231_tree = None
        char_literal232_tree = None
        LT233_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 37):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:227:2: ( 'default' ( LT )* ':' ( LT )* ( statementList )? )
                # ../src/checkjs/parsers/antlr/JavaScript.g:227:4: 'default' ( LT )* ':' ( LT )* ( statementList )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal230=self.match(self.input, 74, self.FOLLOW_74_in_defaultClause1399)
                if self._state.backtracking == 0:

                    string_literal230_tree = self._adaptor.createWithPayload(string_literal230)
                    self._adaptor.addChild(root_0, string_literal230_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:227:16: ( LT )*
                while True: #loop117
                    alt117 = 2
                    LA117_0 = self.input.LA(1)

                    if (LA117_0 == LT) :
                        alt117 = 1


                    if alt117 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT231=self.match(self.input, LT, self.FOLLOW_LT_in_defaultClause1401)


                    else:
                        break #loop117
                char_literal232=self.match(self.input, 71, self.FOLLOW_71_in_defaultClause1405)
                if self._state.backtracking == 0:

                    char_literal232_tree = self._adaptor.createWithPayload(char_literal232)
                    self._adaptor.addChild(root_0, char_literal232_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:227:25: ( LT )*
                while True: #loop118
                    alt118 = 2
                    LA118_0 = self.input.LA(1)

                    if (LA118_0 == LT) :
                        LA118_2 = self.input.LA(2)

                        if (self.synpred130_JavaScript()) :
                            alt118 = 1




                    if alt118 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT233=self.match(self.input, LT, self.FOLLOW_LT_in_defaultClause1407)


                    else:
                        break #loop118
                # ../src/checkjs/parsers/antlr/JavaScript.g:227:28: ( statementList )?
                alt119 = 2
                LA119_0 = self.input.LA(1)

                if ((Identifier <= LA119_0 <= NumericLiteral) or LA119_0 == 52 or LA119_0 == 54 or LA119_0 == 57 or LA119_0 == 59 or LA119_0 == 61 or (63 <= LA119_0 <= 65) or (67 <= LA119_0 <= 70) or LA119_0 == 72 or (75 <= LA119_0 <= 76) or (79 <= LA119_0 <= 80) or (96 <= LA119_0 <= 97) or (108 <= LA119_0 <= 119)) :
                    alt119 = 1
                if alt119 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: statementList
                    pass 
                    self._state.following.append(self.FOLLOW_statementList_in_defaultClause1411)
                    statementList234 = self.statementList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, statementList234.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 37, defaultClause_StartIndex, success)

            pass
        return retval

    # $ANTLR end "defaultClause"

    class throwStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.throwStatement_return, self).__init__()

            self.tree = None




    # $ANTLR start "throwStatement"
    # ../src/checkjs/parsers/antlr/JavaScript.g:230:1: throwStatement : 'throw' expression ( LT )* ';' ;
    def throwStatement(self, ):

        retval = self.throwStatement_return()
        retval.start = self.input.LT(1)
        throwStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal235 = None
        LT237 = None
        char_literal238 = None
        expression236 = None


        string_literal235_tree = None
        LT237_tree = None
        char_literal238_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 38):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:231:2: ( 'throw' expression ( LT )* ';' )
                # ../src/checkjs/parsers/antlr/JavaScript.g:231:4: 'throw' expression ( LT )* ';'
                pass 
                root_0 = self._adaptor.nil()

                string_literal235=self.match(self.input, 75, self.FOLLOW_75_in_throwStatement1423)
                if self._state.backtracking == 0:

                    string_literal235_tree = self._adaptor.createWithPayload(string_literal235)
                    self._adaptor.addChild(root_0, string_literal235_tree)

                self._state.following.append(self.FOLLOW_expression_in_throwStatement1425)
                expression236 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expression236.tree)
                # ../src/checkjs/parsers/antlr/JavaScript.g:231:25: ( LT )*
                while True: #loop120
                    alt120 = 2
                    LA120_0 = self.input.LA(1)

                    if (LA120_0 == LT) :
                        alt120 = 1


                    if alt120 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT237=self.match(self.input, LT, self.FOLLOW_LT_in_throwStatement1427)


                    else:
                        break #loop120
                char_literal238=self.match(self.input, 53, self.FOLLOW_53_in_throwStatement1431)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 38, throwStatement_StartIndex, success)

            pass
        return retval

    # $ANTLR end "throwStatement"

    class tryStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.tryStatement_return, self).__init__()

            self.tree = None




    # $ANTLR start "tryStatement"
    # ../src/checkjs/parsers/antlr/JavaScript.g:234:1: tryStatement : 'try' ( LT )* statementBlock ( LT )* ( finallyClause | catchClause ( ( LT )* finallyClause )? ) ;
    def tryStatement(self, ):

        retval = self.tryStatement_return()
        retval.start = self.input.LT(1)
        tryStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal239 = None
        LT240 = None
        LT242 = None
        LT245 = None
        statementBlock241 = None

        finallyClause243 = None

        catchClause244 = None

        finallyClause246 = None


        string_literal239_tree = None
        LT240_tree = None
        LT242_tree = None
        LT245_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 39):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:235:2: ( 'try' ( LT )* statementBlock ( LT )* ( finallyClause | catchClause ( ( LT )* finallyClause )? ) )
                # ../src/checkjs/parsers/antlr/JavaScript.g:235:4: 'try' ( LT )* statementBlock ( LT )* ( finallyClause | catchClause ( ( LT )* finallyClause )? )
                pass 
                root_0 = self._adaptor.nil()

                string_literal239=self.match(self.input, 76, self.FOLLOW_76_in_tryStatement1443)
                if self._state.backtracking == 0:

                    string_literal239_tree = self._adaptor.createWithPayload(string_literal239)
                    self._adaptor.addChild(root_0, string_literal239_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:235:12: ( LT )*
                while True: #loop121
                    alt121 = 2
                    LA121_0 = self.input.LA(1)

                    if (LA121_0 == LT) :
                        alt121 = 1


                    if alt121 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT240=self.match(self.input, LT, self.FOLLOW_LT_in_tryStatement1445)


                    else:
                        break #loop121
                self._state.following.append(self.FOLLOW_statementBlock_in_tryStatement1449)
                statementBlock241 = self.statementBlock()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, statementBlock241.tree)
                # ../src/checkjs/parsers/antlr/JavaScript.g:235:32: ( LT )*
                while True: #loop122
                    alt122 = 2
                    LA122_0 = self.input.LA(1)

                    if (LA122_0 == LT) :
                        alt122 = 1


                    if alt122 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT242=self.match(self.input, LT, self.FOLLOW_LT_in_tryStatement1451)


                    else:
                        break #loop122
                # ../src/checkjs/parsers/antlr/JavaScript.g:235:35: ( finallyClause | catchClause ( ( LT )* finallyClause )? )
                alt125 = 2
                LA125_0 = self.input.LA(1)

                if (LA125_0 == 78) :
                    alt125 = 1
                elif (LA125_0 == 77) :
                    alt125 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 125, 0, self.input)

                    raise nvae

                if alt125 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:235:36: finallyClause
                    pass 
                    self._state.following.append(self.FOLLOW_finallyClause_in_tryStatement1456)
                    finallyClause243 = self.finallyClause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, finallyClause243.tree)


                elif alt125 == 2:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:235:52: catchClause ( ( LT )* finallyClause )?
                    pass 
                    self._state.following.append(self.FOLLOW_catchClause_in_tryStatement1460)
                    catchClause244 = self.catchClause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, catchClause244.tree)
                    # ../src/checkjs/parsers/antlr/JavaScript.g:235:64: ( ( LT )* finallyClause )?
                    alt124 = 2
                    alt124 = self.dfa124.predict(self.input)
                    if alt124 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:235:65: ( LT )* finallyClause
                        pass 
                        # ../src/checkjs/parsers/antlr/JavaScript.g:235:67: ( LT )*
                        while True: #loop123
                            alt123 = 2
                            LA123_0 = self.input.LA(1)

                            if (LA123_0 == LT) :
                                alt123 = 1


                            if alt123 == 1:
                                # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                                pass 
                                LT245=self.match(self.input, LT, self.FOLLOW_LT_in_tryStatement1463)


                            else:
                                break #loop123
                        self._state.following.append(self.FOLLOW_finallyClause_in_tryStatement1467)
                        finallyClause246 = self.finallyClause()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, finallyClause246.tree)









                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 39, tryStatement_StartIndex, success)

            pass
        return retval

    # $ANTLR end "tryStatement"

    class catchClause_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.catchClause_return, self).__init__()

            self.tree = None




    # $ANTLR start "catchClause"
    # ../src/checkjs/parsers/antlr/JavaScript.g:238:1: catchClause : 'catch' ( LT )* '(' ( LT )* Identifier ( LT )* ')' ( LT )* statementBlock ;
    def catchClause(self, ):

        retval = self.catchClause_return()
        retval.start = self.input.LT(1)
        catchClause_StartIndex = self.input.index()
        root_0 = None

        string_literal247 = None
        LT248 = None
        char_literal249 = None
        LT250 = None
        Identifier251 = None
        LT252 = None
        char_literal253 = None
        LT254 = None
        statementBlock255 = None


        string_literal247_tree = None
        LT248_tree = None
        char_literal249_tree = None
        LT250_tree = None
        Identifier251_tree = None
        LT252_tree = None
        char_literal253_tree = None
        LT254_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 40):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:239:2: ( 'catch' ( LT )* '(' ( LT )* Identifier ( LT )* ')' ( LT )* statementBlock )
                # ../src/checkjs/parsers/antlr/JavaScript.g:239:4: 'catch' ( LT )* '(' ( LT )* Identifier ( LT )* ')' ( LT )* statementBlock
                pass 
                root_0 = self._adaptor.nil()

                string_literal247=self.match(self.input, 77, self.FOLLOW_77_in_catchClause1481)
                if self._state.backtracking == 0:

                    string_literal247_tree = self._adaptor.createWithPayload(string_literal247)
                    self._adaptor.addChild(root_0, string_literal247_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:239:14: ( LT )*
                while True: #loop126
                    alt126 = 2
                    LA126_0 = self.input.LA(1)

                    if (LA126_0 == LT) :
                        alt126 = 1


                    if alt126 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT248=self.match(self.input, LT, self.FOLLOW_LT_in_catchClause1483)


                    else:
                        break #loop126
                char_literal249=self.match(self.input, 54, self.FOLLOW_54_in_catchClause1487)
                if self._state.backtracking == 0:

                    char_literal249_tree = self._adaptor.createWithPayload(char_literal249)
                    self._adaptor.addChild(root_0, char_literal249_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:239:23: ( LT )*
                while True: #loop127
                    alt127 = 2
                    LA127_0 = self.input.LA(1)

                    if (LA127_0 == LT) :
                        alt127 = 1


                    if alt127 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT250=self.match(self.input, LT, self.FOLLOW_LT_in_catchClause1489)


                    else:
                        break #loop127
                Identifier251=self.match(self.input, Identifier, self.FOLLOW_Identifier_in_catchClause1493)
                if self._state.backtracking == 0:

                    Identifier251_tree = self._adaptor.createWithPayload(Identifier251)
                    self._adaptor.addChild(root_0, Identifier251_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:239:39: ( LT )*
                while True: #loop128
                    alt128 = 2
                    LA128_0 = self.input.LA(1)

                    if (LA128_0 == LT) :
                        alt128 = 1


                    if alt128 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT252=self.match(self.input, LT, self.FOLLOW_LT_in_catchClause1495)


                    else:
                        break #loop128
                char_literal253=self.match(self.input, 56, self.FOLLOW_56_in_catchClause1499)
                if self._state.backtracking == 0:

                    char_literal253_tree = self._adaptor.createWithPayload(char_literal253)
                    self._adaptor.addChild(root_0, char_literal253_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:239:48: ( LT )*
                while True: #loop129
                    alt129 = 2
                    LA129_0 = self.input.LA(1)

                    if (LA129_0 == LT) :
                        alt129 = 1


                    if alt129 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT254=self.match(self.input, LT, self.FOLLOW_LT_in_catchClause1501)


                    else:
                        break #loop129
                self._state.following.append(self.FOLLOW_statementBlock_in_catchClause1505)
                statementBlock255 = self.statementBlock()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, statementBlock255.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 40, catchClause_StartIndex, success)

            pass
        return retval

    # $ANTLR end "catchClause"

    class finallyClause_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.finallyClause_return, self).__init__()

            self.tree = None




    # $ANTLR start "finallyClause"
    # ../src/checkjs/parsers/antlr/JavaScript.g:242:1: finallyClause : 'finally' ( LT )* statementBlock ;
    def finallyClause(self, ):

        retval = self.finallyClause_return()
        retval.start = self.input.LT(1)
        finallyClause_StartIndex = self.input.index()
        root_0 = None

        string_literal256 = None
        LT257 = None
        statementBlock258 = None


        string_literal256_tree = None
        LT257_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 41):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:243:2: ( 'finally' ( LT )* statementBlock )
                # ../src/checkjs/parsers/antlr/JavaScript.g:243:4: 'finally' ( LT )* statementBlock
                pass 
                root_0 = self._adaptor.nil()

                string_literal256=self.match(self.input, 78, self.FOLLOW_78_in_finallyClause1516)
                if self._state.backtracking == 0:

                    string_literal256_tree = self._adaptor.createWithPayload(string_literal256)
                    self._adaptor.addChild(root_0, string_literal256_tree)

                # ../src/checkjs/parsers/antlr/JavaScript.g:243:16: ( LT )*
                while True: #loop130
                    alt130 = 2
                    LA130_0 = self.input.LA(1)

                    if (LA130_0 == LT) :
                        alt130 = 1


                    if alt130 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT257=self.match(self.input, LT, self.FOLLOW_LT_in_finallyClause1518)


                    else:
                        break #loop130
                self._state.following.append(self.FOLLOW_statementBlock_in_finallyClause1522)
                statementBlock258 = self.statementBlock()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, statementBlock258.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 41, finallyClause_StartIndex, success)

            pass
        return retval

    # $ANTLR end "finallyClause"

    class expression_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.expression_return, self).__init__()

            self.tree = None




    # $ANTLR start "expression"
    # ../src/checkjs/parsers/antlr/JavaScript.g:247:1: expression : assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )* ;
    def expression(self, ):

        retval = self.expression_return()
        retval.start = self.input.LT(1)
        expression_StartIndex = self.input.index()
        root_0 = None

        LT260 = None
        char_literal261 = None
        LT262 = None
        assignmentExpression259 = None

        assignmentExpression263 = None


        LT260_tree = None
        char_literal261_tree = None
        LT262_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 42):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:248:2: ( assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )* )
                # ../src/checkjs/parsers/antlr/JavaScript.g:248:4: assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_assignmentExpression_in_expression1534)
                assignmentExpression259 = self.assignmentExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, assignmentExpression259.tree)
                # ../src/checkjs/parsers/antlr/JavaScript.g:248:25: ( ( LT )* ',' ( LT )* assignmentExpression )*
                while True: #loop133
                    alt133 = 2
                    alt133 = self.dfa133.predict(self.input)
                    if alt133 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:248:26: ( LT )* ',' ( LT )* assignmentExpression
                        pass 
                        # ../src/checkjs/parsers/antlr/JavaScript.g:248:28: ( LT )*
                        while True: #loop131
                            alt131 = 2
                            LA131_0 = self.input.LA(1)

                            if (LA131_0 == LT) :
                                alt131 = 1


                            if alt131 == 1:
                                # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                                pass 
                                LT260=self.match(self.input, LT, self.FOLLOW_LT_in_expression1537)


                            else:
                                break #loop131
                        char_literal261=self.match(self.input, 55, self.FOLLOW_55_in_expression1541)
                        if self._state.backtracking == 0:

                            char_literal261_tree = self._adaptor.createWithPayload(char_literal261)
                            self._adaptor.addChild(root_0, char_literal261_tree)

                        # ../src/checkjs/parsers/antlr/JavaScript.g:248:37: ( LT )*
                        while True: #loop132
                            alt132 = 2
                            LA132_0 = self.input.LA(1)

                            if (LA132_0 == LT) :
                                alt132 = 1


                            if alt132 == 1:
                                # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                                pass 
                                LT262=self.match(self.input, LT, self.FOLLOW_LT_in_expression1543)


                            else:
                                break #loop132
                        self._state.following.append(self.FOLLOW_assignmentExpression_in_expression1547)
                        assignmentExpression263 = self.assignmentExpression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, assignmentExpression263.tree)


                    else:
                        break #loop133



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 42, expression_StartIndex, success)

            pass
        return retval

    # $ANTLR end "expression"

    class expressionNoIn_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.expressionNoIn_return, self).__init__()

            self.tree = None




    # $ANTLR start "expressionNoIn"
    # ../src/checkjs/parsers/antlr/JavaScript.g:251:1: expressionNoIn : assignmentExpressionNoIn ( ( LT )* ',' ( LT )* assignmentExpressionNoIn )* ;
    def expressionNoIn(self, ):

        retval = self.expressionNoIn_return()
        retval.start = self.input.LT(1)
        expressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT265 = None
        char_literal266 = None
        LT267 = None
        assignmentExpressionNoIn264 = None

        assignmentExpressionNoIn268 = None


        LT265_tree = None
        char_literal266_tree = None
        LT267_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 43):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:252:2: ( assignmentExpressionNoIn ( ( LT )* ',' ( LT )* assignmentExpressionNoIn )* )
                # ../src/checkjs/parsers/antlr/JavaScript.g:252:4: assignmentExpressionNoIn ( ( LT )* ',' ( LT )* assignmentExpressionNoIn )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_assignmentExpressionNoIn_in_expressionNoIn1560)
                assignmentExpressionNoIn264 = self.assignmentExpressionNoIn()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, assignmentExpressionNoIn264.tree)
                # ../src/checkjs/parsers/antlr/JavaScript.g:252:29: ( ( LT )* ',' ( LT )* assignmentExpressionNoIn )*
                while True: #loop136
                    alt136 = 2
                    alt136 = self.dfa136.predict(self.input)
                    if alt136 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:252:30: ( LT )* ',' ( LT )* assignmentExpressionNoIn
                        pass 
                        # ../src/checkjs/parsers/antlr/JavaScript.g:252:32: ( LT )*
                        while True: #loop134
                            alt134 = 2
                            LA134_0 = self.input.LA(1)

                            if (LA134_0 == LT) :
                                alt134 = 1


                            if alt134 == 1:
                                # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                                pass 
                                LT265=self.match(self.input, LT, self.FOLLOW_LT_in_expressionNoIn1563)


                            else:
                                break #loop134
                        char_literal266=self.match(self.input, 55, self.FOLLOW_55_in_expressionNoIn1567)
                        if self._state.backtracking == 0:

                            char_literal266_tree = self._adaptor.createWithPayload(char_literal266)
                            self._adaptor.addChild(root_0, char_literal266_tree)

                        # ../src/checkjs/parsers/antlr/JavaScript.g:252:41: ( LT )*
                        while True: #loop135
                            alt135 = 2
                            LA135_0 = self.input.LA(1)

                            if (LA135_0 == LT) :
                                alt135 = 1


                            if alt135 == 1:
                                # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                                pass 
                                LT267=self.match(self.input, LT, self.FOLLOW_LT_in_expressionNoIn1569)


                            else:
                                break #loop135
                        self._state.following.append(self.FOLLOW_assignmentExpressionNoIn_in_expressionNoIn1573)
                        assignmentExpressionNoIn268 = self.assignmentExpressionNoIn()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, assignmentExpressionNoIn268.tree)


                    else:
                        break #loop136



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 43, expressionNoIn_StartIndex, success)

            pass
        return retval

    # $ANTLR end "expressionNoIn"

    class assignmentExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.assignmentExpression_return, self).__init__()

            self.tree = None




    # $ANTLR start "assignmentExpression"
    # ../src/checkjs/parsers/antlr/JavaScript.g:255:1: assignmentExpression : ( callExpression -> ^( ASSIGNMENT_EXPR callExpression ) | ( leftHandSideExpression ( LT )* nonAssignmentOperator ( LT )* assignmentExpression -> ^( nonAssignmentOperator ^( OPERATOR_ARG leftHandSideExpression ) ^( OPERATOR_ARG assignmentExpression ) ) ) | ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGNMENT ^( assignmentOperator ) ^( OPERATOR_ARGS leftHandSideExpression assignmentExpression ) ) ) | unaryExpression | newExpression -> ^( ASSIGNMENT_EXPR newExpression ) );
    def assignmentExpression(self, ):

        retval = self.assignmentExpression_return()
        retval.start = self.input.LT(1)
        assignmentExpression_StartIndex = self.input.index()
        root_0 = None

        LT271 = None
        LT273 = None
        LT276 = None
        LT278 = None
        callExpression269 = None

        leftHandSideExpression270 = None

        nonAssignmentOperator272 = None

        assignmentExpression274 = None

        leftHandSideExpression275 = None

        assignmentOperator277 = None

        assignmentExpression279 = None

        unaryExpression280 = None

        newExpression281 = None


        LT271_tree = None
        LT273_tree = None
        LT276_tree = None
        LT278_tree = None
        stream_LT = RewriteRuleTokenStream(self._adaptor, "token LT")
        stream_assignmentOperator = RewriteRuleSubtreeStream(self._adaptor, "rule assignmentOperator")
        stream_leftHandSideExpression = RewriteRuleSubtreeStream(self._adaptor, "rule leftHandSideExpression")
        stream_nonAssignmentOperator = RewriteRuleSubtreeStream(self._adaptor, "rule nonAssignmentOperator")
        stream_assignmentExpression = RewriteRuleSubtreeStream(self._adaptor, "rule assignmentExpression")
        stream_callExpression = RewriteRuleSubtreeStream(self._adaptor, "rule callExpression")
        stream_newExpression = RewriteRuleSubtreeStream(self._adaptor, "rule newExpression")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 44):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:257:5: ( callExpression -> ^( ASSIGNMENT_EXPR callExpression ) | ( leftHandSideExpression ( LT )* nonAssignmentOperator ( LT )* assignmentExpression -> ^( nonAssignmentOperator ^( OPERATOR_ARG leftHandSideExpression ) ^( OPERATOR_ARG assignmentExpression ) ) ) | ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGNMENT ^( assignmentOperator ) ^( OPERATOR_ARGS leftHandSideExpression assignmentExpression ) ) ) | unaryExpression | newExpression -> ^( ASSIGNMENT_EXPR newExpression ) )
                alt141 = 5
                alt141 = self.dfa141.predict(self.input)
                if alt141 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:257:7: callExpression
                    pass 
                    self._state.following.append(self.FOLLOW_callExpression_in_assignmentExpression1594)
                    callExpression269 = self.callExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_callExpression.add(callExpression269.tree)

                    # AST Rewrite
                    # elements: callExpression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 257:22: -> ^( ASSIGNMENT_EXPR callExpression )
                        # ../src/checkjs/parsers/antlr/JavaScript.g:257:25: ^( ASSIGNMENT_EXPR callExpression )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ASSIGNMENT_EXPR, "ASSIGNMENT_EXPR"), root_1)

                        self._adaptor.addChild(root_1, stream_callExpression.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt141 == 2:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:258:7: ( leftHandSideExpression ( LT )* nonAssignmentOperator ( LT )* assignmentExpression -> ^( nonAssignmentOperator ^( OPERATOR_ARG leftHandSideExpression ) ^( OPERATOR_ARG assignmentExpression ) ) )
                    pass 
                    # ../src/checkjs/parsers/antlr/JavaScript.g:258:7: ( leftHandSideExpression ( LT )* nonAssignmentOperator ( LT )* assignmentExpression -> ^( nonAssignmentOperator ^( OPERATOR_ARG leftHandSideExpression ) ^( OPERATOR_ARG assignmentExpression ) ) )
                    # ../src/checkjs/parsers/antlr/JavaScript.g:258:8: leftHandSideExpression ( LT )* nonAssignmentOperator ( LT )* assignmentExpression
                    pass 
                    self._state.following.append(self.FOLLOW_leftHandSideExpression_in_assignmentExpression1612)
                    leftHandSideExpression270 = self.leftHandSideExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_leftHandSideExpression.add(leftHandSideExpression270.tree)
                    # ../src/checkjs/parsers/antlr/JavaScript.g:258:31: ( LT )*
                    while True: #loop137
                        alt137 = 2
                        LA137_0 = self.input.LA(1)

                        if (LA137_0 == LT) :
                            alt137 = 1


                        if alt137 == 1:
                            # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                            pass 
                            LT271=self.match(self.input, LT, self.FOLLOW_LT_in_assignmentExpression1614) 
                            if self._state.backtracking == 0:
                                stream_LT.add(LT271)


                        else:
                            break #loop137
                    self._state.following.append(self.FOLLOW_nonAssignmentOperator_in_assignmentExpression1617)
                    nonAssignmentOperator272 = self.nonAssignmentOperator()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_nonAssignmentOperator.add(nonAssignmentOperator272.tree)
                    # ../src/checkjs/parsers/antlr/JavaScript.g:258:57: ( LT )*
                    while True: #loop138
                        alt138 = 2
                        LA138_0 = self.input.LA(1)

                        if (LA138_0 == LT) :
                            alt138 = 1


                        if alt138 == 1:
                            # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                            pass 
                            LT273=self.match(self.input, LT, self.FOLLOW_LT_in_assignmentExpression1619) 
                            if self._state.backtracking == 0:
                                stream_LT.add(LT273)


                        else:
                            break #loop138
                    self._state.following.append(self.FOLLOW_assignmentExpression_in_assignmentExpression1622)
                    assignmentExpression274 = self.assignmentExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_assignmentExpression.add(assignmentExpression274.tree)

                    # AST Rewrite
                    # elements: assignmentExpression, nonAssignmentOperator, leftHandSideExpression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 258:82: -> ^( nonAssignmentOperator ^( OPERATOR_ARG leftHandSideExpression ) ^( OPERATOR_ARG assignmentExpression ) )
                        # ../src/checkjs/parsers/antlr/JavaScript.g:259:13: ^( nonAssignmentOperator ^( OPERATOR_ARG leftHandSideExpression ) ^( OPERATOR_ARG assignmentExpression ) )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(stream_nonAssignmentOperator.nextNode(), root_1)

                        # ../src/checkjs/parsers/antlr/JavaScript.g:260:17: ^( OPERATOR_ARG leftHandSideExpression )
                        root_2 = self._adaptor.nil()
                        root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(OPERATOR_ARG, "OPERATOR_ARG"), root_2)

                        self._adaptor.addChild(root_2, stream_leftHandSideExpression.nextTree())

                        self._adaptor.addChild(root_1, root_2)
                        # ../src/checkjs/parsers/antlr/JavaScript.g:261:17: ^( OPERATOR_ARG assignmentExpression )
                        root_2 = self._adaptor.nil()
                        root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(OPERATOR_ARG, "OPERATOR_ARG"), root_2)

                        self._adaptor.addChild(root_2, stream_assignmentExpression.nextTree())

                        self._adaptor.addChild(root_1, root_2)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0





                elif alt141 == 3:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:264:7: ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGNMENT ^( assignmentOperator ) ^( OPERATOR_ARGS leftHandSideExpression assignmentExpression ) ) )
                    pass 
                    # ../src/checkjs/parsers/antlr/JavaScript.g:264:7: ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGNMENT ^( assignmentOperator ) ^( OPERATOR_ARGS leftHandSideExpression assignmentExpression ) ) )
                    # ../src/checkjs/parsers/antlr/JavaScript.g:264:8: leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression
                    pass 
                    self._state.following.append(self.FOLLOW_leftHandSideExpression_in_assignmentExpression1717)
                    leftHandSideExpression275 = self.leftHandSideExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_leftHandSideExpression.add(leftHandSideExpression275.tree)
                    # ../src/checkjs/parsers/antlr/JavaScript.g:264:31: ( LT )*
                    while True: #loop139
                        alt139 = 2
                        LA139_0 = self.input.LA(1)

                        if (LA139_0 == LT) :
                            alt139 = 1


                        if alt139 == 1:
                            # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                            pass 
                            LT276=self.match(self.input, LT, self.FOLLOW_LT_in_assignmentExpression1719) 
                            if self._state.backtracking == 0:
                                stream_LT.add(LT276)


                        else:
                            break #loop139
                    self._state.following.append(self.FOLLOW_assignmentOperator_in_assignmentExpression1722)
                    assignmentOperator277 = self.assignmentOperator()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_assignmentOperator.add(assignmentOperator277.tree)
                    # ../src/checkjs/parsers/antlr/JavaScript.g:264:54: ( LT )*
                    while True: #loop140
                        alt140 = 2
                        LA140_0 = self.input.LA(1)

                        if (LA140_0 == LT) :
                            alt140 = 1


                        if alt140 == 1:
                            # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                            pass 
                            LT278=self.match(self.input, LT, self.FOLLOW_LT_in_assignmentExpression1724) 
                            if self._state.backtracking == 0:
                                stream_LT.add(LT278)


                        else:
                            break #loop140
                    self._state.following.append(self.FOLLOW_assignmentExpression_in_assignmentExpression1727)
                    assignmentExpression279 = self.assignmentExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_assignmentExpression.add(assignmentExpression279.tree)

                    # AST Rewrite
                    # elements: leftHandSideExpression, assignmentOperator, assignmentExpression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 264:79: -> ^( ASSIGNMENT ^( assignmentOperator ) ^( OPERATOR_ARGS leftHandSideExpression assignmentExpression ) )
                        # ../src/checkjs/parsers/antlr/JavaScript.g:265:13: ^( ASSIGNMENT ^( assignmentOperator ) ^( OPERATOR_ARGS leftHandSideExpression assignmentExpression ) )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ASSIGNMENT, "ASSIGNMENT"), root_1)

                        # ../src/checkjs/parsers/antlr/JavaScript.g:266:17: ^( assignmentOperator )
                        root_2 = self._adaptor.nil()
                        root_2 = self._adaptor.becomeRoot(stream_assignmentOperator.nextNode(), root_2)

                        self._adaptor.addChild(root_1, root_2)
                        # ../src/checkjs/parsers/antlr/JavaScript.g:267:17: ^( OPERATOR_ARGS leftHandSideExpression assignmentExpression )
                        root_2 = self._adaptor.nil()
                        root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(OPERATOR_ARGS, "OPERATOR_ARGS"), root_2)

                        self._adaptor.addChild(root_2, stream_leftHandSideExpression.nextTree())
                        self._adaptor.addChild(root_2, stream_assignmentExpression.nextTree())

                        self._adaptor.addChild(root_1, root_2)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0





                elif alt141 == 4:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:270:7: unaryExpression
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_unaryExpression_in_assignmentExpression1821)
                    unaryExpression280 = self.unaryExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, unaryExpression280.tree)


                elif alt141 == 5:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:271:7: newExpression
                    pass 
                    self._state.following.append(self.FOLLOW_newExpression_in_assignmentExpression1829)
                    newExpression281 = self.newExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_newExpression.add(newExpression281.tree)

                    # AST Rewrite
                    # elements: newExpression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 271:21: -> ^( ASSIGNMENT_EXPR newExpression )
                        # ../src/checkjs/parsers/antlr/JavaScript.g:271:24: ^( ASSIGNMENT_EXPR newExpression )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ASSIGNMENT_EXPR, "ASSIGNMENT_EXPR"), root_1)

                        self._adaptor.addChild(root_1, stream_newExpression.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 44, assignmentExpression_StartIndex, success)

            pass
        return retval

    # $ANTLR end "assignmentExpression"

    class assignmentExpressionNoIn_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.assignmentExpressionNoIn_return, self).__init__()

            self.tree = None




    # $ANTLR start "assignmentExpressionNoIn"
    # ../src/checkjs/parsers/antlr/JavaScript.g:274:1: assignmentExpressionNoIn : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );
    def assignmentExpressionNoIn(self, ):

        retval = self.assignmentExpressionNoIn_return()
        retval.start = self.input.LT(1)
        assignmentExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT284 = None
        LT286 = None
        conditionalExpression282 = None

        leftHandSideExpression283 = None

        assignmentOperator285 = None

        assignmentExpressionNoIn287 = None


        LT284_tree = None
        LT286_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 45):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:275:2: ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn )
                alt144 = 2
                alt144 = self.dfa144.predict(self.input)
                if alt144 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:275:4: conditionalExpression
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_conditionalExpression_in_assignmentExpressionNoIn1852)
                    conditionalExpression282 = self.conditionalExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, conditionalExpression282.tree)


                elif alt144 == 2:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:276:4: leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_leftHandSideExpression_in_assignmentExpressionNoIn1857)
                    leftHandSideExpression283 = self.leftHandSideExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, leftHandSideExpression283.tree)
                    # ../src/checkjs/parsers/antlr/JavaScript.g:276:29: ( LT )*
                    while True: #loop142
                        alt142 = 2
                        LA142_0 = self.input.LA(1)

                        if (LA142_0 == LT) :
                            alt142 = 1


                        if alt142 == 1:
                            # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                            pass 
                            LT284=self.match(self.input, LT, self.FOLLOW_LT_in_assignmentExpressionNoIn1859)


                        else:
                            break #loop142
                    self._state.following.append(self.FOLLOW_assignmentOperator_in_assignmentExpressionNoIn1863)
                    assignmentOperator285 = self.assignmentOperator()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assignmentOperator285.tree)
                    # ../src/checkjs/parsers/antlr/JavaScript.g:276:53: ( LT )*
                    while True: #loop143
                        alt143 = 2
                        LA143_0 = self.input.LA(1)

                        if (LA143_0 == LT) :
                            alt143 = 1


                        if alt143 == 1:
                            # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                            pass 
                            LT286=self.match(self.input, LT, self.FOLLOW_LT_in_assignmentExpressionNoIn1865)


                        else:
                            break #loop143
                    self._state.following.append(self.FOLLOW_assignmentExpressionNoIn_in_assignmentExpressionNoIn1869)
                    assignmentExpressionNoIn287 = self.assignmentExpressionNoIn()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assignmentExpressionNoIn287.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 45, assignmentExpressionNoIn_StartIndex, success)

            pass
        return retval

    # $ANTLR end "assignmentExpressionNoIn"

    class leftHandSideExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.leftHandSideExpression_return, self).__init__()

            self.tree = None




    # $ANTLR start "leftHandSideExpression"
    # ../src/checkjs/parsers/antlr/JavaScript.g:279:1: leftHandSideExpression : memberExpression -> ^( MEMBER_EXPR memberExpression ) ;
    def leftHandSideExpression(self, ):

        retval = self.leftHandSideExpression_return()
        retval.start = self.input.LT(1)
        leftHandSideExpression_StartIndex = self.input.index()
        root_0 = None

        memberExpression288 = None


        stream_memberExpression = RewriteRuleSubtreeStream(self._adaptor, "rule memberExpression")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 46):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:280:2: ( memberExpression -> ^( MEMBER_EXPR memberExpression ) )
                # ../src/checkjs/parsers/antlr/JavaScript.g:280:4: memberExpression
                pass 
                self._state.following.append(self.FOLLOW_memberExpression_in_leftHandSideExpression1880)
                memberExpression288 = self.memberExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_memberExpression.add(memberExpression288.tree)

                # AST Rewrite
                # elements: memberExpression
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 280:21: -> ^( MEMBER_EXPR memberExpression )
                    # ../src/checkjs/parsers/antlr/JavaScript.g:280:24: ^( MEMBER_EXPR memberExpression )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(MEMBER_EXPR, "MEMBER_EXPR"), root_1)

                    self._adaptor.addChild(root_1, stream_memberExpression.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 46, leftHandSideExpression_StartIndex, success)

            pass
        return retval

    # $ANTLR end "leftHandSideExpression"

    class newExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.newExpression_return, self).__init__()

            self.tree = None




    # $ANTLR start "newExpression"
    # ../src/checkjs/parsers/antlr/JavaScript.g:283:1: newExpression : ( memberExpression | 'new' ( LT )* newExpression );
    def newExpression(self, ):

        retval = self.newExpression_return()
        retval.start = self.input.LT(1)
        newExpression_StartIndex = self.input.index()
        root_0 = None

        string_literal290 = None
        LT291 = None
        memberExpression289 = None

        newExpression292 = None


        string_literal290_tree = None
        LT291_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 47):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:284:2: ( memberExpression | 'new' ( LT )* newExpression )
                alt146 = 2
                alt146 = self.dfa146.predict(self.input)
                if alt146 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:284:4: memberExpression
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_memberExpression_in_newExpression1900)
                    memberExpression289 = self.memberExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, memberExpression289.tree)


                elif alt146 == 2:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:285:4: 'new' ( LT )* newExpression
                    pass 
                    root_0 = self._adaptor.nil()

                    string_literal290=self.match(self.input, 79, self.FOLLOW_79_in_newExpression1905)
                    if self._state.backtracking == 0:

                        string_literal290_tree = self._adaptor.createWithPayload(string_literal290)
                        self._adaptor.addChild(root_0, string_literal290_tree)

                    # ../src/checkjs/parsers/antlr/JavaScript.g:285:12: ( LT )*
                    while True: #loop145
                        alt145 = 2
                        LA145_0 = self.input.LA(1)

                        if (LA145_0 == LT) :
                            alt145 = 1


                        if alt145 == 1:
                            # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                            pass 
                            LT291=self.match(self.input, LT, self.FOLLOW_LT_in_newExpression1907)


                        else:
                            break #loop145
                    self._state.following.append(self.FOLLOW_newExpression_in_newExpression1911)
                    newExpression292 = self.newExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, newExpression292.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 47, newExpression_StartIndex, success)

            pass
        return retval

    # $ANTLR end "newExpression"

    class memberExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.memberExpression_return, self).__init__()

            self.tree = None




    # $ANTLR start "memberExpression"
    # ../src/checkjs/parsers/antlr/JavaScript.g:288:1: memberExpression : ( primaryExpression | functionExpression | 'new' ( LT )* memberExpression ( LT )* arguments ) ( ( LT )* memberExpressionSuffix )* ;
    def memberExpression(self, ):

        retval = self.memberExpression_return()
        retval.start = self.input.LT(1)
        memberExpression_StartIndex = self.input.index()
        root_0 = None

        string_literal295 = None
        LT296 = None
        LT298 = None
        LT300 = None
        primaryExpression293 = None

        functionExpression294 = None

        memberExpression297 = None

        arguments299 = None

        memberExpressionSuffix301 = None


        string_literal295_tree = None
        LT296_tree = None
        LT298_tree = None
        LT300_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 48):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:289:2: ( ( primaryExpression | functionExpression | 'new' ( LT )* memberExpression ( LT )* arguments ) ( ( LT )* memberExpressionSuffix )* )
                # ../src/checkjs/parsers/antlr/JavaScript.g:289:4: ( primaryExpression | functionExpression | 'new' ( LT )* memberExpression ( LT )* arguments ) ( ( LT )* memberExpressionSuffix )*
                pass 
                root_0 = self._adaptor.nil()

                # ../src/checkjs/parsers/antlr/JavaScript.g:289:4: ( primaryExpression | functionExpression | 'new' ( LT )* memberExpression ( LT )* arguments )
                alt149 = 3
                LA149 = self.input.LA(1)
                if LA149 == Identifier or LA149 == StringLiteral or LA149 == NumericLiteral or LA149 == 54 or LA149 == 57 or LA149 == 80 or LA149 == 115 or LA149 == 116 or LA149 == 117 or LA149 == 118 or LA149 == 119:
                    alt149 = 1
                elif LA149 == 52:
                    alt149 = 2
                elif LA149 == 79:
                    alt149 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 149, 0, self.input)

                    raise nvae

                if alt149 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:289:5: primaryExpression
                    pass 
                    self._state.following.append(self.FOLLOW_primaryExpression_in_memberExpression1923)
                    primaryExpression293 = self.primaryExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, primaryExpression293.tree)


                elif alt149 == 2:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:289:25: functionExpression
                    pass 
                    self._state.following.append(self.FOLLOW_functionExpression_in_memberExpression1927)
                    functionExpression294 = self.functionExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, functionExpression294.tree)


                elif alt149 == 3:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:289:46: 'new' ( LT )* memberExpression ( LT )* arguments
                    pass 
                    string_literal295=self.match(self.input, 79, self.FOLLOW_79_in_memberExpression1931)
                    if self._state.backtracking == 0:

                        string_literal295_tree = self._adaptor.createWithPayload(string_literal295)
                        self._adaptor.addChild(root_0, string_literal295_tree)

                    # ../src/checkjs/parsers/antlr/JavaScript.g:289:54: ( LT )*
                    while True: #loop147
                        alt147 = 2
                        LA147_0 = self.input.LA(1)

                        if (LA147_0 == LT) :
                            alt147 = 1


                        if alt147 == 1:
                            # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                            pass 
                            LT296=self.match(self.input, LT, self.FOLLOW_LT_in_memberExpression1933)


                        else:
                            break #loop147
                    self._state.following.append(self.FOLLOW_memberExpression_in_memberExpression1937)
                    memberExpression297 = self.memberExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, memberExpression297.tree)
                    # ../src/checkjs/parsers/antlr/JavaScript.g:289:76: ( LT )*
                    while True: #loop148
                        alt148 = 2
                        LA148_0 = self.input.LA(1)

                        if (LA148_0 == LT) :
                            alt148 = 1


                        if alt148 == 1:
                            # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                            pass 
                            LT298=self.match(self.input, LT, self.FOLLOW_LT_in_memberExpression1939)


                        else:
                            break #loop148
                    self._state.following.append(self.FOLLOW_arguments_in_memberExpression1943)
                    arguments299 = self.arguments()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, arguments299.tree)



                # ../src/checkjs/parsers/antlr/JavaScript.g:289:90: ( ( LT )* memberExpressionSuffix )*
                while True: #loop151
                    alt151 = 2
                    alt151 = self.dfa151.predict(self.input)
                    if alt151 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:289:91: ( LT )* memberExpressionSuffix
                        pass 
                        # ../src/checkjs/parsers/antlr/JavaScript.g:289:93: ( LT )*
                        while True: #loop150
                            alt150 = 2
                            LA150_0 = self.input.LA(1)

                            if (LA150_0 == LT) :
                                alt150 = 1


                            if alt150 == 1:
                                # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                                pass 
                                LT300=self.match(self.input, LT, self.FOLLOW_LT_in_memberExpression1947)


                            else:
                                break #loop150
                        self._state.following.append(self.FOLLOW_memberExpressionSuffix_in_memberExpression1951)
                        memberExpressionSuffix301 = self.memberExpressionSuffix()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, memberExpressionSuffix301.tree)


                    else:
                        break #loop151



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 48, memberExpression_StartIndex, success)

            pass
        return retval

    # $ANTLR end "memberExpression"

    class memberExpressionSuffix_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.memberExpressionSuffix_return, self).__init__()

            self.tree = None




    # $ANTLR start "memberExpressionSuffix"
    # ../src/checkjs/parsers/antlr/JavaScript.g:292:1: memberExpressionSuffix : ( indexSuffix | propertyReferenceSuffix );
    def memberExpressionSuffix(self, ):

        retval = self.memberExpressionSuffix_return()
        retval.start = self.input.LT(1)
        memberExpressionSuffix_StartIndex = self.input.index()
        root_0 = None

        indexSuffix302 = None

        propertyReferenceSuffix303 = None



        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 49):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:293:2: ( indexSuffix | propertyReferenceSuffix )
                alt152 = 2
                LA152_0 = self.input.LA(1)

                if (LA152_0 == 80) :
                    alt152 = 1
                elif (LA152_0 == 82) :
                    alt152 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 152, 0, self.input)

                    raise nvae

                if alt152 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:293:4: indexSuffix
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_indexSuffix_in_memberExpressionSuffix1964)
                    indexSuffix302 = self.indexSuffix()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, indexSuffix302.tree)


                elif alt152 == 2:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:294:4: propertyReferenceSuffix
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_propertyReferenceSuffix_in_memberExpressionSuffix1969)
                    propertyReferenceSuffix303 = self.propertyReferenceSuffix()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, propertyReferenceSuffix303.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 49, memberExpressionSuffix_StartIndex, success)

            pass
        return retval

    # $ANTLR end "memberExpressionSuffix"

    class callExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.callExpression_return, self).__init__()

            self.tree = None




    # $ANTLR start "callExpression"
    # ../src/checkjs/parsers/antlr/JavaScript.g:297:1: callExpression : memberExpression ( LT )* arguments ( ( LT )* callExpressionSuffix )* -> ^( CALL ^( CALL_IDENTIFIER memberExpression ) arguments ( callExpressionSuffix )* ) ;
    def callExpression(self, ):

        retval = self.callExpression_return()
        retval.start = self.input.LT(1)
        callExpression_StartIndex = self.input.index()
        root_0 = None

        LT305 = None
        LT307 = None
        memberExpression304 = None

        arguments306 = None

        callExpressionSuffix308 = None


        LT305_tree = None
        LT307_tree = None
        stream_LT = RewriteRuleTokenStream(self._adaptor, "token LT")
        stream_memberExpression = RewriteRuleSubtreeStream(self._adaptor, "rule memberExpression")
        stream_arguments = RewriteRuleSubtreeStream(self._adaptor, "rule arguments")
        stream_callExpressionSuffix = RewriteRuleSubtreeStream(self._adaptor, "rule callExpressionSuffix")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 50):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:298:2: ( memberExpression ( LT )* arguments ( ( LT )* callExpressionSuffix )* -> ^( CALL ^( CALL_IDENTIFIER memberExpression ) arguments ( callExpressionSuffix )* ) )
                # ../src/checkjs/parsers/antlr/JavaScript.g:298:4: memberExpression ( LT )* arguments ( ( LT )* callExpressionSuffix )*
                pass 
                self._state.following.append(self.FOLLOW_memberExpression_in_callExpression1980)
                memberExpression304 = self.memberExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_memberExpression.add(memberExpression304.tree)
                # ../src/checkjs/parsers/antlr/JavaScript.g:298:21: ( LT )*
                while True: #loop153
                    alt153 = 2
                    LA153_0 = self.input.LA(1)

                    if (LA153_0 == LT) :
                        alt153 = 1


                    if alt153 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT305=self.match(self.input, LT, self.FOLLOW_LT_in_callExpression1982) 
                        if self._state.backtracking == 0:
                            stream_LT.add(LT305)


                    else:
                        break #loop153
                self._state.following.append(self.FOLLOW_arguments_in_callExpression1985)
                arguments306 = self.arguments()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_arguments.add(arguments306.tree)
                # ../src/checkjs/parsers/antlr/JavaScript.g:298:35: ( ( LT )* callExpressionSuffix )*
                while True: #loop155
                    alt155 = 2
                    alt155 = self.dfa155.predict(self.input)
                    if alt155 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:298:36: ( LT )* callExpressionSuffix
                        pass 
                        # ../src/checkjs/parsers/antlr/JavaScript.g:298:36: ( LT )*
                        while True: #loop154
                            alt154 = 2
                            LA154_0 = self.input.LA(1)

                            if (LA154_0 == LT) :
                                alt154 = 1


                            if alt154 == 1:
                                # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                                pass 
                                LT307=self.match(self.input, LT, self.FOLLOW_LT_in_callExpression1988) 
                                if self._state.backtracking == 0:
                                    stream_LT.add(LT307)


                            else:
                                break #loop154
                        self._state.following.append(self.FOLLOW_callExpressionSuffix_in_callExpression1991)
                        callExpressionSuffix308 = self.callExpressionSuffix()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_callExpressionSuffix.add(callExpressionSuffix308.tree)


                    else:
                        break #loop155

                # AST Rewrite
                # elements: memberExpression, callExpressionSuffix, arguments
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 298:63: -> ^( CALL ^( CALL_IDENTIFIER memberExpression ) arguments ( callExpressionSuffix )* )
                    # ../src/checkjs/parsers/antlr/JavaScript.g:299:9: ^( CALL ^( CALL_IDENTIFIER memberExpression ) arguments ( callExpressionSuffix )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(CALL, "CALL"), root_1)

                    # ../src/checkjs/parsers/antlr/JavaScript.g:299:16: ^( CALL_IDENTIFIER memberExpression )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(CALL_IDENTIFIER, "CALL_IDENTIFIER"), root_2)

                    self._adaptor.addChild(root_2, stream_memberExpression.nextTree())

                    self._adaptor.addChild(root_1, root_2)
                    self._adaptor.addChild(root_1, stream_arguments.nextTree())
                    # ../src/checkjs/parsers/antlr/JavaScript.g:299:62: ( callExpressionSuffix )*
                    while stream_callExpressionSuffix.hasNext():
                        self._adaptor.addChild(root_1, stream_callExpressionSuffix.nextTree())


                    stream_callExpressionSuffix.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 50, callExpression_StartIndex, success)

            pass
        return retval

    # $ANTLR end "callExpression"

    class callExpressionSuffix_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.callExpressionSuffix_return, self).__init__()

            self.tree = None




    # $ANTLR start "callExpressionSuffix"
    # ../src/checkjs/parsers/antlr/JavaScript.g:302:1: callExpressionSuffix : ( arguments | indexSuffix | propertyReferenceSuffix );
    def callExpressionSuffix(self, ):

        retval = self.callExpressionSuffix_return()
        retval.start = self.input.LT(1)
        callExpressionSuffix_StartIndex = self.input.index()
        root_0 = None

        arguments309 = None

        indexSuffix310 = None

        propertyReferenceSuffix311 = None



        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 51):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:303:2: ( arguments | indexSuffix | propertyReferenceSuffix )
                alt156 = 3
                LA156 = self.input.LA(1)
                if LA156 == 54:
                    alt156 = 1
                elif LA156 == 80:
                    alt156 = 2
                elif LA156 == 82:
                    alt156 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 156, 0, self.input)

                    raise nvae

                if alt156 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:303:4: arguments
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_arguments_in_callExpressionSuffix2029)
                    arguments309 = self.arguments()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, arguments309.tree)


                elif alt156 == 2:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:304:4: indexSuffix
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_indexSuffix_in_callExpressionSuffix2034)
                    indexSuffix310 = self.indexSuffix()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, indexSuffix310.tree)


                elif alt156 == 3:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:305:4: propertyReferenceSuffix
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_propertyReferenceSuffix_in_callExpressionSuffix2039)
                    propertyReferenceSuffix311 = self.propertyReferenceSuffix()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, propertyReferenceSuffix311.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 51, callExpressionSuffix_StartIndex, success)

            pass
        return retval

    # $ANTLR end "callExpressionSuffix"

    class arguments_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.arguments_return, self).__init__()

            self.tree = None




    # $ANTLR start "arguments"
    # ../src/checkjs/parsers/antlr/JavaScript.g:308:1: arguments : '(' ( ( LT )* assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )* )? ( LT )* ')' -> ^( CALL_ARGUMENTS ( assignmentExpression )* ) ;
    def arguments(self, ):

        retval = self.arguments_return()
        retval.start = self.input.LT(1)
        arguments_StartIndex = self.input.index()
        root_0 = None

        char_literal312 = None
        LT313 = None
        LT315 = None
        char_literal316 = None
        LT317 = None
        LT319 = None
        char_literal320 = None
        assignmentExpression314 = None

        assignmentExpression318 = None


        char_literal312_tree = None
        LT313_tree = None
        LT315_tree = None
        char_literal316_tree = None
        LT317_tree = None
        LT319_tree = None
        char_literal320_tree = None
        stream_LT = RewriteRuleTokenStream(self._adaptor, "token LT")
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_55 = RewriteRuleTokenStream(self._adaptor, "token 55")
        stream_54 = RewriteRuleTokenStream(self._adaptor, "token 54")
        stream_assignmentExpression = RewriteRuleSubtreeStream(self._adaptor, "rule assignmentExpression")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 52):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:309:2: ( '(' ( ( LT )* assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )* )? ( LT )* ')' -> ^( CALL_ARGUMENTS ( assignmentExpression )* ) )
                # ../src/checkjs/parsers/antlr/JavaScript.g:309:4: '(' ( ( LT )* assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )* )? ( LT )* ')'
                pass 
                char_literal312=self.match(self.input, 54, self.FOLLOW_54_in_arguments2050) 
                if self._state.backtracking == 0:
                    stream_54.add(char_literal312)
                # ../src/checkjs/parsers/antlr/JavaScript.g:309:8: ( ( LT )* assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )* )?
                alt161 = 2
                alt161 = self.dfa161.predict(self.input)
                if alt161 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:309:9: ( LT )* assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )*
                    pass 
                    # ../src/checkjs/parsers/antlr/JavaScript.g:309:9: ( LT )*
                    while True: #loop157
                        alt157 = 2
                        LA157_0 = self.input.LA(1)

                        if (LA157_0 == LT) :
                            alt157 = 1


                        if alt157 == 1:
                            # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                            pass 
                            LT313=self.match(self.input, LT, self.FOLLOW_LT_in_arguments2053) 
                            if self._state.backtracking == 0:
                                stream_LT.add(LT313)


                        else:
                            break #loop157
                    self._state.following.append(self.FOLLOW_assignmentExpression_in_arguments2056)
                    assignmentExpression314 = self.assignmentExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_assignmentExpression.add(assignmentExpression314.tree)
                    # ../src/checkjs/parsers/antlr/JavaScript.g:309:34: ( ( LT )* ',' ( LT )* assignmentExpression )*
                    while True: #loop160
                        alt160 = 2
                        alt160 = self.dfa160.predict(self.input)
                        if alt160 == 1:
                            # ../src/checkjs/parsers/antlr/JavaScript.g:309:35: ( LT )* ',' ( LT )* assignmentExpression
                            pass 
                            # ../src/checkjs/parsers/antlr/JavaScript.g:309:35: ( LT )*
                            while True: #loop158
                                alt158 = 2
                                LA158_0 = self.input.LA(1)

                                if (LA158_0 == LT) :
                                    alt158 = 1


                                if alt158 == 1:
                                    # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                                    pass 
                                    LT315=self.match(self.input, LT, self.FOLLOW_LT_in_arguments2059) 
                                    if self._state.backtracking == 0:
                                        stream_LT.add(LT315)


                                else:
                                    break #loop158
                            char_literal316=self.match(self.input, 55, self.FOLLOW_55_in_arguments2062) 
                            if self._state.backtracking == 0:
                                stream_55.add(char_literal316)
                            # ../src/checkjs/parsers/antlr/JavaScript.g:309:43: ( LT )*
                            while True: #loop159
                                alt159 = 2
                                LA159_0 = self.input.LA(1)

                                if (LA159_0 == LT) :
                                    alt159 = 1


                                if alt159 == 1:
                                    # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                                    pass 
                                    LT317=self.match(self.input, LT, self.FOLLOW_LT_in_arguments2064) 
                                    if self._state.backtracking == 0:
                                        stream_LT.add(LT317)


                                else:
                                    break #loop159
                            self._state.following.append(self.FOLLOW_assignmentExpression_in_arguments2067)
                            assignmentExpression318 = self.assignmentExpression()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_assignmentExpression.add(assignmentExpression318.tree)


                        else:
                            break #loop160



                # ../src/checkjs/parsers/antlr/JavaScript.g:309:73: ( LT )*
                while True: #loop162
                    alt162 = 2
                    LA162_0 = self.input.LA(1)

                    if (LA162_0 == LT) :
                        alt162 = 1


                    if alt162 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT319=self.match(self.input, LT, self.FOLLOW_LT_in_arguments2074) 
                        if self._state.backtracking == 0:
                            stream_LT.add(LT319)


                    else:
                        break #loop162
                char_literal320=self.match(self.input, 56, self.FOLLOW_56_in_arguments2077) 
                if self._state.backtracking == 0:
                    stream_56.add(char_literal320)

                # AST Rewrite
                # elements: assignmentExpression
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 309:81: -> ^( CALL_ARGUMENTS ( assignmentExpression )* )
                    # ../src/checkjs/parsers/antlr/JavaScript.g:310:9: ^( CALL_ARGUMENTS ( assignmentExpression )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(CALL_ARGUMENTS, "CALL_ARGUMENTS"), root_1)

                    # ../src/checkjs/parsers/antlr/JavaScript.g:310:27: ( assignmentExpression )*
                    while stream_assignmentExpression.hasNext():
                        self._adaptor.addChild(root_1, stream_assignmentExpression.nextTree())


                    stream_assignmentExpression.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 52, arguments_StartIndex, success)

            pass
        return retval

    # $ANTLR end "arguments"

    class indexSuffix_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.indexSuffix_return, self).__init__()

            self.tree = None




    # $ANTLR start "indexSuffix"
    # ../src/checkjs/parsers/antlr/JavaScript.g:313:1: indexSuffix : '[' ( LT )* expression ( LT )* ']' -> ^( INDEX expression ) ;
    def indexSuffix(self, ):

        retval = self.indexSuffix_return()
        retval.start = self.input.LT(1)
        indexSuffix_StartIndex = self.input.index()
        root_0 = None

        char_literal321 = None
        LT322 = None
        LT324 = None
        char_literal325 = None
        expression323 = None


        char_literal321_tree = None
        LT322_tree = None
        LT324_tree = None
        char_literal325_tree = None
        stream_LT = RewriteRuleTokenStream(self._adaptor, "token LT")
        stream_80 = RewriteRuleTokenStream(self._adaptor, "token 80")
        stream_81 = RewriteRuleTokenStream(self._adaptor, "token 81")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 53):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:314:2: ( '[' ( LT )* expression ( LT )* ']' -> ^( INDEX expression ) )
                # ../src/checkjs/parsers/antlr/JavaScript.g:314:4: '[' ( LT )* expression ( LT )* ']'
                pass 
                char_literal321=self.match(self.input, 80, self.FOLLOW_80_in_indexSuffix2106) 
                if self._state.backtracking == 0:
                    stream_80.add(char_literal321)
                # ../src/checkjs/parsers/antlr/JavaScript.g:314:8: ( LT )*
                while True: #loop163
                    alt163 = 2
                    LA163_0 = self.input.LA(1)

                    if (LA163_0 == LT) :
                        alt163 = 1


                    if alt163 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT322=self.match(self.input, LT, self.FOLLOW_LT_in_indexSuffix2108) 
                        if self._state.backtracking == 0:
                            stream_LT.add(LT322)


                    else:
                        break #loop163
                self._state.following.append(self.FOLLOW_expression_in_indexSuffix2111)
                expression323 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expression.add(expression323.tree)
                # ../src/checkjs/parsers/antlr/JavaScript.g:314:23: ( LT )*
                while True: #loop164
                    alt164 = 2
                    LA164_0 = self.input.LA(1)

                    if (LA164_0 == LT) :
                        alt164 = 1


                    if alt164 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT324=self.match(self.input, LT, self.FOLLOW_LT_in_indexSuffix2113) 
                        if self._state.backtracking == 0:
                            stream_LT.add(LT324)


                    else:
                        break #loop164
                char_literal325=self.match(self.input, 81, self.FOLLOW_81_in_indexSuffix2116) 
                if self._state.backtracking == 0:
                    stream_81.add(char_literal325)

                # AST Rewrite
                # elements: expression
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 314:31: -> ^( INDEX expression )
                    # ../src/checkjs/parsers/antlr/JavaScript.g:314:34: ^( INDEX expression )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(INDEX, "INDEX"), root_1)

                    self._adaptor.addChild(root_1, stream_expression.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 53, indexSuffix_StartIndex, success)

            pass
        return retval

    # $ANTLR end "indexSuffix"

    class propertyReferenceSuffix_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.propertyReferenceSuffix_return, self).__init__()

            self.tree = None




    # $ANTLR start "propertyReferenceSuffix"
    # ../src/checkjs/parsers/antlr/JavaScript.g:317:1: propertyReferenceSuffix : '.' ( LT )* Identifier -> ^( MEMBER Identifier ) ;
    def propertyReferenceSuffix(self, ):

        retval = self.propertyReferenceSuffix_return()
        retval.start = self.input.LT(1)
        propertyReferenceSuffix_StartIndex = self.input.index()
        root_0 = None

        char_literal326 = None
        LT327 = None
        Identifier328 = None

        char_literal326_tree = None
        LT327_tree = None
        Identifier328_tree = None
        stream_LT = RewriteRuleTokenStream(self._adaptor, "token LT")
        stream_82 = RewriteRuleTokenStream(self._adaptor, "token 82")
        stream_Identifier = RewriteRuleTokenStream(self._adaptor, "token Identifier")

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 54):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:318:2: ( '.' ( LT )* Identifier -> ^( MEMBER Identifier ) )
                # ../src/checkjs/parsers/antlr/JavaScript.g:318:4: '.' ( LT )* Identifier
                pass 
                char_literal326=self.match(self.input, 82, self.FOLLOW_82_in_propertyReferenceSuffix2136) 
                if self._state.backtracking == 0:
                    stream_82.add(char_literal326)
                # ../src/checkjs/parsers/antlr/JavaScript.g:318:8: ( LT )*
                while True: #loop165
                    alt165 = 2
                    LA165_0 = self.input.LA(1)

                    if (LA165_0 == LT) :
                        alt165 = 1


                    if alt165 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT327=self.match(self.input, LT, self.FOLLOW_LT_in_propertyReferenceSuffix2138) 
                        if self._state.backtracking == 0:
                            stream_LT.add(LT327)


                    else:
                        break #loop165
                Identifier328=self.match(self.input, Identifier, self.FOLLOW_Identifier_in_propertyReferenceSuffix2141) 
                if self._state.backtracking == 0:
                    stream_Identifier.add(Identifier328)

                # AST Rewrite
                # elements: Identifier
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 318:23: -> ^( MEMBER Identifier )
                    # ../src/checkjs/parsers/antlr/JavaScript.g:318:26: ^( MEMBER Identifier )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(MEMBER, "MEMBER"), root_1)

                    self._adaptor.addChild(root_1, stream_Identifier.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 54, propertyReferenceSuffix_StartIndex, success)

            pass
        return retval

    # $ANTLR end "propertyReferenceSuffix"

    class assignmentOperator_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.assignmentOperator_return, self).__init__()

            self.tree = None




    # $ANTLR start "assignmentOperator"
    # ../src/checkjs/parsers/antlr/JavaScript.g:321:1: assignmentOperator : ( '=' | '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '>>>=' | '&=' | '^=' | '|=' );
    def assignmentOperator(self, ):

        retval = self.assignmentOperator_return()
        retval.start = self.input.LT(1)
        assignmentOperator_StartIndex = self.input.index()
        root_0 = None

        set329 = None

        set329_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 55):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:322:2: ( '=' | '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '>>>=' | '&=' | '^=' | '|=' )
                # ../src/checkjs/parsers/antlr/JavaScript.g:
                pass 
                root_0 = self._adaptor.nil()

                set329 = self.input.LT(1)
                if self.input.LA(1) == 60 or (83 <= self.input.LA(1) <= 93):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set329))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 55, assignmentOperator_StartIndex, success)

            pass
        return retval

    # $ANTLR end "assignmentOperator"

    class conditionalExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.conditionalExpression_return, self).__init__()

            self.tree = None




    # $ANTLR start "conditionalExpression"
    # ../src/checkjs/parsers/antlr/JavaScript.g:325:1: conditionalExpression : operatorExpression ( ( LT )* '?' ( LT )* operatorExpression ( LT )* ':' ( LT )* operatorExpression )? ;
    def conditionalExpression(self, ):

        retval = self.conditionalExpression_return()
        retval.start = self.input.LT(1)
        conditionalExpression_StartIndex = self.input.index()
        root_0 = None

        LT331 = None
        char_literal332 = None
        LT333 = None
        LT335 = None
        char_literal336 = None
        LT337 = None
        operatorExpression330 = None

        operatorExpression334 = None

        operatorExpression338 = None


        LT331_tree = None
        char_literal332_tree = None
        LT333_tree = None
        LT335_tree = None
        char_literal336_tree = None
        LT337_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 56):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:326:2: ( operatorExpression ( ( LT )* '?' ( LT )* operatorExpression ( LT )* ':' ( LT )* operatorExpression )? )
                # ../src/checkjs/parsers/antlr/JavaScript.g:326:4: operatorExpression ( ( LT )* '?' ( LT )* operatorExpression ( LT )* ':' ( LT )* operatorExpression )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_operatorExpression_in_conditionalExpression2216)
                operatorExpression330 = self.operatorExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, operatorExpression330.tree)
                # ../src/checkjs/parsers/antlr/JavaScript.g:326:23: ( ( LT )* '?' ( LT )* operatorExpression ( LT )* ':' ( LT )* operatorExpression )?
                alt170 = 2
                alt170 = self.dfa170.predict(self.input)
                if alt170 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:326:24: ( LT )* '?' ( LT )* operatorExpression ( LT )* ':' ( LT )* operatorExpression
                    pass 
                    # ../src/checkjs/parsers/antlr/JavaScript.g:326:26: ( LT )*
                    while True: #loop166
                        alt166 = 2
                        LA166_0 = self.input.LA(1)

                        if (LA166_0 == LT) :
                            alt166 = 1


                        if alt166 == 1:
                            # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                            pass 
                            LT331=self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpression2219)


                        else:
                            break #loop166
                    char_literal332=self.match(self.input, 94, self.FOLLOW_94_in_conditionalExpression2223)
                    if self._state.backtracking == 0:

                        char_literal332_tree = self._adaptor.createWithPayload(char_literal332)
                        self._adaptor.addChild(root_0, char_literal332_tree)

                    # ../src/checkjs/parsers/antlr/JavaScript.g:326:35: ( LT )*
                    while True: #loop167
                        alt167 = 2
                        LA167_0 = self.input.LA(1)

                        if (LA167_0 == LT) :
                            alt167 = 1


                        if alt167 == 1:
                            # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                            pass 
                            LT333=self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpression2225)


                        else:
                            break #loop167
                    self._state.following.append(self.FOLLOW_operatorExpression_in_conditionalExpression2229)
                    operatorExpression334 = self.operatorExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, operatorExpression334.tree)
                    # ../src/checkjs/parsers/antlr/JavaScript.g:326:59: ( LT )*
                    while True: #loop168
                        alt168 = 2
                        LA168_0 = self.input.LA(1)

                        if (LA168_0 == LT) :
                            alt168 = 1


                        if alt168 == 1:
                            # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                            pass 
                            LT335=self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpression2231)


                        else:
                            break #loop168
                    char_literal336=self.match(self.input, 71, self.FOLLOW_71_in_conditionalExpression2235)
                    if self._state.backtracking == 0:

                        char_literal336_tree = self._adaptor.createWithPayload(char_literal336)
                        self._adaptor.addChild(root_0, char_literal336_tree)

                    # ../src/checkjs/parsers/antlr/JavaScript.g:326:68: ( LT )*
                    while True: #loop169
                        alt169 = 2
                        LA169_0 = self.input.LA(1)

                        if (LA169_0 == LT) :
                            alt169 = 1


                        if alt169 == 1:
                            # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                            pass 
                            LT337=self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpression2237)


                        else:
                            break #loop169
                    self._state.following.append(self.FOLLOW_operatorExpression_in_conditionalExpression2241)
                    operatorExpression338 = self.operatorExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, operatorExpression338.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 56, conditionalExpression_StartIndex, success)

            pass
        return retval

    # $ANTLR end "conditionalExpression"

    class operatorExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.operatorExpression_return, self).__init__()

            self.tree = None




    # $ANTLR start "operatorExpression"
    # ../src/checkjs/parsers/antlr/JavaScript.g:329:1: operatorExpression : ( ( leftHandSideExpression ( LT )* nonAssignmentOperator ( LT )* assignmentExpression -> ^( nonAssignmentOperator ^( OPERATOR_ARG leftHandSideExpression ) ^( OPERATOR_ARG assignmentExpression ) ) ) | unaryExpression );
    def operatorExpression(self, ):

        retval = self.operatorExpression_return()
        retval.start = self.input.LT(1)
        operatorExpression_StartIndex = self.input.index()
        root_0 = None

        LT340 = None
        LT342 = None
        leftHandSideExpression339 = None

        nonAssignmentOperator341 = None

        assignmentExpression343 = None

        unaryExpression344 = None


        LT340_tree = None
        LT342_tree = None
        stream_LT = RewriteRuleTokenStream(self._adaptor, "token LT")
        stream_leftHandSideExpression = RewriteRuleSubtreeStream(self._adaptor, "rule leftHandSideExpression")
        stream_nonAssignmentOperator = RewriteRuleSubtreeStream(self._adaptor, "rule nonAssignmentOperator")
        stream_assignmentExpression = RewriteRuleSubtreeStream(self._adaptor, "rule assignmentExpression")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 57):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:330:5: ( ( leftHandSideExpression ( LT )* nonAssignmentOperator ( LT )* assignmentExpression -> ^( nonAssignmentOperator ^( OPERATOR_ARG leftHandSideExpression ) ^( OPERATOR_ARG assignmentExpression ) ) ) | unaryExpression )
                alt173 = 2
                alt173 = self.dfa173.predict(self.input)
                if alt173 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:330:7: ( leftHandSideExpression ( LT )* nonAssignmentOperator ( LT )* assignmentExpression -> ^( nonAssignmentOperator ^( OPERATOR_ARG leftHandSideExpression ) ^( OPERATOR_ARG assignmentExpression ) ) )
                    pass 
                    # ../src/checkjs/parsers/antlr/JavaScript.g:330:7: ( leftHandSideExpression ( LT )* nonAssignmentOperator ( LT )* assignmentExpression -> ^( nonAssignmentOperator ^( OPERATOR_ARG leftHandSideExpression ) ^( OPERATOR_ARG assignmentExpression ) ) )
                    # ../src/checkjs/parsers/antlr/JavaScript.g:330:8: leftHandSideExpression ( LT )* nonAssignmentOperator ( LT )* assignmentExpression
                    pass 
                    self._state.following.append(self.FOLLOW_leftHandSideExpression_in_operatorExpression2258)
                    leftHandSideExpression339 = self.leftHandSideExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_leftHandSideExpression.add(leftHandSideExpression339.tree)
                    # ../src/checkjs/parsers/antlr/JavaScript.g:330:31: ( LT )*
                    while True: #loop171
                        alt171 = 2
                        LA171_0 = self.input.LA(1)

                        if (LA171_0 == LT) :
                            alt171 = 1


                        if alt171 == 1:
                            # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                            pass 
                            LT340=self.match(self.input, LT, self.FOLLOW_LT_in_operatorExpression2260) 
                            if self._state.backtracking == 0:
                                stream_LT.add(LT340)


                        else:
                            break #loop171
                    self._state.following.append(self.FOLLOW_nonAssignmentOperator_in_operatorExpression2263)
                    nonAssignmentOperator341 = self.nonAssignmentOperator()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_nonAssignmentOperator.add(nonAssignmentOperator341.tree)
                    # ../src/checkjs/parsers/antlr/JavaScript.g:330:57: ( LT )*
                    while True: #loop172
                        alt172 = 2
                        LA172_0 = self.input.LA(1)

                        if (LA172_0 == LT) :
                            alt172 = 1


                        if alt172 == 1:
                            # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                            pass 
                            LT342=self.match(self.input, LT, self.FOLLOW_LT_in_operatorExpression2265) 
                            if self._state.backtracking == 0:
                                stream_LT.add(LT342)


                        else:
                            break #loop172
                    self._state.following.append(self.FOLLOW_assignmentExpression_in_operatorExpression2268)
                    assignmentExpression343 = self.assignmentExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_assignmentExpression.add(assignmentExpression343.tree)

                    # AST Rewrite
                    # elements: assignmentExpression, leftHandSideExpression, nonAssignmentOperator
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 330:82: -> ^( nonAssignmentOperator ^( OPERATOR_ARG leftHandSideExpression ) ^( OPERATOR_ARG assignmentExpression ) )
                        # ../src/checkjs/parsers/antlr/JavaScript.g:331:13: ^( nonAssignmentOperator ^( OPERATOR_ARG leftHandSideExpression ) ^( OPERATOR_ARG assignmentExpression ) )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(stream_nonAssignmentOperator.nextNode(), root_1)

                        # ../src/checkjs/parsers/antlr/JavaScript.g:332:17: ^( OPERATOR_ARG leftHandSideExpression )
                        root_2 = self._adaptor.nil()
                        root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(OPERATOR_ARG, "OPERATOR_ARG"), root_2)

                        self._adaptor.addChild(root_2, stream_leftHandSideExpression.nextTree())

                        self._adaptor.addChild(root_1, root_2)
                        # ../src/checkjs/parsers/antlr/JavaScript.g:333:17: ^( OPERATOR_ARG assignmentExpression )
                        root_2 = self._adaptor.nil()
                        root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(OPERATOR_ARG, "OPERATOR_ARG"), root_2)

                        self._adaptor.addChild(root_2, stream_assignmentExpression.nextTree())

                        self._adaptor.addChild(root_1, root_2)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0





                elif alt173 == 2:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:336:7: unaryExpression
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_unaryExpression_in_operatorExpression2362)
                    unaryExpression344 = self.unaryExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, unaryExpression344.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 57, operatorExpression_StartIndex, success)

            pass
        return retval

    # $ANTLR end "operatorExpression"

    class nonAssignmentOperator_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.nonAssignmentOperator_return, self).__init__()

            self.tree = None




    # $ANTLR start "nonAssignmentOperator"
    # ../src/checkjs/parsers/antlr/JavaScript.g:339:1: nonAssignmentOperator : ( '*' | '-' | '+' | '/' | '&' | '&&' | '|' | '||' | '<' | '<=' | '>' | '>=' | '==' | '!=' | '?' | ':' );
    def nonAssignmentOperator(self, ):

        retval = self.nonAssignmentOperator_return()
        retval.start = self.input.LT(1)
        nonAssignmentOperator_StartIndex = self.input.index()
        root_0 = None

        set345 = None

        set345_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 58):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:340:5: ( '*' | '-' | '+' | '/' | '&' | '&&' | '|' | '||' | '<' | '<=' | '>' | '>=' | '==' | '!=' | '?' | ':' )
                # ../src/checkjs/parsers/antlr/JavaScript.g:
                pass 
                root_0 = self._adaptor.nil()

                set345 = self.input.LT(1)
                if self.input.LA(1) == SingleSlash or self.input.LA(1) == 71 or (94 <= self.input.LA(1) <= 107):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set345))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 58, nonAssignmentOperator_StartIndex, success)

            pass
        return retval

    # $ANTLR end "nonAssignmentOperator"

    class unaryExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.unaryExpression_return, self).__init__()

            self.tree = None




    # $ANTLR start "unaryExpression"
    # ../src/checkjs/parsers/antlr/JavaScript.g:344:1: unaryExpression : ( postfixExpression | ( 'delete' | 'void' | 'typeof' | '++' | '--' | '+' | '-' | '~' | '!' ) unaryExpression );
    def unaryExpression(self, ):

        retval = self.unaryExpression_return()
        retval.start = self.input.LT(1)
        unaryExpression_StartIndex = self.input.index()
        root_0 = None

        set347 = None
        postfixExpression346 = None

        unaryExpression348 = None


        set347_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 59):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:345:2: ( postfixExpression | ( 'delete' | 'void' | 'typeof' | '++' | '--' | '+' | '-' | '~' | '!' ) unaryExpression )
                alt174 = 2
                LA174_0 = self.input.LA(1)

                if ((Identifier <= LA174_0 <= NumericLiteral) or LA174_0 == 52 or LA174_0 == 54 or LA174_0 == 57 or (79 <= LA174_0 <= 80) or (115 <= LA174_0 <= 119)) :
                    alt174 = 1
                elif ((96 <= LA174_0 <= 97) or (108 <= LA174_0 <= 114)) :
                    alt174 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 174, 0, self.input)

                    raise nvae

                if alt174 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:345:4: postfixExpression
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_postfixExpression_in_unaryExpression2454)
                    postfixExpression346 = self.postfixExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, postfixExpression346.tree)


                elif alt174 == 2:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:346:4: ( 'delete' | 'void' | 'typeof' | '++' | '--' | '+' | '-' | '~' | '!' ) unaryExpression
                    pass 
                    root_0 = self._adaptor.nil()

                    set347 = self.input.LT(1)
                    if (96 <= self.input.LA(1) <= 97) or (108 <= self.input.LA(1) <= 114):
                        self.input.consume()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set347))
                        self._state.errorRecovery = False

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        raise mse


                    self._state.following.append(self.FOLLOW_unaryExpression_in_unaryExpression2495)
                    unaryExpression348 = self.unaryExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, unaryExpression348.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 59, unaryExpression_StartIndex, success)

            pass
        return retval

    # $ANTLR end "unaryExpression"

    class postfixExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.postfixExpression_return, self).__init__()

            self.tree = None




    # $ANTLR start "postfixExpression"
    # ../src/checkjs/parsers/antlr/JavaScript.g:349:1: postfixExpression : leftHandSideExpression ( '++' | '--' )? ;
    def postfixExpression(self, ):

        retval = self.postfixExpression_return()
        retval.start = self.input.LT(1)
        postfixExpression_StartIndex = self.input.index()
        root_0 = None

        set350 = None
        leftHandSideExpression349 = None


        set350_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 60):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:350:2: ( leftHandSideExpression ( '++' | '--' )? )
                # ../src/checkjs/parsers/antlr/JavaScript.g:350:4: leftHandSideExpression ( '++' | '--' )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_leftHandSideExpression_in_postfixExpression2506)
                leftHandSideExpression349 = self.leftHandSideExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, leftHandSideExpression349.tree)
                # ../src/checkjs/parsers/antlr/JavaScript.g:350:27: ( '++' | '--' )?
                alt175 = 2
                LA175_0 = self.input.LA(1)

                if ((111 <= LA175_0 <= 112)) :
                    alt175 = 1
                if alt175 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:
                    pass 
                    set350 = self.input.LT(1)
                    if (111 <= self.input.LA(1) <= 112):
                        self.input.consume()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set350))
                        self._state.errorRecovery = False

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        raise mse








                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 60, postfixExpression_StartIndex, success)

            pass
        return retval

    # $ANTLR end "postfixExpression"

    class primaryExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.primaryExpression_return, self).__init__()

            self.tree = None




    # $ANTLR start "primaryExpression"
    # ../src/checkjs/parsers/antlr/JavaScript.g:353:1: primaryExpression : ( 'this' | Identifier | literal | arrayLiteral | objectLiteral | '(' ( LT )* expression ( LT )* ')' );
    def primaryExpression(self, ):

        retval = self.primaryExpression_return()
        retval.start = self.input.LT(1)
        primaryExpression_StartIndex = self.input.index()
        root_0 = None

        string_literal351 = None
        Identifier352 = None
        char_literal356 = None
        LT357 = None
        LT359 = None
        char_literal360 = None
        literal353 = None

        arrayLiteral354 = None

        objectLiteral355 = None

        expression358 = None


        string_literal351_tree = None
        Identifier352_tree = None
        char_literal356_tree = None
        LT357_tree = None
        LT359_tree = None
        char_literal360_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 61):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:354:2: ( 'this' | Identifier | literal | arrayLiteral | objectLiteral | '(' ( LT )* expression ( LT )* ')' )
                alt178 = 6
                LA178 = self.input.LA(1)
                if LA178 == 115:
                    alt178 = 1
                elif LA178 == Identifier:
                    alt178 = 2
                elif LA178 == StringLiteral or LA178 == NumericLiteral or LA178 == 116 or LA178 == 117 or LA178 == 118 or LA178 == 119:
                    alt178 = 3
                elif LA178 == 80:
                    alt178 = 4
                elif LA178 == 57:
                    alt178 = 5
                elif LA178 == 54:
                    alt178 = 6
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 178, 0, self.input)

                    raise nvae

                if alt178 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:354:4: 'this'
                    pass 
                    root_0 = self._adaptor.nil()

                    string_literal351=self.match(self.input, 115, self.FOLLOW_115_in_primaryExpression2526)
                    if self._state.backtracking == 0:

                        string_literal351_tree = self._adaptor.createWithPayload(string_literal351)
                        self._adaptor.addChild(root_0, string_literal351_tree)



                elif alt178 == 2:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:355:4: Identifier
                    pass 
                    root_0 = self._adaptor.nil()

                    Identifier352=self.match(self.input, Identifier, self.FOLLOW_Identifier_in_primaryExpression2531)
                    if self._state.backtracking == 0:

                        Identifier352_tree = self._adaptor.createWithPayload(Identifier352)
                        self._adaptor.addChild(root_0, Identifier352_tree)



                elif alt178 == 3:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:356:4: literal
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_literal_in_primaryExpression2536)
                    literal353 = self.literal()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, literal353.tree)


                elif alt178 == 4:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:357:4: arrayLiteral
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_arrayLiteral_in_primaryExpression2541)
                    arrayLiteral354 = self.arrayLiteral()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, arrayLiteral354.tree)


                elif alt178 == 5:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:358:4: objectLiteral
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_objectLiteral_in_primaryExpression2546)
                    objectLiteral355 = self.objectLiteral()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, objectLiteral355.tree)


                elif alt178 == 6:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:359:4: '(' ( LT )* expression ( LT )* ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal356=self.match(self.input, 54, self.FOLLOW_54_in_primaryExpression2551)
                    if self._state.backtracking == 0:

                        char_literal356_tree = self._adaptor.createWithPayload(char_literal356)
                        self._adaptor.addChild(root_0, char_literal356_tree)

                    # ../src/checkjs/parsers/antlr/JavaScript.g:359:10: ( LT )*
                    while True: #loop176
                        alt176 = 2
                        LA176_0 = self.input.LA(1)

                        if (LA176_0 == LT) :
                            alt176 = 1


                        if alt176 == 1:
                            # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                            pass 
                            LT357=self.match(self.input, LT, self.FOLLOW_LT_in_primaryExpression2553)


                        else:
                            break #loop176
                    self._state.following.append(self.FOLLOW_expression_in_primaryExpression2557)
                    expression358 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression358.tree)
                    # ../src/checkjs/parsers/antlr/JavaScript.g:359:26: ( LT )*
                    while True: #loop177
                        alt177 = 2
                        LA177_0 = self.input.LA(1)

                        if (LA177_0 == LT) :
                            alt177 = 1


                        if alt177 == 1:
                            # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                            pass 
                            LT359=self.match(self.input, LT, self.FOLLOW_LT_in_primaryExpression2559)


                        else:
                            break #loop177
                    char_literal360=self.match(self.input, 56, self.FOLLOW_56_in_primaryExpression2563)
                    if self._state.backtracking == 0:

                        char_literal360_tree = self._adaptor.createWithPayload(char_literal360)
                        self._adaptor.addChild(root_0, char_literal360_tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 61, primaryExpression_StartIndex, success)

            pass
        return retval

    # $ANTLR end "primaryExpression"

    class arrayLiteral_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.arrayLiteral_return, self).__init__()

            self.tree = None




    # $ANTLR start "arrayLiteral"
    # ../src/checkjs/parsers/antlr/JavaScript.g:363:1: arrayLiteral : '[' ( LT )* ( assignmentExpression )? ( ( LT )* ',' ( ( LT )* assignmentExpression )? )* ( LT )* ']' -> ^( ARRAY ( assignmentExpression )* ) ;
    def arrayLiteral(self, ):

        retval = self.arrayLiteral_return()
        retval.start = self.input.LT(1)
        arrayLiteral_StartIndex = self.input.index()
        root_0 = None

        char_literal361 = None
        LT362 = None
        LT364 = None
        char_literal365 = None
        LT366 = None
        LT368 = None
        char_literal369 = None
        assignmentExpression363 = None

        assignmentExpression367 = None


        char_literal361_tree = None
        LT362_tree = None
        LT364_tree = None
        char_literal365_tree = None
        LT366_tree = None
        LT368_tree = None
        char_literal369_tree = None
        stream_LT = RewriteRuleTokenStream(self._adaptor, "token LT")
        stream_55 = RewriteRuleTokenStream(self._adaptor, "token 55")
        stream_80 = RewriteRuleTokenStream(self._adaptor, "token 80")
        stream_81 = RewriteRuleTokenStream(self._adaptor, "token 81")
        stream_assignmentExpression = RewriteRuleSubtreeStream(self._adaptor, "rule assignmentExpression")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 62):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:364:2: ( '[' ( LT )* ( assignmentExpression )? ( ( LT )* ',' ( ( LT )* assignmentExpression )? )* ( LT )* ']' -> ^( ARRAY ( assignmentExpression )* ) )
                # ../src/checkjs/parsers/antlr/JavaScript.g:364:4: '[' ( LT )* ( assignmentExpression )? ( ( LT )* ',' ( ( LT )* assignmentExpression )? )* ( LT )* ']'
                pass 
                char_literal361=self.match(self.input, 80, self.FOLLOW_80_in_arrayLiteral2575) 
                if self._state.backtracking == 0:
                    stream_80.add(char_literal361)
                # ../src/checkjs/parsers/antlr/JavaScript.g:364:8: ( LT )*
                while True: #loop179
                    alt179 = 2
                    LA179_0 = self.input.LA(1)

                    if (LA179_0 == LT) :
                        LA179_2 = self.input.LA(2)

                        if (self.synpred235_JavaScript()) :
                            alt179 = 1




                    if alt179 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT362=self.match(self.input, LT, self.FOLLOW_LT_in_arrayLiteral2577) 
                        if self._state.backtracking == 0:
                            stream_LT.add(LT362)


                    else:
                        break #loop179
                # ../src/checkjs/parsers/antlr/JavaScript.g:364:12: ( assignmentExpression )?
                alt180 = 2
                LA180_0 = self.input.LA(1)

                if ((Identifier <= LA180_0 <= NumericLiteral) or LA180_0 == 52 or LA180_0 == 54 or LA180_0 == 57 or (79 <= LA180_0 <= 80) or (96 <= LA180_0 <= 97) or (108 <= LA180_0 <= 119)) :
                    alt180 = 1
                if alt180 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: assignmentExpression
                    pass 
                    self._state.following.append(self.FOLLOW_assignmentExpression_in_arrayLiteral2580)
                    assignmentExpression363 = self.assignmentExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_assignmentExpression.add(assignmentExpression363.tree)



                # ../src/checkjs/parsers/antlr/JavaScript.g:364:34: ( ( LT )* ',' ( ( LT )* assignmentExpression )? )*
                while True: #loop184
                    alt184 = 2
                    alt184 = self.dfa184.predict(self.input)
                    if alt184 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:364:35: ( LT )* ',' ( ( LT )* assignmentExpression )?
                        pass 
                        # ../src/checkjs/parsers/antlr/JavaScript.g:364:35: ( LT )*
                        while True: #loop181
                            alt181 = 2
                            LA181_0 = self.input.LA(1)

                            if (LA181_0 == LT) :
                                alt181 = 1


                            if alt181 == 1:
                                # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                                pass 
                                LT364=self.match(self.input, LT, self.FOLLOW_LT_in_arrayLiteral2584) 
                                if self._state.backtracking == 0:
                                    stream_LT.add(LT364)


                            else:
                                break #loop181
                        char_literal365=self.match(self.input, 55, self.FOLLOW_55_in_arrayLiteral2587) 
                        if self._state.backtracking == 0:
                            stream_55.add(char_literal365)
                        # ../src/checkjs/parsers/antlr/JavaScript.g:364:43: ( ( LT )* assignmentExpression )?
                        alt183 = 2
                        alt183 = self.dfa183.predict(self.input)
                        if alt183 == 1:
                            # ../src/checkjs/parsers/antlr/JavaScript.g:364:44: ( LT )* assignmentExpression
                            pass 
                            # ../src/checkjs/parsers/antlr/JavaScript.g:364:44: ( LT )*
                            while True: #loop182
                                alt182 = 2
                                LA182_0 = self.input.LA(1)

                                if (LA182_0 == LT) :
                                    alt182 = 1


                                if alt182 == 1:
                                    # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                                    pass 
                                    LT366=self.match(self.input, LT, self.FOLLOW_LT_in_arrayLiteral2590) 
                                    if self._state.backtracking == 0:
                                        stream_LT.add(LT366)


                                else:
                                    break #loop182
                            self._state.following.append(self.FOLLOW_assignmentExpression_in_arrayLiteral2593)
                            assignmentExpression367 = self.assignmentExpression()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_assignmentExpression.add(assignmentExpression367.tree)





                    else:
                        break #loop184
                # ../src/checkjs/parsers/antlr/JavaScript.g:364:73: ( LT )*
                while True: #loop185
                    alt185 = 2
                    LA185_0 = self.input.LA(1)

                    if (LA185_0 == LT) :
                        alt185 = 1


                    if alt185 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT368=self.match(self.input, LT, self.FOLLOW_LT_in_arrayLiteral2599) 
                        if self._state.backtracking == 0:
                            stream_LT.add(LT368)


                    else:
                        break #loop185
                char_literal369=self.match(self.input, 81, self.FOLLOW_81_in_arrayLiteral2602) 
                if self._state.backtracking == 0:
                    stream_81.add(char_literal369)

                # AST Rewrite
                # elements: assignmentExpression
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 365:9: -> ^( ARRAY ( assignmentExpression )* )
                    # ../src/checkjs/parsers/antlr/JavaScript.g:365:12: ^( ARRAY ( assignmentExpression )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ARRAY, "ARRAY"), root_1)

                    # ../src/checkjs/parsers/antlr/JavaScript.g:365:21: ( assignmentExpression )*
                    while stream_assignmentExpression.hasNext():
                        self._adaptor.addChild(root_1, stream_assignmentExpression.nextTree())


                    stream_assignmentExpression.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 62, arrayLiteral_StartIndex, success)

            pass
        return retval

    # $ANTLR end "arrayLiteral"

    class objectLiteral_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.objectLiteral_return, self).__init__()

            self.tree = None




    # $ANTLR start "objectLiteral"
    # ../src/checkjs/parsers/antlr/JavaScript.g:369:1: objectLiteral : '{' ( LT )* ( propertyNameAndValue ( ( LT )* ',' ( LT )* propertyNameAndValue )* )? ( LT )* '}' -> ^( OBJECT ( propertyNameAndValue )* ) ;
    def objectLiteral(self, ):

        retval = self.objectLiteral_return()
        retval.start = self.input.LT(1)
        objectLiteral_StartIndex = self.input.index()
        root_0 = None

        char_literal370 = None
        LT371 = None
        LT373 = None
        char_literal374 = None
        LT375 = None
        LT377 = None
        char_literal378 = None
        propertyNameAndValue372 = None

        propertyNameAndValue376 = None


        char_literal370_tree = None
        LT371_tree = None
        LT373_tree = None
        char_literal374_tree = None
        LT375_tree = None
        LT377_tree = None
        char_literal378_tree = None
        stream_LT = RewriteRuleTokenStream(self._adaptor, "token LT")
        stream_58 = RewriteRuleTokenStream(self._adaptor, "token 58")
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_55 = RewriteRuleTokenStream(self._adaptor, "token 55")
        stream_propertyNameAndValue = RewriteRuleSubtreeStream(self._adaptor, "rule propertyNameAndValue")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 63):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:370:2: ( '{' ( LT )* ( propertyNameAndValue ( ( LT )* ',' ( LT )* propertyNameAndValue )* )? ( LT )* '}' -> ^( OBJECT ( propertyNameAndValue )* ) )
                # ../src/checkjs/parsers/antlr/JavaScript.g:370:4: '{' ( LT )* ( propertyNameAndValue ( ( LT )* ',' ( LT )* propertyNameAndValue )* )? ( LT )* '}'
                pass 
                char_literal370=self.match(self.input, 57, self.FOLLOW_57_in_objectLiteral2632) 
                if self._state.backtracking == 0:
                    stream_57.add(char_literal370)
                # ../src/checkjs/parsers/antlr/JavaScript.g:370:8: ( LT )*
                while True: #loop186
                    alt186 = 2
                    LA186_0 = self.input.LA(1)

                    if (LA186_0 == LT) :
                        LA186_2 = self.input.LA(2)

                        if (self.synpred242_JavaScript()) :
                            alt186 = 1




                    if alt186 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT371=self.match(self.input, LT, self.FOLLOW_LT_in_objectLiteral2634) 
                        if self._state.backtracking == 0:
                            stream_LT.add(LT371)


                    else:
                        break #loop186
                # ../src/checkjs/parsers/antlr/JavaScript.g:370:12: ( propertyNameAndValue ( ( LT )* ',' ( LT )* propertyNameAndValue )* )?
                alt190 = 2
                LA190_0 = self.input.LA(1)

                if ((Identifier <= LA190_0 <= NumericLiteral)) :
                    alt190 = 1
                if alt190 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:370:13: propertyNameAndValue ( ( LT )* ',' ( LT )* propertyNameAndValue )*
                    pass 
                    self._state.following.append(self.FOLLOW_propertyNameAndValue_in_objectLiteral2638)
                    propertyNameAndValue372 = self.propertyNameAndValue()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_propertyNameAndValue.add(propertyNameAndValue372.tree)
                    # ../src/checkjs/parsers/antlr/JavaScript.g:370:34: ( ( LT )* ',' ( LT )* propertyNameAndValue )*
                    while True: #loop189
                        alt189 = 2
                        alt189 = self.dfa189.predict(self.input)
                        if alt189 == 1:
                            # ../src/checkjs/parsers/antlr/JavaScript.g:370:35: ( LT )* ',' ( LT )* propertyNameAndValue
                            pass 
                            # ../src/checkjs/parsers/antlr/JavaScript.g:370:35: ( LT )*
                            while True: #loop187
                                alt187 = 2
                                LA187_0 = self.input.LA(1)

                                if (LA187_0 == LT) :
                                    alt187 = 1


                                if alt187 == 1:
                                    # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                                    pass 
                                    LT373=self.match(self.input, LT, self.FOLLOW_LT_in_objectLiteral2641) 
                                    if self._state.backtracking == 0:
                                        stream_LT.add(LT373)


                                else:
                                    break #loop187
                            char_literal374=self.match(self.input, 55, self.FOLLOW_55_in_objectLiteral2644) 
                            if self._state.backtracking == 0:
                                stream_55.add(char_literal374)
                            # ../src/checkjs/parsers/antlr/JavaScript.g:370:43: ( LT )*
                            while True: #loop188
                                alt188 = 2
                                LA188_0 = self.input.LA(1)

                                if (LA188_0 == LT) :
                                    alt188 = 1


                                if alt188 == 1:
                                    # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                                    pass 
                                    LT375=self.match(self.input, LT, self.FOLLOW_LT_in_objectLiteral2646) 
                                    if self._state.backtracking == 0:
                                        stream_LT.add(LT375)


                                else:
                                    break #loop188
                            self._state.following.append(self.FOLLOW_propertyNameAndValue_in_objectLiteral2649)
                            propertyNameAndValue376 = self.propertyNameAndValue()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_propertyNameAndValue.add(propertyNameAndValue376.tree)


                        else:
                            break #loop189



                # ../src/checkjs/parsers/antlr/JavaScript.g:370:72: ( LT )*
                while True: #loop191
                    alt191 = 2
                    LA191_0 = self.input.LA(1)

                    if (LA191_0 == LT) :
                        alt191 = 1


                    if alt191 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT377=self.match(self.input, LT, self.FOLLOW_LT_in_objectLiteral2655) 
                        if self._state.backtracking == 0:
                            stream_LT.add(LT377)


                    else:
                        break #loop191
                char_literal378=self.match(self.input, 58, self.FOLLOW_58_in_objectLiteral2658) 
                if self._state.backtracking == 0:
                    stream_58.add(char_literal378)

                # AST Rewrite
                # elements: propertyNameAndValue
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 371:9: -> ^( OBJECT ( propertyNameAndValue )* )
                    # ../src/checkjs/parsers/antlr/JavaScript.g:371:12: ^( OBJECT ( propertyNameAndValue )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(OBJECT, "OBJECT"), root_1)

                    # ../src/checkjs/parsers/antlr/JavaScript.g:371:22: ( propertyNameAndValue )*
                    while stream_propertyNameAndValue.hasNext():
                        self._adaptor.addChild(root_1, stream_propertyNameAndValue.nextTree())


                    stream_propertyNameAndValue.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 63, objectLiteral_StartIndex, success)

            pass
        return retval

    # $ANTLR end "objectLiteral"

    class propertyNameAndValue_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.propertyNameAndValue_return, self).__init__()

            self.tree = None




    # $ANTLR start "propertyNameAndValue"
    # ../src/checkjs/parsers/antlr/JavaScript.g:374:1: propertyNameAndValue : propertyName ( LT )* ':' ( LT )* assignmentExpression -> ^( PROPERTY propertyName assignmentExpression ) ;
    def propertyNameAndValue(self, ):

        retval = self.propertyNameAndValue_return()
        retval.start = self.input.LT(1)
        propertyNameAndValue_StartIndex = self.input.index()
        root_0 = None

        LT380 = None
        char_literal381 = None
        LT382 = None
        propertyName379 = None

        assignmentExpression383 = None


        LT380_tree = None
        char_literal381_tree = None
        LT382_tree = None
        stream_LT = RewriteRuleTokenStream(self._adaptor, "token LT")
        stream_71 = RewriteRuleTokenStream(self._adaptor, "token 71")
        stream_propertyName = RewriteRuleSubtreeStream(self._adaptor, "rule propertyName")
        stream_assignmentExpression = RewriteRuleSubtreeStream(self._adaptor, "rule assignmentExpression")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 64):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:375:2: ( propertyName ( LT )* ':' ( LT )* assignmentExpression -> ^( PROPERTY propertyName assignmentExpression ) )
                # ../src/checkjs/parsers/antlr/JavaScript.g:375:4: propertyName ( LT )* ':' ( LT )* assignmentExpression
                pass 
                self._state.following.append(self.FOLLOW_propertyName_in_propertyNameAndValue2687)
                propertyName379 = self.propertyName()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_propertyName.add(propertyName379.tree)
                # ../src/checkjs/parsers/antlr/JavaScript.g:375:17: ( LT )*
                while True: #loop192
                    alt192 = 2
                    LA192_0 = self.input.LA(1)

                    if (LA192_0 == LT) :
                        alt192 = 1


                    if alt192 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT380=self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue2689) 
                        if self._state.backtracking == 0:
                            stream_LT.add(LT380)


                    else:
                        break #loop192
                char_literal381=self.match(self.input, 71, self.FOLLOW_71_in_propertyNameAndValue2692) 
                if self._state.backtracking == 0:
                    stream_71.add(char_literal381)
                # ../src/checkjs/parsers/antlr/JavaScript.g:375:25: ( LT )*
                while True: #loop193
                    alt193 = 2
                    LA193_0 = self.input.LA(1)

                    if (LA193_0 == LT) :
                        alt193 = 1


                    if alt193 == 1:
                        # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                        pass 
                        LT382=self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue2694) 
                        if self._state.backtracking == 0:
                            stream_LT.add(LT382)


                    else:
                        break #loop193
                self._state.following.append(self.FOLLOW_assignmentExpression_in_propertyNameAndValue2697)
                assignmentExpression383 = self.assignmentExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_assignmentExpression.add(assignmentExpression383.tree)

                # AST Rewrite
                # elements: assignmentExpression, propertyName
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 375:50: -> ^( PROPERTY propertyName assignmentExpression )
                    # ../src/checkjs/parsers/antlr/JavaScript.g:376:9: ^( PROPERTY propertyName assignmentExpression )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROPERTY, "PROPERTY"), root_1)

                    self._adaptor.addChild(root_1, stream_propertyName.nextTree())
                    self._adaptor.addChild(root_1, stream_assignmentExpression.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 64, propertyNameAndValue_StartIndex, success)

            pass
        return retval

    # $ANTLR end "propertyNameAndValue"

    class propertyName_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.propertyName_return, self).__init__()

            self.tree = None




    # $ANTLR start "propertyName"
    # ../src/checkjs/parsers/antlr/JavaScript.g:379:1: propertyName : ( Identifier | StringLiteral | NumericLiteral );
    def propertyName(self, ):

        retval = self.propertyName_return()
        retval.start = self.input.LT(1)
        propertyName_StartIndex = self.input.index()
        root_0 = None

        set384 = None

        set384_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 65):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:380:2: ( Identifier | StringLiteral | NumericLiteral )
                # ../src/checkjs/parsers/antlr/JavaScript.g:
                pass 
                root_0 = self._adaptor.nil()

                set384 = self.input.LT(1)
                if (Identifier <= self.input.LA(1) <= NumericLiteral):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set384))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 65, propertyName_StartIndex, success)

            pass
        return retval

    # $ANTLR end "propertyName"

    class literal_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.literal_return, self).__init__()

            self.tree = None




    # $ANTLR start "literal"
    # ../src/checkjs/parsers/antlr/JavaScript.g:386:1: literal : ( 'null' | 'true' | 'false' | StringLiteral | NumericLiteral | regexpLiteral );
    def literal(self, ):

        retval = self.literal_return()
        retval.start = self.input.LT(1)
        literal_StartIndex = self.input.index()
        root_0 = None

        string_literal385 = None
        string_literal386 = None
        string_literal387 = None
        StringLiteral388 = None
        NumericLiteral389 = None
        regexpLiteral390 = None


        string_literal385_tree = None
        string_literal386_tree = None
        string_literal387_tree = None
        StringLiteral388_tree = None
        NumericLiteral389_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 66):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:387:2: ( 'null' | 'true' | 'false' | StringLiteral | NumericLiteral | regexpLiteral )
                alt194 = 6
                LA194 = self.input.LA(1)
                if LA194 == 116:
                    alt194 = 1
                elif LA194 == 117:
                    alt194 = 2
                elif LA194 == 118:
                    alt194 = 3
                elif LA194 == StringLiteral:
                    alt194 = 4
                elif LA194 == NumericLiteral:
                    alt194 = 5
                elif LA194 == 119:
                    alt194 = 6
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 194, 0, self.input)

                    raise nvae

                if alt194 == 1:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:387:4: 'null'
                    pass 
                    root_0 = self._adaptor.nil()

                    string_literal385=self.match(self.input, 116, self.FOLLOW_116_in_literal2749)
                    if self._state.backtracking == 0:

                        string_literal385_tree = self._adaptor.createWithPayload(string_literal385)
                        self._adaptor.addChild(root_0, string_literal385_tree)



                elif alt194 == 2:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:388:4: 'true'
                    pass 
                    root_0 = self._adaptor.nil()

                    string_literal386=self.match(self.input, 117, self.FOLLOW_117_in_literal2754)
                    if self._state.backtracking == 0:

                        string_literal386_tree = self._adaptor.createWithPayload(string_literal386)
                        self._adaptor.addChild(root_0, string_literal386_tree)



                elif alt194 == 3:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:389:4: 'false'
                    pass 
                    root_0 = self._adaptor.nil()

                    string_literal387=self.match(self.input, 118, self.FOLLOW_118_in_literal2759)
                    if self._state.backtracking == 0:

                        string_literal387_tree = self._adaptor.createWithPayload(string_literal387)
                        self._adaptor.addChild(root_0, string_literal387_tree)



                elif alt194 == 4:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:390:4: StringLiteral
                    pass 
                    root_0 = self._adaptor.nil()

                    StringLiteral388=self.match(self.input, StringLiteral, self.FOLLOW_StringLiteral_in_literal2764)
                    if self._state.backtracking == 0:

                        StringLiteral388_tree = self._adaptor.createWithPayload(StringLiteral388)
                        self._adaptor.addChild(root_0, StringLiteral388_tree)



                elif alt194 == 5:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:391:4: NumericLiteral
                    pass 
                    root_0 = self._adaptor.nil()

                    NumericLiteral389=self.match(self.input, NumericLiteral, self.FOLLOW_NumericLiteral_in_literal2769)
                    if self._state.backtracking == 0:

                        NumericLiteral389_tree = self._adaptor.createWithPayload(NumericLiteral389)
                        self._adaptor.addChild(root_0, NumericLiteral389_tree)



                elif alt194 == 6:
                    # ../src/checkjs/parsers/antlr/JavaScript.g:392:7: regexpLiteral
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_regexpLiteral_in_literal2777)
                    regexpLiteral390 = self.regexpLiteral()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, regexpLiteral390.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 66, literal_StartIndex, success)

            pass
        return retval

    # $ANTLR end "literal"

    class regexpLiteral_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaScriptParser.regexpLiteral_return, self).__init__()

            self.tree = None




    # $ANTLR start "regexpLiteral"
    # ../src/checkjs/parsers/antlr/JavaScript.g:397:1: regexpLiteral : '\\/' ~ '\\/' '\\/' ;
    def regexpLiteral(self, ):

        retval = self.regexpLiteral_return()
        retval.start = self.input.LT(1)
        regexpLiteral_StartIndex = self.input.index()
        root_0 = None

        char_literal391 = None
        set392 = None
        char_literal393 = None

        char_literal391_tree = None
        set392_tree = None
        char_literal393_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 67):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # ../src/checkjs/parsers/antlr/JavaScript.g:398:2: ( '\\/' ~ '\\/' '\\/' )
                # ../src/checkjs/parsers/antlr/JavaScript.g:398:4: '\\/' ~ '\\/' '\\/'
                pass 
                root_0 = self._adaptor.nil()

                char_literal391=self.match(self.input, 119, self.FOLLOW_119_in_regexpLiteral2790)
                if self._state.backtracking == 0:

                    char_literal391_tree = self._adaptor.createWithPayload(char_literal391)
                    self._adaptor.addChild(root_0, char_literal391_tree)

                set392 = self.input.LT(1)
                if (FUNCTION <= self.input.LA(1) <= 118):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set392))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse


                char_literal393=self.match(self.input, 119, self.FOLLOW_119_in_regexpLiteral2795)
                if self._state.backtracking == 0:

                    char_literal393_tree = self._adaptor.createWithPayload(char_literal393)
                    self._adaptor.addChild(root_0, char_literal393_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 67, regexpLiteral_StartIndex, success)

            pass
        return retval

    # $ANTLR end "regexpLiteral"

    # $ANTLR start "synpred5_JavaScript"
    def synpred5_JavaScript_fragment(self, ):
        # ../src/checkjs/parsers/antlr/JavaScript.g:54:4: ( functionDeclaration )
        # ../src/checkjs/parsers/antlr/JavaScript.g:54:4: functionDeclaration
        pass 
        self._state.following.append(self.FOLLOW_functionDeclaration_in_synpred5_JavaScript229)
        self.functionDeclaration()

        self._state.following.pop()


    # $ANTLR end "synpred5_JavaScript"



    # $ANTLR start "synpred10_JavaScript"
    def synpred10_JavaScript_fragment(self, ):
        # ../src/checkjs/parsers/antlr/JavaScript.g:65:15: ( LT )
        # ../src/checkjs/parsers/antlr/JavaScript.g:65:15: LT
        pass 
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred10_JavaScript301)


    # $ANTLR end "synpred10_JavaScript"



    # $ANTLR start "synpred20_JavaScript"
    def synpred20_JavaScript_fragment(self, ):
        # ../src/checkjs/parsers/antlr/JavaScript.g:75:8: ( LT )
        # ../src/checkjs/parsers/antlr/JavaScript.g:75:8: LT
        pass 
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred20_JavaScript402)


    # $ANTLR end "synpred20_JavaScript"



    # $ANTLR start "synpred25_JavaScript"
    def synpred25_JavaScript_fragment(self, ):
        # ../src/checkjs/parsers/antlr/JavaScript.g:97:4: ( expressionStatement )
        # ../src/checkjs/parsers/antlr/JavaScript.g:97:4: expressionStatement
        pass 
        self._state.following.append(self.FOLLOW_expressionStatement_in_synpred25_JavaScript481)
        self.expressionStatement()

        self._state.following.pop()


    # $ANTLR end "synpred25_JavaScript"



    # $ANTLR start "synpred32_JavaScript"
    def synpred32_JavaScript_fragment(self, ):
        # ../src/checkjs/parsers/antlr/JavaScript.g:105:4: ( labelledStatement )
        # ../src/checkjs/parsers/antlr/JavaScript.g:105:4: labelledStatement
        pass 
        self._state.following.append(self.FOLLOW_labelledStatement_in_synpred32_JavaScript521)
        self.labelledStatement()

        self._state.following.pop()


    # $ANTLR end "synpred32_JavaScript"



    # $ANTLR start "synpred35_JavaScript"
    def synpred35_JavaScript_fragment(self, ):
        # ../src/checkjs/parsers/antlr/JavaScript.g:112:8: ( LT )
        # ../src/checkjs/parsers/antlr/JavaScript.g:112:8: LT
        pass 
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred35_JavaScript549)


    # $ANTLR end "synpred35_JavaScript"



    # $ANTLR start "synpred50_JavaScript"
    def synpred50_JavaScript_fragment(self, ):
        # ../src/checkjs/parsers/antlr/JavaScript.g:133:15: ( LT )
        # ../src/checkjs/parsers/antlr/JavaScript.g:133:15: LT
        pass 
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred50_JavaScript693)


    # $ANTLR end "synpred50_JavaScript"



    # $ANTLR start "synpred51_JavaScript"
    def synpred51_JavaScript_fragment(self, ):
        # ../src/checkjs/parsers/antlr/JavaScript.g:137:15: ( LT )
        # ../src/checkjs/parsers/antlr/JavaScript.g:137:15: LT
        pass 
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred51_JavaScript716)


    # $ANTLR end "synpred51_JavaScript"



    # $ANTLR start "synpred60_JavaScript"
    def synpred60_JavaScript_fragment(self, ):
        # ../src/checkjs/parsers/antlr/JavaScript.g:158:49: ( statement )
        # ../src/checkjs/parsers/antlr/JavaScript.g:158:49: statement
        pass 
        self._state.following.append(self.FOLLOW_statement_in_synpred60_JavaScript840)
        self.statement()

        self._state.following.pop()


    # $ANTLR end "synpred60_JavaScript"



    # $ANTLR start "synpred63_JavaScript"
    def synpred63_JavaScript_fragment(self, ):
        # ../src/checkjs/parsers/antlr/JavaScript.g:158:96: ( statement )
        # ../src/checkjs/parsers/antlr/JavaScript.g:158:96: statement
        pass 
        self._state.following.append(self.FOLLOW_statement_in_synpred63_JavaScript859)
        self.statement()

        self._state.following.pop()


    # $ANTLR end "synpred63_JavaScript"



    # $ANTLR start "synpred64_JavaScript"
    def synpred64_JavaScript_fragment(self, ):
        # ../src/checkjs/parsers/antlr/JavaScript.g:158:78: ( ( LT )* 'else' ( LT )* ( statement | statementBlock ) )
        # ../src/checkjs/parsers/antlr/JavaScript.g:158:78: ( LT )* 'else' ( LT )* ( statement | statementBlock )
        pass 
        # ../src/checkjs/parsers/antlr/JavaScript.g:158:80: ( LT )*
        while True: #loop208
            alt208 = 2
            LA208_0 = self.input.LA(1)

            if (LA208_0 == LT) :
                alt208 = 1


            if alt208 == 1:
                # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                pass 
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred64_JavaScript848)


            else:
                break #loop208
        self.match(self.input, 62, self.FOLLOW_62_in_synpred64_JavaScript852)
        # ../src/checkjs/parsers/antlr/JavaScript.g:158:92: ( LT )*
        while True: #loop209
            alt209 = 2
            LA209_0 = self.input.LA(1)

            if (LA209_0 == LT) :
                alt209 = 1


            if alt209 == 1:
                # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                pass 
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred64_JavaScript854)


            else:
                break #loop209
        # ../src/checkjs/parsers/antlr/JavaScript.g:158:95: ( statement | statementBlock )
        alt210 = 2
        alt210 = self.dfa210.predict(self.input)
        if alt210 == 1:
            # ../src/checkjs/parsers/antlr/JavaScript.g:158:96: statement
            pass 
            self._state.following.append(self.FOLLOW_statement_in_synpred64_JavaScript859)
            self.statement()

            self._state.following.pop()


        elif alt210 == 2:
            # ../src/checkjs/parsers/antlr/JavaScript.g:158:108: statementBlock
            pass 
            self._state.following.append(self.FOLLOW_statementBlock_in_synpred64_JavaScript863)
            self.statementBlock()

            self._state.following.pop()





    # $ANTLR end "synpred64_JavaScript"



    # $ANTLR start "synpred67_JavaScript"
    def synpred67_JavaScript_fragment(self, ):
        # ../src/checkjs/parsers/antlr/JavaScript.g:164:4: ( forStatement )
        # ../src/checkjs/parsers/antlr/JavaScript.g:164:4: forStatement
        pass 
        self._state.following.append(self.FOLLOW_forStatement_in_synpred67_JavaScript887)
        self.forStatement()

        self._state.following.pop()


    # $ANTLR end "synpred67_JavaScript"



    # $ANTLR start "synpred69_JavaScript"
    def synpred69_JavaScript_fragment(self, ):
        # ../src/checkjs/parsers/antlr/JavaScript.g:169:15: ( statement )
        # ../src/checkjs/parsers/antlr/JavaScript.g:169:15: statement
        pass 
        self._state.following.append(self.FOLLOW_statement_in_synpred69_JavaScript910)
        self.statement()

        self._state.following.pop()


    # $ANTLR end "synpred69_JavaScript"



    # $ANTLR start "synpred77_JavaScript"
    def synpred77_JavaScript_fragment(self, ):
        # ../src/checkjs/parsers/antlr/JavaScript.g:173:52: ( statement )
        # ../src/checkjs/parsers/antlr/JavaScript.g:173:52: statement
        pass 
        self._state.following.append(self.FOLLOW_statement_in_synpred77_JavaScript974)
        self.statement()

        self._state.following.pop()


    # $ANTLR end "synpred77_JavaScript"



    # $ANTLR start "synpred89_JavaScript"
    def synpred89_JavaScript_fragment(self, ):
        # ../src/checkjs/parsers/antlr/JavaScript.g:177:128: ( statement )
        # ../src/checkjs/parsers/antlr/JavaScript.g:177:128: statement
        pass 
        self._state.following.append(self.FOLLOW_statement_in_synpred89_JavaScript1050)
        self.statement()

        self._state.following.pop()


    # $ANTLR end "synpred89_JavaScript"



    # $ANTLR start "synpred98_JavaScript"
    def synpred98_JavaScript_fragment(self, ):
        # ../src/checkjs/parsers/antlr/JavaScript.g:186:95: ( statement )
        # ../src/checkjs/parsers/antlr/JavaScript.g:186:95: statement
        pass 
        self._state.following.append(self.FOLLOW_statement_in_synpred98_JavaScript1125)
        self.statement()

        self._state.following.pop()


    # $ANTLR end "synpred98_JavaScript"



    # $ANTLR start "synpred111_JavaScript"
    def synpred111_JavaScript_fragment(self, ):
        # ../src/checkjs/parsers/antlr/JavaScript.g:207:51: ( statement )
        # ../src/checkjs/parsers/antlr/JavaScript.g:207:51: statement
        pass 
        self._state.following.append(self.FOLLOW_statement_in_synpred111_JavaScript1251)
        self.statement()

        self._state.following.pop()


    # $ANTLR end "synpred111_JavaScript"



    # $ANTLR start "synpred127_JavaScript"
    def synpred127_JavaScript_fragment(self, ):
        # ../src/checkjs/parsers/antlr/JavaScript.g:223:36: ( LT )
        # ../src/checkjs/parsers/antlr/JavaScript.g:223:36: LT
        pass 
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred127_JavaScript1383)


    # $ANTLR end "synpred127_JavaScript"



    # $ANTLR start "synpred130_JavaScript"
    def synpred130_JavaScript_fragment(self, ):
        # ../src/checkjs/parsers/antlr/JavaScript.g:227:23: ( LT )
        # ../src/checkjs/parsers/antlr/JavaScript.g:227:23: LT
        pass 
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred130_JavaScript1407)


    # $ANTLR end "synpred130_JavaScript"



    # $ANTLR start "synpred149_JavaScript"
    def synpred149_JavaScript_fragment(self, ):
        # ../src/checkjs/parsers/antlr/JavaScript.g:257:7: ( callExpression )
        # ../src/checkjs/parsers/antlr/JavaScript.g:257:7: callExpression
        pass 
        self._state.following.append(self.FOLLOW_callExpression_in_synpred149_JavaScript1594)
        self.callExpression()

        self._state.following.pop()


    # $ANTLR end "synpred149_JavaScript"



    # $ANTLR start "synpred152_JavaScript"
    def synpred152_JavaScript_fragment(self, ):
        # ../src/checkjs/parsers/antlr/JavaScript.g:258:7: ( ( leftHandSideExpression ( LT )* nonAssignmentOperator ( LT )* assignmentExpression ) )
        # ../src/checkjs/parsers/antlr/JavaScript.g:258:7: ( leftHandSideExpression ( LT )* nonAssignmentOperator ( LT )* assignmentExpression )
        pass 
        # ../src/checkjs/parsers/antlr/JavaScript.g:258:7: ( leftHandSideExpression ( LT )* nonAssignmentOperator ( LT )* assignmentExpression )
        # ../src/checkjs/parsers/antlr/JavaScript.g:258:8: leftHandSideExpression ( LT )* nonAssignmentOperator ( LT )* assignmentExpression
        pass 
        self._state.following.append(self.FOLLOW_leftHandSideExpression_in_synpred152_JavaScript1612)
        self.leftHandSideExpression()

        self._state.following.pop()
        # ../src/checkjs/parsers/antlr/JavaScript.g:258:31: ( LT )*
        while True: #loop224
            alt224 = 2
            LA224_0 = self.input.LA(1)

            if (LA224_0 == LT) :
                alt224 = 1


            if alt224 == 1:
                # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                pass 
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred152_JavaScript1614)


            else:
                break #loop224
        self._state.following.append(self.FOLLOW_nonAssignmentOperator_in_synpred152_JavaScript1617)
        self.nonAssignmentOperator()

        self._state.following.pop()
        # ../src/checkjs/parsers/antlr/JavaScript.g:258:57: ( LT )*
        while True: #loop225
            alt225 = 2
            LA225_0 = self.input.LA(1)

            if (LA225_0 == LT) :
                alt225 = 1


            if alt225 == 1:
                # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                pass 
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred152_JavaScript1619)


            else:
                break #loop225
        self._state.following.append(self.FOLLOW_assignmentExpression_in_synpred152_JavaScript1622)
        self.assignmentExpression()

        self._state.following.pop()





    # $ANTLR end "synpred152_JavaScript"



    # $ANTLR start "synpred155_JavaScript"
    def synpred155_JavaScript_fragment(self, ):
        # ../src/checkjs/parsers/antlr/JavaScript.g:264:7: ( ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression ) )
        # ../src/checkjs/parsers/antlr/JavaScript.g:264:7: ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression )
        pass 
        # ../src/checkjs/parsers/antlr/JavaScript.g:264:7: ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression )
        # ../src/checkjs/parsers/antlr/JavaScript.g:264:8: leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression
        pass 
        self._state.following.append(self.FOLLOW_leftHandSideExpression_in_synpred155_JavaScript1717)
        self.leftHandSideExpression()

        self._state.following.pop()
        # ../src/checkjs/parsers/antlr/JavaScript.g:264:31: ( LT )*
        while True: #loop226
            alt226 = 2
            LA226_0 = self.input.LA(1)

            if (LA226_0 == LT) :
                alt226 = 1


            if alt226 == 1:
                # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                pass 
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred155_JavaScript1719)


            else:
                break #loop226
        self._state.following.append(self.FOLLOW_assignmentOperator_in_synpred155_JavaScript1722)
        self.assignmentOperator()

        self._state.following.pop()
        # ../src/checkjs/parsers/antlr/JavaScript.g:264:54: ( LT )*
        while True: #loop227
            alt227 = 2
            LA227_0 = self.input.LA(1)

            if (LA227_0 == LT) :
                alt227 = 1


            if alt227 == 1:
                # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                pass 
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred155_JavaScript1724)


            else:
                break #loop227
        self._state.following.append(self.FOLLOW_assignmentExpression_in_synpred155_JavaScript1727)
        self.assignmentExpression()

        self._state.following.pop()





    # $ANTLR end "synpred155_JavaScript"



    # $ANTLR start "synpred156_JavaScript"
    def synpred156_JavaScript_fragment(self, ):
        # ../src/checkjs/parsers/antlr/JavaScript.g:270:7: ( unaryExpression )
        # ../src/checkjs/parsers/antlr/JavaScript.g:270:7: unaryExpression
        pass 
        self._state.following.append(self.FOLLOW_unaryExpression_in_synpred156_JavaScript1821)
        self.unaryExpression()

        self._state.following.pop()


    # $ANTLR end "synpred156_JavaScript"



    # $ANTLR start "synpred157_JavaScript"
    def synpred157_JavaScript_fragment(self, ):
        # ../src/checkjs/parsers/antlr/JavaScript.g:275:4: ( conditionalExpression )
        # ../src/checkjs/parsers/antlr/JavaScript.g:275:4: conditionalExpression
        pass 
        self._state.following.append(self.FOLLOW_conditionalExpression_in_synpred157_JavaScript1852)
        self.conditionalExpression()

        self._state.following.pop()


    # $ANTLR end "synpred157_JavaScript"



    # $ANTLR start "synpred160_JavaScript"
    def synpred160_JavaScript_fragment(self, ):
        # ../src/checkjs/parsers/antlr/JavaScript.g:284:4: ( memberExpression )
        # ../src/checkjs/parsers/antlr/JavaScript.g:284:4: memberExpression
        pass 
        self._state.following.append(self.FOLLOW_memberExpression_in_synpred160_JavaScript1900)
        self.memberExpression()

        self._state.following.pop()


    # $ANTLR end "synpred160_JavaScript"



    # $ANTLR start "synpred201_JavaScript"
    def synpred201_JavaScript_fragment(self, ):
        # ../src/checkjs/parsers/antlr/JavaScript.g:330:7: ( ( leftHandSideExpression ( LT )* nonAssignmentOperator ( LT )* assignmentExpression ) )
        # ../src/checkjs/parsers/antlr/JavaScript.g:330:7: ( leftHandSideExpression ( LT )* nonAssignmentOperator ( LT )* assignmentExpression )
        pass 
        # ../src/checkjs/parsers/antlr/JavaScript.g:330:7: ( leftHandSideExpression ( LT )* nonAssignmentOperator ( LT )* assignmentExpression )
        # ../src/checkjs/parsers/antlr/JavaScript.g:330:8: leftHandSideExpression ( LT )* nonAssignmentOperator ( LT )* assignmentExpression
        pass 
        self._state.following.append(self.FOLLOW_leftHandSideExpression_in_synpred201_JavaScript2258)
        self.leftHandSideExpression()

        self._state.following.pop()
        # ../src/checkjs/parsers/antlr/JavaScript.g:330:31: ( LT )*
        while True: #loop240
            alt240 = 2
            LA240_0 = self.input.LA(1)

            if (LA240_0 == LT) :
                alt240 = 1


            if alt240 == 1:
                # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                pass 
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred201_JavaScript2260)


            else:
                break #loop240
        self._state.following.append(self.FOLLOW_nonAssignmentOperator_in_synpred201_JavaScript2263)
        self.nonAssignmentOperator()

        self._state.following.pop()
        # ../src/checkjs/parsers/antlr/JavaScript.g:330:57: ( LT )*
        while True: #loop241
            alt241 = 2
            LA241_0 = self.input.LA(1)

            if (LA241_0 == LT) :
                alt241 = 1


            if alt241 == 1:
                # ../src/checkjs/parsers/antlr/JavaScript.g:0:0: LT
                pass 
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred201_JavaScript2265)


            else:
                break #loop241
        self._state.following.append(self.FOLLOW_assignmentExpression_in_synpred201_JavaScript2268)
        self.assignmentExpression()

        self._state.following.pop()





    # $ANTLR end "synpred201_JavaScript"



    # $ANTLR start "synpred235_JavaScript"
    def synpred235_JavaScript_fragment(self, ):
        # ../src/checkjs/parsers/antlr/JavaScript.g:364:8: ( LT )
        # ../src/checkjs/parsers/antlr/JavaScript.g:364:8: LT
        pass 
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred235_JavaScript2577)


    # $ANTLR end "synpred235_JavaScript"



    # $ANTLR start "synpred242_JavaScript"
    def synpred242_JavaScript_fragment(self, ):
        # ../src/checkjs/parsers/antlr/JavaScript.g:370:8: ( LT )
        # ../src/checkjs/parsers/antlr/JavaScript.g:370:8: LT
        pass 
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred242_JavaScript2634)


    # $ANTLR end "synpred242_JavaScript"




    # Delegated rules

    def synpred60_JavaScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred60_JavaScript_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred67_JavaScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred67_JavaScript_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred25_JavaScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred25_JavaScript_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred89_JavaScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred89_JavaScript_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred242_JavaScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred242_JavaScript_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred157_JavaScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred157_JavaScript_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred201_JavaScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred201_JavaScript_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred130_JavaScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred130_JavaScript_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred156_JavaScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred156_JavaScript_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred98_JavaScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred98_JavaScript_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred149_JavaScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred149_JavaScript_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred155_JavaScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred155_JavaScript_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred152_JavaScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred152_JavaScript_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred20_JavaScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred20_JavaScript_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred63_JavaScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred63_JavaScript_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred50_JavaScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred50_JavaScript_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred127_JavaScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred127_JavaScript_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred77_JavaScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred77_JavaScript_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred69_JavaScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred69_JavaScript_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred235_JavaScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred235_JavaScript_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred51_JavaScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred51_JavaScript_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred35_JavaScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred35_JavaScript_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred64_JavaScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred64_JavaScript_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred10_JavaScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred10_JavaScript_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred32_JavaScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred32_JavaScript_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred111_JavaScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred111_JavaScript_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred5_JavaScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred5_JavaScript_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred160_JavaScript(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred160_JavaScript_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



    # lookup tables for DFA #4

    DFA4_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA4_eof = DFA.unpack(
        u"\2\2\2\uffff"
        )

    DFA4_min = DFA.unpack(
        u"\2\26\2\uffff"
        )

    DFA4_max = DFA.unpack(
        u"\2\167\2\uffff"
        )

    DFA4_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA4_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA4_transition = [
        DFA.unpack(u"\1\1\3\3\32\uffff\1\3\1\uffff\1\3\2\uffff\1\3\1\2\1"
        u"\3\1\uffff\1\3\1\uffff\3\3\1\uffff\4\3\1\uffff\1\3\2\uffff\2\3"
        u"\2\uffff\2\3\17\uffff\2\3\12\uffff\14\3"),
        DFA.unpack(u"\1\1\3\3\32\uffff\1\3\1\uffff\1\3\2\uffff\1\3\1\2\1"
        u"\3\1\uffff\1\3\1\uffff\3\3\1\uffff\4\3\1\uffff\1\3\2\uffff\2\3"
        u"\2\uffff\2\3\17\uffff\2\3\12\uffff\14\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #4

    class DFA4(DFA):
        pass


    # lookup tables for DFA #5

    DFA5_eot = DFA.unpack(
        u"\34\uffff"
        )

    DFA5_eof = DFA.unpack(
        u"\34\uffff"
        )

    DFA5_min = DFA.unpack(
        u"\1\27\1\0\32\uffff"
        )

    DFA5_max = DFA.unpack(
        u"\1\167\1\0\32\uffff"
        )

    DFA5_accept = DFA.unpack(
        u"\2\uffff\1\2\30\uffff\1\1"
        )

    DFA5_special = DFA.unpack(
        u"\1\uffff\1\0\32\uffff"
        )

            
    DFA5_transition = [
        DFA.unpack(u"\3\2\32\uffff\1\1\1\uffff\1\2\2\uffff\1\2\1\uffff\1"
        u"\2\1\uffff\1\2\1\uffff\3\2\1\uffff\4\2\1\uffff\1\2\2\uffff\2\2"
        u"\2\uffff\2\2\17\uffff\2\2\12\uffff\14\2"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #5

    class DFA5(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA5_1 = input.LA(1)

                 
                index5_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred5_JavaScript()):
                    s = 27

                elif (True):
                    s = 2

                 
                input.seek(index5_1)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 5, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #18

    DFA18_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA18_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA18_min = DFA.unpack(
        u"\2\26\2\uffff"
        )

    DFA18_max = DFA.unpack(
        u"\2\70\2\uffff"
        )

    DFA18_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA18_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA18_transition = [
        DFA.unpack(u"\1\1\1\2\40\uffff\1\3"),
        DFA.unpack(u"\1\1\1\2\40\uffff\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #18

    class DFA18(DFA):
        pass


    # lookup tables for DFA #17

    DFA17_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA17_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA17_min = DFA.unpack(
        u"\2\26\2\uffff"
        )

    DFA17_max = DFA.unpack(
        u"\2\70\2\uffff"
        )

    DFA17_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA17_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA17_transition = [
        DFA.unpack(u"\1\1\40\uffff\1\3\1\2"),
        DFA.unpack(u"\1\1\40\uffff\1\3\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #17

    class DFA17(DFA):
        pass


    # lookup tables for DFA #24

    DFA24_eot = DFA.unpack(
        u"\34\uffff"
        )

    DFA24_eof = DFA.unpack(
        u"\34\uffff"
        )

    DFA24_min = DFA.unpack(
        u"\1\27\2\uffff\1\0\30\uffff"
        )

    DFA24_max = DFA.unpack(
        u"\1\167\2\uffff\1\0\30\uffff"
        )

    DFA24_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\15\uffff\1\3\1\4\2\uffff\1\5\1\6\1\7\1\10\1\12"
        u"\1\13\1\14\1\11"
        )

    DFA24_special = DFA.unpack(
        u"\3\uffff\1\0\30\uffff"
        )

            
    DFA24_transition = [
        DFA.unpack(u"\1\3\2\2\32\uffff\1\2\1\uffff\1\2\2\uffff\1\2\1\uffff"
        u"\1\1\1\uffff\1\20\1\uffff\3\21\1\uffff\1\24\1\25\1\26\1\27\1\uffff"
        u"\1\30\2\uffff\1\31\1\32\2\uffff\2\2\17\uffff\2\2\12\uffff\14\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #24

    class DFA24(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA24_3 = input.LA(1)

                 
                index24_3 = input.index()
                input.rewind()
                s = -1
                if (self.synpred25_JavaScript()):
                    s = 2

                elif (self.synpred32_JavaScript()):
                    s = 27

                 
                input.seek(index24_3)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 24, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #29

    DFA29_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA29_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA29_min = DFA.unpack(
        u"\2\26\2\uffff"
        )

    DFA29_max = DFA.unpack(
        u"\2\167\2\uffff"
        )

    DFA29_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA29_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA29_transition = [
        DFA.unpack(u"\1\1\3\3\32\uffff\1\3\1\uffff\1\3\2\uffff\1\3\1\2\1"
        u"\3\1\uffff\1\3\1\uffff\3\3\1\uffff\4\3\1\uffff\1\3\2\2\2\3\2\uffff"
        u"\2\3\17\uffff\2\3\12\uffff\14\3"),
        DFA.unpack(u"\1\1\3\3\32\uffff\1\3\1\uffff\1\3\2\uffff\1\3\1\2\1"
        u"\3\1\uffff\1\3\1\uffff\3\3\1\uffff\4\3\1\uffff\1\3\2\2\2\3\2\uffff"
        u"\2\3\17\uffff\2\3\12\uffff\14\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #29

    class DFA29(DFA):
        pass


    # lookup tables for DFA #34

    DFA34_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA34_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA34_min = DFA.unpack(
        u"\2\26\2\uffff"
        )

    DFA34_max = DFA.unpack(
        u"\2\67\2\uffff"
        )

    DFA34_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA34_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA34_transition = [
        DFA.unpack(u"\1\1\36\uffff\1\2\1\uffff\1\3"),
        DFA.unpack(u"\1\1\36\uffff\1\2\1\uffff\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #34

    class DFA34(DFA):
        pass


    # lookup tables for DFA #37

    DFA37_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA37_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA37_min = DFA.unpack(
        u"\2\26\2\uffff"
        )

    DFA37_max = DFA.unpack(
        u"\2\67\2\uffff"
        )

    DFA37_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA37_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA37_transition = [
        DFA.unpack(u"\1\1\36\uffff\1\2\1\uffff\1\3"),
        DFA.unpack(u"\1\1\36\uffff\1\2\1\uffff\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #37

    class DFA37(DFA):
        pass


    # lookup tables for DFA #40

    DFA40_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA40_eof = DFA.unpack(
        u"\1\uffff\2\3\2\uffff"
        )

    DFA40_min = DFA.unpack(
        u"\1\27\2\26\2\uffff"
        )

    DFA40_max = DFA.unpack(
        u"\1\27\2\74\2\uffff"
        )

    DFA40_accept = DFA.unpack(
        u"\3\uffff\1\2\1\1"
        )

    DFA40_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA40_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\2\36\uffff\1\3\1\uffff\1\3\4\uffff\1\4"),
        DFA.unpack(u"\1\2\36\uffff\1\3\1\uffff\1\3\4\uffff\1\4"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #40

    class DFA40(DFA):
        pass


    # lookup tables for DFA #50

    DFA50_eot = DFA.unpack(
        u"\34\uffff"
        )

    DFA50_eof = DFA.unpack(
        u"\34\uffff"
        )

    DFA50_min = DFA.unpack(
        u"\1\27\12\uffff\1\0\20\uffff"
        )

    DFA50_max = DFA.unpack(
        u"\1\167\12\uffff\1\0\20\uffff"
        )

    DFA50_accept = DFA.unpack(
        u"\1\uffff\1\1\31\uffff\1\2"
        )

    DFA50_special = DFA.unpack(
        u"\13\uffff\1\0\20\uffff"
        )

            
    DFA50_transition = [
        DFA.unpack(u"\3\1\32\uffff\1\1\1\uffff\1\1\2\uffff\1\13\1\uffff\1"
        u"\1\1\uffff\1\1\1\uffff\3\1\1\uffff\4\1\1\uffff\1\1\2\uffff\2\1"
        u"\2\uffff\2\1\17\uffff\2\1\12\uffff\14\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #50

    class DFA50(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA50_11 = input.LA(1)

                 
                index50_11 = input.index()
                input.rewind()
                s = -1
                if (self.synpred60_JavaScript()):
                    s = 1

                elif (True):
                    s = 27

                 
                input.seek(index50_11)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 50, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #53

    DFA53_eot = DFA.unpack(
        u"\34\uffff"
        )

    DFA53_eof = DFA.unpack(
        u"\34\uffff"
        )

    DFA53_min = DFA.unpack(
        u"\1\27\12\uffff\1\0\20\uffff"
        )

    DFA53_max = DFA.unpack(
        u"\1\167\12\uffff\1\0\20\uffff"
        )

    DFA53_accept = DFA.unpack(
        u"\1\uffff\1\1\31\uffff\1\2"
        )

    DFA53_special = DFA.unpack(
        u"\13\uffff\1\0\20\uffff"
        )

            
    DFA53_transition = [
        DFA.unpack(u"\3\1\32\uffff\1\1\1\uffff\1\1\2\uffff\1\13\1\uffff\1"
        u"\1\1\uffff\1\1\1\uffff\3\1\1\uffff\4\1\1\uffff\1\1\2\uffff\2\1"
        u"\2\uffff\2\1\17\uffff\2\1\12\uffff\14\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #53

    class DFA53(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA53_11 = input.LA(1)

                 
                index53_11 = input.index()
                input.rewind()
                s = -1
                if (self.synpred63_JavaScript()):
                    s = 1

                elif (True):
                    s = 27

                 
                input.seek(index53_11)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 53, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #57

    DFA57_eot = DFA.unpack(
        u"\34\uffff"
        )

    DFA57_eof = DFA.unpack(
        u"\34\uffff"
        )

    DFA57_min = DFA.unpack(
        u"\1\27\12\uffff\1\0\20\uffff"
        )

    DFA57_max = DFA.unpack(
        u"\1\167\12\uffff\1\0\20\uffff"
        )

    DFA57_accept = DFA.unpack(
        u"\1\uffff\1\1\31\uffff\1\2"
        )

    DFA57_special = DFA.unpack(
        u"\13\uffff\1\0\20\uffff"
        )

            
    DFA57_transition = [
        DFA.unpack(u"\3\1\32\uffff\1\1\1\uffff\1\1\2\uffff\1\13\1\uffff\1"
        u"\1\1\uffff\1\1\1\uffff\3\1\1\uffff\4\1\1\uffff\1\1\2\uffff\2\1"
        u"\2\uffff\2\1\17\uffff\2\1\12\uffff\14\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #57

    class DFA57(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA57_11 = input.LA(1)

                 
                index57_11 = input.index()
                input.rewind()
                s = -1
                if (self.synpred69_JavaScript()):
                    s = 1

                elif (True):
                    s = 27

                 
                input.seek(index57_11)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 57, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #65

    DFA65_eot = DFA.unpack(
        u"\34\uffff"
        )

    DFA65_eof = DFA.unpack(
        u"\34\uffff"
        )

    DFA65_min = DFA.unpack(
        u"\1\27\12\uffff\1\0\20\uffff"
        )

    DFA65_max = DFA.unpack(
        u"\1\167\12\uffff\1\0\20\uffff"
        )

    DFA65_accept = DFA.unpack(
        u"\1\uffff\1\1\31\uffff\1\2"
        )

    DFA65_special = DFA.unpack(
        u"\13\uffff\1\0\20\uffff"
        )

            
    DFA65_transition = [
        DFA.unpack(u"\3\1\32\uffff\1\1\1\uffff\1\1\2\uffff\1\13\1\uffff\1"
        u"\1\1\uffff\1\1\1\uffff\3\1\1\uffff\4\1\1\uffff\1\1\2\uffff\2\1"
        u"\2\uffff\2\1\17\uffff\2\1\12\uffff\14\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #65

    class DFA65(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA65_11 = input.LA(1)

                 
                index65_11 = input.index()
                input.rewind()
                s = -1
                if (self.synpred77_JavaScript()):
                    s = 1

                elif (True):
                    s = 27

                 
                input.seek(index65_11)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 65, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #68

    DFA68_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA68_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA68_min = DFA.unpack(
        u"\2\26\2\uffff"
        )

    DFA68_max = DFA.unpack(
        u"\2\167\2\uffff"
        )

    DFA68_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA68_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA68_transition = [
        DFA.unpack(u"\1\1\3\2\32\uffff\1\2\1\3\1\2\2\uffff\1\2\1\uffff\1"
        u"\2\23\uffff\2\2\17\uffff\2\2\12\uffff\14\2"),
        DFA.unpack(u"\1\1\3\2\32\uffff\1\2\1\3\1\2\2\uffff\1\2\1\uffff\1"
        u"\2\23\uffff\2\2\17\uffff\2\2\12\uffff\14\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #68

    class DFA68(DFA):
        pass


    # lookup tables for DFA #71

    DFA71_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA71_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA71_min = DFA.unpack(
        u"\2\26\2\uffff"
        )

    DFA71_max = DFA.unpack(
        u"\2\167\2\uffff"
        )

    DFA71_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA71_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA71_transition = [
        DFA.unpack(u"\1\1\3\2\32\uffff\1\2\1\3\1\2\2\uffff\1\2\25\uffff\2"
        u"\2\17\uffff\2\2\12\uffff\14\2"),
        DFA.unpack(u"\1\1\3\2\32\uffff\1\2\1\3\1\2\2\uffff\1\2\25\uffff"
        u"\2\2\17\uffff\2\2\12\uffff\14\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #71

    class DFA71(DFA):
        pass


    # lookup tables for DFA #74

    DFA74_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA74_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA74_min = DFA.unpack(
        u"\2\26\2\uffff"
        )

    DFA74_max = DFA.unpack(
        u"\2\167\2\uffff"
        )

    DFA74_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA74_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA74_transition = [
        DFA.unpack(u"\1\1\3\2\32\uffff\1\2\1\uffff\1\2\1\uffff\1\3\1\2\25"
        u"\uffff\2\2\17\uffff\2\2\12\uffff\14\2"),
        DFA.unpack(u"\1\1\3\2\32\uffff\1\2\1\uffff\1\2\1\uffff\1\3\1\2\25"
        u"\uffff\2\2\17\uffff\2\2\12\uffff\14\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #74

    class DFA74(DFA):
        pass


    # lookup tables for DFA #77

    DFA77_eot = DFA.unpack(
        u"\34\uffff"
        )

    DFA77_eof = DFA.unpack(
        u"\34\uffff"
        )

    DFA77_min = DFA.unpack(
        u"\1\27\12\uffff\1\0\20\uffff"
        )

    DFA77_max = DFA.unpack(
        u"\1\167\12\uffff\1\0\20\uffff"
        )

    DFA77_accept = DFA.unpack(
        u"\1\uffff\1\1\31\uffff\1\2"
        )

    DFA77_special = DFA.unpack(
        u"\13\uffff\1\0\20\uffff"
        )

            
    DFA77_transition = [
        DFA.unpack(u"\3\1\32\uffff\1\1\1\uffff\1\1\2\uffff\1\13\1\uffff\1"
        u"\1\1\uffff\1\1\1\uffff\3\1\1\uffff\4\1\1\uffff\1\1\2\uffff\2\1"
        u"\2\uffff\2\1\17\uffff\2\1\12\uffff\14\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #77

    class DFA77(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA77_11 = input.LA(1)

                 
                index77_11 = input.index()
                input.rewind()
                s = -1
                if (self.synpred89_JavaScript()):
                    s = 1

                elif (True):
                    s = 27

                 
                input.seek(index77_11)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 77, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #86

    DFA86_eot = DFA.unpack(
        u"\34\uffff"
        )

    DFA86_eof = DFA.unpack(
        u"\34\uffff"
        )

    DFA86_min = DFA.unpack(
        u"\1\27\12\uffff\1\0\20\uffff"
        )

    DFA86_max = DFA.unpack(
        u"\1\167\12\uffff\1\0\20\uffff"
        )

    DFA86_accept = DFA.unpack(
        u"\1\uffff\1\1\31\uffff\1\2"
        )

    DFA86_special = DFA.unpack(
        u"\13\uffff\1\0\20\uffff"
        )

            
    DFA86_transition = [
        DFA.unpack(u"\3\1\32\uffff\1\1\1\uffff\1\1\2\uffff\1\13\1\uffff\1"
        u"\1\1\uffff\1\1\1\uffff\3\1\1\uffff\4\1\1\uffff\1\1\2\uffff\2\1"
        u"\2\uffff\2\1\17\uffff\2\1\12\uffff\14\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #86

    class DFA86(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA86_11 = input.LA(1)

                 
                index86_11 = input.index()
                input.rewind()
                s = -1
                if (self.synpred98_JavaScript()):
                    s = 1

                elif (True):
                    s = 27

                 
                input.seek(index86_11)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 86, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #99

    DFA99_eot = DFA.unpack(
        u"\34\uffff"
        )

    DFA99_eof = DFA.unpack(
        u"\34\uffff"
        )

    DFA99_min = DFA.unpack(
        u"\1\27\12\uffff\1\0\20\uffff"
        )

    DFA99_max = DFA.unpack(
        u"\1\167\12\uffff\1\0\20\uffff"
        )

    DFA99_accept = DFA.unpack(
        u"\1\uffff\1\1\31\uffff\1\2"
        )

    DFA99_special = DFA.unpack(
        u"\13\uffff\1\0\20\uffff"
        )

            
    DFA99_transition = [
        DFA.unpack(u"\3\1\32\uffff\1\1\1\uffff\1\1\2\uffff\1\13\1\uffff\1"
        u"\1\1\uffff\1\1\1\uffff\3\1\1\uffff\4\1\1\uffff\1\1\2\uffff\2\1"
        u"\2\uffff\2\1\17\uffff\2\1\12\uffff\14\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #99

    class DFA99(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA99_11 = input.LA(1)

                 
                index99_11 = input.index()
                input.rewind()
                s = -1
                if (self.synpred111_JavaScript()):
                    s = 1

                elif (True):
                    s = 27

                 
                input.seek(index99_11)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 99, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #107

    DFA107_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA107_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA107_min = DFA.unpack(
        u"\2\26\2\uffff"
        )

    DFA107_max = DFA.unpack(
        u"\2\112\2\uffff"
        )

    DFA107_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA107_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA107_transition = [
        DFA.unpack(u"\1\1\43\uffff\1\2\16\uffff\1\3\1\2"),
        DFA.unpack(u"\1\1\43\uffff\1\2\16\uffff\1\3\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #107

    class DFA107(DFA):
        pass


    # lookup tables for DFA #111

    DFA111_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA111_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA111_min = DFA.unpack(
        u"\2\26\2\uffff"
        )

    DFA111_max = DFA.unpack(
        u"\2\112\2\uffff"
        )

    DFA111_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA111_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA111_transition = [
        DFA.unpack(u"\1\1\43\uffff\1\3\17\uffff\1\2"),
        DFA.unpack(u"\1\1\43\uffff\1\3\17\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #111

    class DFA111(DFA):
        pass


    # lookup tables for DFA #110

    DFA110_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA110_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA110_min = DFA.unpack(
        u"\2\26\2\uffff"
        )

    DFA110_max = DFA.unpack(
        u"\2\111\2\uffff"
        )

    DFA110_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA110_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA110_transition = [
        DFA.unpack(u"\1\1\43\uffff\1\2\16\uffff\1\3"),
        DFA.unpack(u"\1\1\43\uffff\1\2\16\uffff\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #110

    class DFA110(DFA):
        pass


    # lookup tables for DFA #124

    DFA124_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA124_eof = DFA.unpack(
        u"\2\3\2\uffff"
        )

    DFA124_min = DFA.unpack(
        u"\2\26\2\uffff"
        )

    DFA124_max = DFA.unpack(
        u"\2\167\2\uffff"
        )

    DFA124_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA124_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA124_transition = [
        DFA.unpack(u"\1\1\3\3\32\uffff\1\3\1\uffff\1\3\2\uffff\3\3\1\uffff"
        u"\5\3\1\uffff\4\3\1\uffff\5\3\1\uffff\1\2\2\3\17\uffff\2\3\12\uffff"
        u"\14\3"),
        DFA.unpack(u"\1\1\3\3\32\uffff\1\3\1\uffff\1\3\2\uffff\3\3\1\uffff"
        u"\5\3\1\uffff\4\3\1\uffff\5\3\1\uffff\1\2\2\3\17\uffff\2\3\12\uffff"
        u"\14\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #124

    class DFA124(DFA):
        pass


    # lookup tables for DFA #133

    DFA133_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA133_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA133_min = DFA.unpack(
        u"\2\26\2\uffff"
        )

    DFA133_max = DFA.unpack(
        u"\2\121\2\uffff"
        )

    DFA133_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA133_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA133_transition = [
        DFA.unpack(u"\1\1\36\uffff\1\2\1\uffff\1\3\1\2\16\uffff\1\2\11\uffff"
        u"\1\2"),
        DFA.unpack(u"\1\1\36\uffff\1\2\1\uffff\1\3\1\2\16\uffff\1\2\11\uffff"
        u"\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #133

    class DFA133(DFA):
        pass


    # lookup tables for DFA #136

    DFA136_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA136_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA136_min = DFA.unpack(
        u"\2\26\2\uffff"
        )

    DFA136_max = DFA.unpack(
        u"\2\67\2\uffff"
        )

    DFA136_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA136_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA136_transition = [
        DFA.unpack(u"\1\1\36\uffff\1\2\1\uffff\1\3"),
        DFA.unpack(u"\1\1\36\uffff\1\2\1\uffff\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #136

    class DFA136(DFA):
        pass


    # lookup tables for DFA #141

    DFA141_eot = DFA.unpack(
        u"\23\uffff"
        )

    DFA141_eof = DFA.unpack(
        u"\23\uffff"
        )

    DFA141_min = DFA.unpack(
        u"\1\27\15\0\5\uffff"
        )

    DFA141_max = DFA.unpack(
        u"\1\167\15\0\5\uffff"
        )

    DFA141_accept = DFA.unpack(
        u"\16\uffff\1\4\1\1\1\2\1\3\1\5"
        )

    DFA141_special = DFA.unpack(
        u"\1\uffff\1\0\1\1\1\2\1\3\1\4\1\5\1\6\1\7\1\10\1\11\1\12\1\13\1"
        u"\14\5\uffff"
        )

            
    DFA141_transition = [
        DFA.unpack(u"\1\2\1\6\1\7\32\uffff\1\14\1\uffff\1\13\2\uffff\1\12"
        u"\25\uffff\1\15\1\11\17\uffff\2\16\12\uffff\7\16\1\1\1\3\1\4\1\5"
        u"\1\10"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #141

    class DFA141(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA141_1 = input.LA(1)

                 
                index141_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred149_JavaScript()):
                    s = 15

                elif (self.synpred152_JavaScript()):
                    s = 16

                elif (self.synpred155_JavaScript()):
                    s = 17

                elif (self.synpred156_JavaScript()):
                    s = 14

                elif (True):
                    s = 18

                 
                input.seek(index141_1)
                if s >= 0:
                    return s
            elif s == 1: 
                LA141_2 = input.LA(1)

                 
                index141_2 = input.index()
                input.rewind()
                s = -1
                if (self.synpred149_JavaScript()):
                    s = 15

                elif (self.synpred152_JavaScript()):
                    s = 16

                elif (self.synpred155_JavaScript()):
                    s = 17

                elif (self.synpred156_JavaScript()):
                    s = 14

                elif (True):
                    s = 18

                 
                input.seek(index141_2)
                if s >= 0:
                    return s
            elif s == 2: 
                LA141_3 = input.LA(1)

                 
                index141_3 = input.index()
                input.rewind()
                s = -1
                if (self.synpred149_JavaScript()):
                    s = 15

                elif (self.synpred152_JavaScript()):
                    s = 16

                elif (self.synpred155_JavaScript()):
                    s = 17

                elif (self.synpred156_JavaScript()):
                    s = 14

                elif (True):
                    s = 18

                 
                input.seek(index141_3)
                if s >= 0:
                    return s
            elif s == 3: 
                LA141_4 = input.LA(1)

                 
                index141_4 = input.index()
                input.rewind()
                s = -1
                if (self.synpred149_JavaScript()):
                    s = 15

                elif (self.synpred152_JavaScript()):
                    s = 16

                elif (self.synpred155_JavaScript()):
                    s = 17

                elif (self.synpred156_JavaScript()):
                    s = 14

                elif (True):
                    s = 18

                 
                input.seek(index141_4)
                if s >= 0:
                    return s
            elif s == 4: 
                LA141_5 = input.LA(1)

                 
                index141_5 = input.index()
                input.rewind()
                s = -1
                if (self.synpred149_JavaScript()):
                    s = 15

                elif (self.synpred152_JavaScript()):
                    s = 16

                elif (self.synpred155_JavaScript()):
                    s = 17

                elif (self.synpred156_JavaScript()):
                    s = 14

                elif (True):
                    s = 18

                 
                input.seek(index141_5)
                if s >= 0:
                    return s
            elif s == 5: 
                LA141_6 = input.LA(1)

                 
                index141_6 = input.index()
                input.rewind()
                s = -1
                if (self.synpred149_JavaScript()):
                    s = 15

                elif (self.synpred152_JavaScript()):
                    s = 16

                elif (self.synpred155_JavaScript()):
                    s = 17

                elif (self.synpred156_JavaScript()):
                    s = 14

                elif (True):
                    s = 18

                 
                input.seek(index141_6)
                if s >= 0:
                    return s
            elif s == 6: 
                LA141_7 = input.LA(1)

                 
                index141_7 = input.index()
                input.rewind()
                s = -1
                if (self.synpred149_JavaScript()):
                    s = 15

                elif (self.synpred152_JavaScript()):
                    s = 16

                elif (self.synpred155_JavaScript()):
                    s = 17

                elif (self.synpred156_JavaScript()):
                    s = 14

                elif (True):
                    s = 18

                 
                input.seek(index141_7)
                if s >= 0:
                    return s
            elif s == 7: 
                LA141_8 = input.LA(1)

                 
                index141_8 = input.index()
                input.rewind()
                s = -1
                if (self.synpred149_JavaScript()):
                    s = 15

                elif (self.synpred152_JavaScript()):
                    s = 16

                elif (self.synpred155_JavaScript()):
                    s = 17

                elif (self.synpred156_JavaScript()):
                    s = 14

                elif (True):
                    s = 18

                 
                input.seek(index141_8)
                if s >= 0:
                    return s
            elif s == 8: 
                LA141_9 = input.LA(1)

                 
                index141_9 = input.index()
                input.rewind()
                s = -1
                if (self.synpred149_JavaScript()):
                    s = 15

                elif (self.synpred152_JavaScript()):
                    s = 16

                elif (self.synpred155_JavaScript()):
                    s = 17

                elif (self.synpred156_JavaScript()):
                    s = 14

                elif (True):
                    s = 18

                 
                input.seek(index141_9)
                if s >= 0:
                    return s
            elif s == 9: 
                LA141_10 = input.LA(1)

                 
                index141_10 = input.index()
                input.rewind()
                s = -1
                if (self.synpred149_JavaScript()):
                    s = 15

                elif (self.synpred152_JavaScript()):
                    s = 16

                elif (self.synpred155_JavaScript()):
                    s = 17

                elif (self.synpred156_JavaScript()):
                    s = 14

                elif (True):
                    s = 18

                 
                input.seek(index141_10)
                if s >= 0:
                    return s
            elif s == 10: 
                LA141_11 = input.LA(1)

                 
                index141_11 = input.index()
                input.rewind()
                s = -1
                if (self.synpred149_JavaScript()):
                    s = 15

                elif (self.synpred152_JavaScript()):
                    s = 16

                elif (self.synpred155_JavaScript()):
                    s = 17

                elif (self.synpred156_JavaScript()):
                    s = 14

                elif (True):
                    s = 18

                 
                input.seek(index141_11)
                if s >= 0:
                    return s
            elif s == 11: 
                LA141_12 = input.LA(1)

                 
                index141_12 = input.index()
                input.rewind()
                s = -1
                if (self.synpred149_JavaScript()):
                    s = 15

                elif (self.synpred152_JavaScript()):
                    s = 16

                elif (self.synpred155_JavaScript()):
                    s = 17

                elif (self.synpred156_JavaScript()):
                    s = 14

                elif (True):
                    s = 18

                 
                input.seek(index141_12)
                if s >= 0:
                    return s
            elif s == 12: 
                LA141_13 = input.LA(1)

                 
                index141_13 = input.index()
                input.rewind()
                s = -1
                if (self.synpred149_JavaScript()):
                    s = 15

                elif (self.synpred152_JavaScript()):
                    s = 16

                elif (self.synpred155_JavaScript()):
                    s = 17

                elif (self.synpred156_JavaScript()):
                    s = 14

                elif (True):
                    s = 18

                 
                input.seek(index141_13)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 141, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #144

    DFA144_eot = DFA.unpack(
        u"\20\uffff"
        )

    DFA144_eof = DFA.unpack(
        u"\20\uffff"
        )

    DFA144_min = DFA.unpack(
        u"\1\27\15\0\2\uffff"
        )

    DFA144_max = DFA.unpack(
        u"\1\167\15\0\2\uffff"
        )

    DFA144_accept = DFA.unpack(
        u"\16\uffff\1\1\1\2"
        )

    DFA144_special = DFA.unpack(
        u"\1\uffff\1\0\1\1\1\2\1\3\1\4\1\5\1\6\1\7\1\10\1\11\1\12\1\13\1"
        u"\14\2\uffff"
        )

            
    DFA144_transition = [
        DFA.unpack(u"\1\2\1\6\1\7\32\uffff\1\14\1\uffff\1\13\2\uffff\1\12"
        u"\25\uffff\1\15\1\11\17\uffff\2\16\12\uffff\7\16\1\1\1\3\1\4\1\5"
        u"\1\10"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #144

    class DFA144(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA144_1 = input.LA(1)

                 
                index144_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred157_JavaScript()):
                    s = 14

                elif (True):
                    s = 15

                 
                input.seek(index144_1)
                if s >= 0:
                    return s
            elif s == 1: 
                LA144_2 = input.LA(1)

                 
                index144_2 = input.index()
                input.rewind()
                s = -1
                if (self.synpred157_JavaScript()):
                    s = 14

                elif (True):
                    s = 15

                 
                input.seek(index144_2)
                if s >= 0:
                    return s
            elif s == 2: 
                LA144_3 = input.LA(1)

                 
                index144_3 = input.index()
                input.rewind()
                s = -1
                if (self.synpred157_JavaScript()):
                    s = 14

                elif (True):
                    s = 15

                 
                input.seek(index144_3)
                if s >= 0:
                    return s
            elif s == 3: 
                LA144_4 = input.LA(1)

                 
                index144_4 = input.index()
                input.rewind()
                s = -1
                if (self.synpred157_JavaScript()):
                    s = 14

                elif (True):
                    s = 15

                 
                input.seek(index144_4)
                if s >= 0:
                    return s
            elif s == 4: 
                LA144_5 = input.LA(1)

                 
                index144_5 = input.index()
                input.rewind()
                s = -1
                if (self.synpred157_JavaScript()):
                    s = 14

                elif (True):
                    s = 15

                 
                input.seek(index144_5)
                if s >= 0:
                    return s
            elif s == 5: 
                LA144_6 = input.LA(1)

                 
                index144_6 = input.index()
                input.rewind()
                s = -1
                if (self.synpred157_JavaScript()):
                    s = 14

                elif (True):
                    s = 15

                 
                input.seek(index144_6)
                if s >= 0:
                    return s
            elif s == 6: 
                LA144_7 = input.LA(1)

                 
                index144_7 = input.index()
                input.rewind()
                s = -1
                if (self.synpred157_JavaScript()):
                    s = 14

                elif (True):
                    s = 15

                 
                input.seek(index144_7)
                if s >= 0:
                    return s
            elif s == 7: 
                LA144_8 = input.LA(1)

                 
                index144_8 = input.index()
                input.rewind()
                s = -1
                if (self.synpred157_JavaScript()):
                    s = 14

                elif (True):
                    s = 15

                 
                input.seek(index144_8)
                if s >= 0:
                    return s
            elif s == 8: 
                LA144_9 = input.LA(1)

                 
                index144_9 = input.index()
                input.rewind()
                s = -1
                if (self.synpred157_JavaScript()):
                    s = 14

                elif (True):
                    s = 15

                 
                input.seek(index144_9)
                if s >= 0:
                    return s
            elif s == 9: 
                LA144_10 = input.LA(1)

                 
                index144_10 = input.index()
                input.rewind()
                s = -1
                if (self.synpred157_JavaScript()):
                    s = 14

                elif (True):
                    s = 15

                 
                input.seek(index144_10)
                if s >= 0:
                    return s
            elif s == 10: 
                LA144_11 = input.LA(1)

                 
                index144_11 = input.index()
                input.rewind()
                s = -1
                if (self.synpred157_JavaScript()):
                    s = 14

                elif (True):
                    s = 15

                 
                input.seek(index144_11)
                if s >= 0:
                    return s
            elif s == 11: 
                LA144_12 = input.LA(1)

                 
                index144_12 = input.index()
                input.rewind()
                s = -1
                if (self.synpred157_JavaScript()):
                    s = 14

                elif (True):
                    s = 15

                 
                input.seek(index144_12)
                if s >= 0:
                    return s
            elif s == 12: 
                LA144_13 = input.LA(1)

                 
                index144_13 = input.index()
                input.rewind()
                s = -1
                if (self.synpred157_JavaScript()):
                    s = 14

                elif (True):
                    s = 15

                 
                input.seek(index144_13)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 144, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #146

    DFA146_eot = DFA.unpack(
        u"\17\uffff"
        )

    DFA146_eof = DFA.unpack(
        u"\17\uffff"
        )

    DFA146_min = DFA.unpack(
        u"\1\27\14\uffff\1\0\1\uffff"
        )

    DFA146_max = DFA.unpack(
        u"\1\167\14\uffff\1\0\1\uffff"
        )

    DFA146_accept = DFA.unpack(
        u"\1\uffff\1\1\14\uffff\1\2"
        )

    DFA146_special = DFA.unpack(
        u"\15\uffff\1\0\1\uffff"
        )

            
    DFA146_transition = [
        DFA.unpack(u"\3\1\32\uffff\1\1\1\uffff\1\1\2\uffff\1\1\25\uffff\1"
        u"\15\1\1\42\uffff\5\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #146

    class DFA146(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA146_13 = input.LA(1)

                 
                index146_13 = input.index()
                input.rewind()
                s = -1
                if (self.synpred160_JavaScript()):
                    s = 1

                elif (True):
                    s = 14

                 
                input.seek(index146_13)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 146, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #151

    DFA151_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA151_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA151_min = DFA.unpack(
        u"\2\26\2\uffff"
        )

    DFA151_max = DFA.unpack(
        u"\1\160\1\153\2\uffff"
        )

    DFA151_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA151_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA151_transition = [
        DFA.unpack(u"\1\1\31\uffff\1\2\4\uffff\4\2\1\uffff\1\2\1\uffff\1"
        u"\2\5\uffff\1\2\4\uffff\1\2\10\uffff\1\3\1\2\1\3\31\2\3\uffff\2"
        u"\2"),
        DFA.unpack(u"\1\1\31\uffff\1\2\4\uffff\4\2\1\uffff\1\2\1\uffff\1"
        u"\2\5\uffff\1\2\4\uffff\1\2\10\uffff\1\3\1\2\1\3\31\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #151

    class DFA151(DFA):
        pass


    # lookup tables for DFA #155

    DFA155_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA155_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA155_min = DFA.unpack(
        u"\2\26\2\uffff"
        )

    DFA155_max = DFA.unpack(
        u"\2\136\2\uffff"
        )

    DFA155_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA155_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA155_transition = [
        DFA.unpack(u"\1\1\36\uffff\1\2\1\3\2\2\1\uffff\1\2\7\uffff\1\2\4"
        u"\uffff\1\2\10\uffff\1\3\1\2\1\3\13\uffff\1\2"),
        DFA.unpack(u"\1\1\36\uffff\1\2\1\3\2\2\1\uffff\1\2\7\uffff\1\2\4"
        u"\uffff\1\2\10\uffff\1\3\1\2\1\3\13\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #155

    class DFA155(DFA):
        pass


    # lookup tables for DFA #161

    DFA161_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA161_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA161_min = DFA.unpack(
        u"\2\26\2\uffff"
        )

    DFA161_max = DFA.unpack(
        u"\2\167\2\uffff"
        )

    DFA161_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA161_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA161_transition = [
        DFA.unpack(u"\1\1\3\2\32\uffff\1\2\1\uffff\1\2\1\uffff\1\3\1\2\25"
        u"\uffff\2\2\17\uffff\2\2\12\uffff\14\2"),
        DFA.unpack(u"\1\1\3\2\32\uffff\1\2\1\uffff\1\2\1\uffff\1\3\1\2\25"
        u"\uffff\2\2\17\uffff\2\2\12\uffff\14\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #161

    class DFA161(DFA):
        pass


    # lookup tables for DFA #160

    DFA160_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA160_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA160_min = DFA.unpack(
        u"\2\26\2\uffff"
        )

    DFA160_max = DFA.unpack(
        u"\2\70\2\uffff"
        )

    DFA160_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA160_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA160_transition = [
        DFA.unpack(u"\1\1\40\uffff\1\3\1\2"),
        DFA.unpack(u"\1\1\40\uffff\1\3\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #160

    class DFA160(DFA):
        pass


    # lookup tables for DFA #170

    DFA170_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA170_eof = DFA.unpack(
        u"\1\3\3\uffff"
        )

    DFA170_min = DFA.unpack(
        u"\2\26\2\uffff"
        )

    DFA170_max = DFA.unpack(
        u"\2\136\2\uffff"
        )

    DFA170_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA170_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA170_transition = [
        DFA.unpack(u"\1\1\36\uffff\1\3\1\uffff\1\3\12\uffff\1\3\33\uffff"
        u"\1\2"),
        DFA.unpack(u"\1\1\36\uffff\1\3\1\uffff\1\3\12\uffff\1\3\33\uffff"
        u"\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #170

    class DFA170(DFA):
        pass


    # lookup tables for DFA #173

    DFA173_eot = DFA.unpack(
        u"\20\uffff"
        )

    DFA173_eof = DFA.unpack(
        u"\20\uffff"
        )

    DFA173_min = DFA.unpack(
        u"\1\27\15\0\2\uffff"
        )

    DFA173_max = DFA.unpack(
        u"\1\167\15\0\2\uffff"
        )

    DFA173_accept = DFA.unpack(
        u"\16\uffff\1\2\1\1"
        )

    DFA173_special = DFA.unpack(
        u"\1\uffff\1\0\1\1\1\2\1\3\1\4\1\5\1\6\1\7\1\10\1\11\1\12\1\13\1"
        u"\14\2\uffff"
        )

            
    DFA173_transition = [
        DFA.unpack(u"\1\2\1\6\1\7\32\uffff\1\14\1\uffff\1\13\2\uffff\1\12"
        u"\25\uffff\1\15\1\11\17\uffff\2\16\12\uffff\7\16\1\1\1\3\1\4\1\5"
        u"\1\10"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #173

    class DFA173(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA173_1 = input.LA(1)

                 
                index173_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred201_JavaScript()):
                    s = 15

                elif (True):
                    s = 14

                 
                input.seek(index173_1)
                if s >= 0:
                    return s
            elif s == 1: 
                LA173_2 = input.LA(1)

                 
                index173_2 = input.index()
                input.rewind()
                s = -1
                if (self.synpred201_JavaScript()):
                    s = 15

                elif (True):
                    s = 14

                 
                input.seek(index173_2)
                if s >= 0:
                    return s
            elif s == 2: 
                LA173_3 = input.LA(1)

                 
                index173_3 = input.index()
                input.rewind()
                s = -1
                if (self.synpred201_JavaScript()):
                    s = 15

                elif (True):
                    s = 14

                 
                input.seek(index173_3)
                if s >= 0:
                    return s
            elif s == 3: 
                LA173_4 = input.LA(1)

                 
                index173_4 = input.index()
                input.rewind()
                s = -1
                if (self.synpred201_JavaScript()):
                    s = 15

                elif (True):
                    s = 14

                 
                input.seek(index173_4)
                if s >= 0:
                    return s
            elif s == 4: 
                LA173_5 = input.LA(1)

                 
                index173_5 = input.index()
                input.rewind()
                s = -1
                if (self.synpred201_JavaScript()):
                    s = 15

                elif (True):
                    s = 14

                 
                input.seek(index173_5)
                if s >= 0:
                    return s
            elif s == 5: 
                LA173_6 = input.LA(1)

                 
                index173_6 = input.index()
                input.rewind()
                s = -1
                if (self.synpred201_JavaScript()):
                    s = 15

                elif (True):
                    s = 14

                 
                input.seek(index173_6)
                if s >= 0:
                    return s
            elif s == 6: 
                LA173_7 = input.LA(1)

                 
                index173_7 = input.index()
                input.rewind()
                s = -1
                if (self.synpred201_JavaScript()):
                    s = 15

                elif (True):
                    s = 14

                 
                input.seek(index173_7)
                if s >= 0:
                    return s
            elif s == 7: 
                LA173_8 = input.LA(1)

                 
                index173_8 = input.index()
                input.rewind()
                s = -1
                if (self.synpred201_JavaScript()):
                    s = 15

                elif (True):
                    s = 14

                 
                input.seek(index173_8)
                if s >= 0:
                    return s
            elif s == 8: 
                LA173_9 = input.LA(1)

                 
                index173_9 = input.index()
                input.rewind()
                s = -1
                if (self.synpred201_JavaScript()):
                    s = 15

                elif (True):
                    s = 14

                 
                input.seek(index173_9)
                if s >= 0:
                    return s
            elif s == 9: 
                LA173_10 = input.LA(1)

                 
                index173_10 = input.index()
                input.rewind()
                s = -1
                if (self.synpred201_JavaScript()):
                    s = 15

                elif (True):
                    s = 14

                 
                input.seek(index173_10)
                if s >= 0:
                    return s
            elif s == 10: 
                LA173_11 = input.LA(1)

                 
                index173_11 = input.index()
                input.rewind()
                s = -1
                if (self.synpred201_JavaScript()):
                    s = 15

                elif (True):
                    s = 14

                 
                input.seek(index173_11)
                if s >= 0:
                    return s
            elif s == 11: 
                LA173_12 = input.LA(1)

                 
                index173_12 = input.index()
                input.rewind()
                s = -1
                if (self.synpred201_JavaScript()):
                    s = 15

                elif (True):
                    s = 14

                 
                input.seek(index173_12)
                if s >= 0:
                    return s
            elif s == 12: 
                LA173_13 = input.LA(1)

                 
                index173_13 = input.index()
                input.rewind()
                s = -1
                if (self.synpred201_JavaScript()):
                    s = 15

                elif (True):
                    s = 14

                 
                input.seek(index173_13)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 173, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #184

    DFA184_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA184_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA184_min = DFA.unpack(
        u"\2\26\2\uffff"
        )

    DFA184_max = DFA.unpack(
        u"\2\121\2\uffff"
        )

    DFA184_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA184_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA184_transition = [
        DFA.unpack(u"\1\1\40\uffff\1\3\31\uffff\1\2"),
        DFA.unpack(u"\1\1\40\uffff\1\3\31\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #184

    class DFA184(DFA):
        pass


    # lookup tables for DFA #183

    DFA183_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA183_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA183_min = DFA.unpack(
        u"\2\26\2\uffff"
        )

    DFA183_max = DFA.unpack(
        u"\2\167\2\uffff"
        )

    DFA183_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA183_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA183_transition = [
        DFA.unpack(u"\1\1\3\2\32\uffff\1\2\1\uffff\1\2\1\3\1\uffff\1\2\25"
        u"\uffff\2\2\1\3\16\uffff\2\2\12\uffff\14\2"),
        DFA.unpack(u"\1\1\3\2\32\uffff\1\2\1\uffff\1\2\1\3\1\uffff\1\2\25"
        u"\uffff\2\2\1\3\16\uffff\2\2\12\uffff\14\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #183

    class DFA183(DFA):
        pass


    # lookup tables for DFA #189

    DFA189_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA189_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA189_min = DFA.unpack(
        u"\2\26\2\uffff"
        )

    DFA189_max = DFA.unpack(
        u"\2\72\2\uffff"
        )

    DFA189_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA189_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA189_transition = [
        DFA.unpack(u"\1\1\40\uffff\1\3\2\uffff\1\2"),
        DFA.unpack(u"\1\1\40\uffff\1\3\2\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #189

    class DFA189(DFA):
        pass


    # lookup tables for DFA #210

    DFA210_eot = DFA.unpack(
        u"\34\uffff"
        )

    DFA210_eof = DFA.unpack(
        u"\34\uffff"
        )

    DFA210_min = DFA.unpack(
        u"\1\27\12\uffff\1\0\20\uffff"
        )

    DFA210_max = DFA.unpack(
        u"\1\167\12\uffff\1\0\20\uffff"
        )

    DFA210_accept = DFA.unpack(
        u"\1\uffff\1\1\31\uffff\1\2"
        )

    DFA210_special = DFA.unpack(
        u"\13\uffff\1\0\20\uffff"
        )

            
    DFA210_transition = [
        DFA.unpack(u"\3\1\32\uffff\1\1\1\uffff\1\1\2\uffff\1\13\1\uffff\1"
        u"\1\1\uffff\1\1\1\uffff\3\1\1\uffff\4\1\1\uffff\1\1\2\uffff\2\1"
        u"\2\uffff\2\1\17\uffff\2\1\12\uffff\14\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #210

    class DFA210(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA210_11 = input.LA(1)

                 
                index210_11 = input.index()
                input.rewind()
                s = -1
                if (self.synpred63_JavaScript()):
                    s = 1

                elif (True):
                    s = 27

                 
                input.seek(index210_11)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 210, _s, input)
            self_.error(nvae)
            raise nvae
 

    FOLLOW_LT_in_program187 = frozenset([22, 23, 24, 25, 52, 54, 57, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_sourceElements_in_program191 = frozenset([22])
    FOLLOW_LT_in_program193 = frozenset([22])
    FOLLOW_EOF_in_program197 = frozenset([1])
    FOLLOW_sourceElement_in_sourceElements209 = frozenset([1, 22, 23, 24, 25, 52, 54, 57, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_sourceElements212 = frozenset([22, 23, 24, 25, 52, 54, 57, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_sourceElement_in_sourceElements216 = frozenset([1, 22, 23, 24, 25, 52, 54, 57, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_functionDeclaration_in_sourceElement229 = frozenset([1])
    FOLLOW_statement_in_sourceElement234 = frozenset([1])
    FOLLOW_52_in_functionDeclaration246 = frozenset([22, 23])
    FOLLOW_LT_in_functionDeclaration248 = frozenset([22, 23])
    FOLLOW_Identifier_in_functionDeclaration251 = frozenset([22, 54])
    FOLLOW_LT_in_functionDeclaration253 = frozenset([22, 54])
    FOLLOW_formalParameterList_in_functionDeclaration256 = frozenset([22, 57])
    FOLLOW_LT_in_functionDeclaration258 = frozenset([22, 57])
    FOLLOW_functionBody_in_functionDeclaration261 = frozenset([1, 53])
    FOLLOW_53_in_functionDeclaration263 = frozenset([1])
    FOLLOW_52_in_functionExpression299 = frozenset([22, 23, 54])
    FOLLOW_LT_in_functionExpression301 = frozenset([22, 23, 54])
    FOLLOW_Identifier_in_functionExpression304 = frozenset([22, 54])
    FOLLOW_LT_in_functionExpression307 = frozenset([22, 54])
    FOLLOW_formalParameterList_in_functionExpression310 = frozenset([22, 57])
    FOLLOW_LT_in_functionExpression312 = frozenset([22, 57])
    FOLLOW_functionBody_in_functionExpression315 = frozenset([1])
    FOLLOW_54_in_formalParameterList345 = frozenset([22, 23, 56])
    FOLLOW_LT_in_formalParameterList348 = frozenset([22, 23])
    FOLLOW_Identifier_in_formalParameterList351 = frozenset([22, 55, 56])
    FOLLOW_LT_in_formalParameterList354 = frozenset([22, 55])
    FOLLOW_55_in_formalParameterList357 = frozenset([22, 23])
    FOLLOW_LT_in_formalParameterList359 = frozenset([22, 23])
    FOLLOW_Identifier_in_formalParameterList362 = frozenset([22, 55, 56])
    FOLLOW_LT_in_formalParameterList368 = frozenset([22, 56])
    FOLLOW_56_in_formalParameterList371 = frozenset([1])
    FOLLOW_57_in_functionBody400 = frozenset([22, 23, 24, 25, 52, 54, 57, 58, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_functionBody402 = frozenset([22, 23, 24, 25, 52, 54, 57, 58, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_sourceElements_in_functionBody405 = frozenset([22, 58])
    FOLLOW_LT_in_functionBody408 = frozenset([22, 58])
    FOLLOW_58_in_functionBody411 = frozenset([1])
    FOLLOW_57_in_djangoVariable441 = frozenset([57])
    FOLLOW_57_in_djangoVariable443 = frozenset([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_58_in_djangoVariable446 = frozenset([58])
    FOLLOW_58_in_djangoVariable448 = frozenset([1])
    FOLLOW_variableStatement_in_statement474 = frozenset([1])
    FOLLOW_expressionStatement_in_statement481 = frozenset([1])
    FOLLOW_ifStatement_in_statement491 = frozenset([1])
    FOLLOW_iterationStatement_in_statement496 = frozenset([1])
    FOLLOW_continueStatement_in_statement501 = frozenset([1])
    FOLLOW_breakStatement_in_statement506 = frozenset([1])
    FOLLOW_returnStatement_in_statement511 = frozenset([1])
    FOLLOW_withStatement_in_statement516 = frozenset([1])
    FOLLOW_labelledStatement_in_statement521 = frozenset([1])
    FOLLOW_switchStatement_in_statement526 = frozenset([1])
    FOLLOW_throwStatement_in_statement531 = frozenset([1])
    FOLLOW_tryStatement_in_statement536 = frozenset([1])
    FOLLOW_57_in_statementBlock547 = frozenset([22, 23, 24, 25, 52, 54, 57, 58, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_statementBlock549 = frozenset([22, 23, 24, 25, 52, 54, 57, 58, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_statementList_in_statementBlock553 = frozenset([22, 58])
    FOLLOW_LT_in_statementBlock556 = frozenset([22, 58])
    FOLLOW_58_in_statementBlock560 = frozenset([1])
    FOLLOW_statement_in_statementList571 = frozenset([1, 22, 23, 24, 25, 52, 54, 57, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_statementList574 = frozenset([22, 23, 24, 25, 52, 54, 57, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_statement_in_statementList578 = frozenset([1, 22, 23, 24, 25, 52, 54, 57, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_59_in_variableStatement591 = frozenset([22, 23])
    FOLLOW_LT_in_variableStatement594 = frozenset([22, 23])
    FOLLOW_variableDeclarationList_in_variableStatement598 = frozenset([22, 53])
    FOLLOW_LT_in_variableStatement600 = frozenset([22, 53])
    FOLLOW_53_in_variableStatement604 = frozenset([1])
    FOLLOW_variableDeclaration_in_variableDeclarationList616 = frozenset([1, 22, 55])
    FOLLOW_LT_in_variableDeclarationList619 = frozenset([22, 55])
    FOLLOW_55_in_variableDeclarationList623 = frozenset([22, 23])
    FOLLOW_LT_in_variableDeclarationList626 = frozenset([22, 23])
    FOLLOW_variableDeclaration_in_variableDeclarationList630 = frozenset([1, 22, 55])
    FOLLOW_variableDeclarationNoIn_in_variableDeclarationListNoIn643 = frozenset([1, 22, 55])
    FOLLOW_LT_in_variableDeclarationListNoIn646 = frozenset([22, 55])
    FOLLOW_55_in_variableDeclarationListNoIn650 = frozenset([22, 23])
    FOLLOW_LT_in_variableDeclarationListNoIn653 = frozenset([22, 23])
    FOLLOW_variableDeclarationNoIn_in_variableDeclarationListNoIn657 = frozenset([1, 22, 55])
    FOLLOW_Identifier_in_variableDeclaration670 = frozenset([22, 60])
    FOLLOW_LT_in_variableDeclaration672 = frozenset([22, 60])
    FOLLOW_initialiser_in_variableDeclaration675 = frozenset([1])
    FOLLOW_Identifier_in_variableDeclaration691 = frozenset([1, 22])
    FOLLOW_LT_in_variableDeclaration693 = frozenset([1, 22])
    FOLLOW_Identifier_in_variableDeclarationNoIn714 = frozenset([1, 22, 60])
    FOLLOW_LT_in_variableDeclarationNoIn716 = frozenset([1, 22, 60])
    FOLLOW_initialiserNoIn_in_variableDeclarationNoIn719 = frozenset([1])
    FOLLOW_60_in_initialiser750 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_initialiser753 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_assignmentExpression_in_initialiser757 = frozenset([1])
    FOLLOW_60_in_initialiserNoIn768 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_initialiserNoIn771 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_assignmentExpressionNoIn_in_initialiserNoIn775 = frozenset([1])
    FOLLOW_53_in_emptyStatement786 = frozenset([1])
    FOLLOW_expression_in_expressionStatement797 = frozenset([22, 53])
    FOLLOW_LT_in_expressionStatement799 = frozenset([22, 53])
    FOLLOW_53_in_expressionStatement803 = frozenset([1])
    FOLLOW_61_in_ifStatement815 = frozenset([22, 54])
    FOLLOW_LT_in_ifStatement817 = frozenset([22, 54])
    FOLLOW_54_in_ifStatement821 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_ifStatement823 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_expression_in_ifStatement827 = frozenset([22, 56])
    FOLLOW_LT_in_ifStatement829 = frozenset([22, 56])
    FOLLOW_56_in_ifStatement833 = frozenset([22, 23, 24, 25, 52, 54, 57, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_ifStatement835 = frozenset([22, 23, 24, 25, 52, 54, 57, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_statement_in_ifStatement840 = frozenset([1, 22, 62])
    FOLLOW_statementBlock_in_ifStatement844 = frozenset([1, 22, 62])
    FOLLOW_LT_in_ifStatement848 = frozenset([22, 62])
    FOLLOW_62_in_ifStatement852 = frozenset([22, 23, 24, 25, 52, 54, 57, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_ifStatement854 = frozenset([22, 23, 24, 25, 52, 54, 57, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_statement_in_ifStatement859 = frozenset([1])
    FOLLOW_statementBlock_in_ifStatement863 = frozenset([1])
    FOLLOW_doWhileStatement_in_iterationStatement877 = frozenset([1])
    FOLLOW_whileStatement_in_iterationStatement882 = frozenset([1])
    FOLLOW_forStatement_in_iterationStatement887 = frozenset([1])
    FOLLOW_forInStatement_in_iterationStatement892 = frozenset([1])
    FOLLOW_63_in_doWhileStatement903 = frozenset([22, 23, 24, 25, 52, 54, 57, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_doWhileStatement905 = frozenset([22, 23, 24, 25, 52, 54, 57, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_statement_in_doWhileStatement910 = frozenset([22, 64])
    FOLLOW_statementBlock_in_doWhileStatement914 = frozenset([22, 64])
    FOLLOW_LT_in_doWhileStatement917 = frozenset([22, 64])
    FOLLOW_64_in_doWhileStatement921 = frozenset([22, 54])
    FOLLOW_LT_in_doWhileStatement923 = frozenset([22, 54])
    FOLLOW_54_in_doWhileStatement927 = frozenset([23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_expression_in_doWhileStatement929 = frozenset([56])
    FOLLOW_56_in_doWhileStatement931 = frozenset([22, 53])
    FOLLOW_LT_in_doWhileStatement933 = frozenset([22, 53])
    FOLLOW_53_in_doWhileStatement937 = frozenset([1])
    FOLLOW_64_in_whileStatement949 = frozenset([22, 54])
    FOLLOW_LT_in_whileStatement951 = frozenset([22, 54])
    FOLLOW_54_in_whileStatement955 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_whileStatement957 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_expression_in_whileStatement961 = frozenset([22, 56])
    FOLLOW_LT_in_whileStatement963 = frozenset([22, 56])
    FOLLOW_56_in_whileStatement967 = frozenset([22, 23, 24, 25, 52, 54, 57, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_whileStatement969 = frozenset([22, 23, 24, 25, 52, 54, 57, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_statement_in_whileStatement974 = frozenset([1])
    FOLLOW_statementBlock_in_whileStatement978 = frozenset([1])
    FOLLOW_65_in_forStatement990 = frozenset([22, 54])
    FOLLOW_LT_in_forStatement992 = frozenset([22, 54])
    FOLLOW_54_in_forStatement996 = frozenset([22, 23, 24, 25, 52, 53, 54, 57, 59, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_forStatement999 = frozenset([22, 23, 24, 25, 52, 54, 57, 59, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_forStatementInitialiserPart_in_forStatement1003 = frozenset([22, 53])
    FOLLOW_LT_in_forStatement1007 = frozenset([22, 53])
    FOLLOW_53_in_forStatement1011 = frozenset([22, 23, 24, 25, 52, 53, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_forStatement1015 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_expression_in_forStatement1019 = frozenset([22, 53])
    FOLLOW_LT_in_forStatement1023 = frozenset([22, 53])
    FOLLOW_53_in_forStatement1027 = frozenset([22, 23, 24, 25, 52, 54, 56, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_forStatement1031 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_expression_in_forStatement1035 = frozenset([22, 56])
    FOLLOW_LT_in_forStatement1039 = frozenset([22, 56])
    FOLLOW_56_in_forStatement1043 = frozenset([22, 23, 24, 25, 52, 54, 57, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_forStatement1045 = frozenset([22, 23, 24, 25, 52, 54, 57, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_statement_in_forStatement1050 = frozenset([1])
    FOLLOW_statementBlock_in_forStatement1054 = frozenset([1])
    FOLLOW_expressionNoIn_in_forStatementInitialiserPart1066 = frozenset([1])
    FOLLOW_59_in_forStatementInitialiserPart1071 = frozenset([22, 23])
    FOLLOW_LT_in_forStatementInitialiserPart1073 = frozenset([22, 23])
    FOLLOW_variableDeclarationListNoIn_in_forStatementInitialiserPart1077 = frozenset([1])
    FOLLOW_65_in_forInStatement1088 = frozenset([22, 54])
    FOLLOW_LT_in_forInStatement1090 = frozenset([22, 54])
    FOLLOW_54_in_forInStatement1094 = frozenset([22, 23, 24, 25, 52, 54, 57, 59, 79, 80, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_forInStatement1096 = frozenset([22, 23, 24, 25, 52, 54, 57, 59, 79, 80, 115, 116, 117, 118, 119])
    FOLLOW_forInStatementInitialiserPart_in_forInStatement1100 = frozenset([22, 66])
    FOLLOW_LT_in_forInStatement1102 = frozenset([22, 66])
    FOLLOW_66_in_forInStatement1106 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_forInStatement1108 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_expression_in_forInStatement1112 = frozenset([22, 56])
    FOLLOW_LT_in_forInStatement1114 = frozenset([22, 56])
    FOLLOW_56_in_forInStatement1118 = frozenset([22, 23, 24, 25, 52, 54, 57, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_forInStatement1120 = frozenset([22, 23, 24, 25, 52, 54, 57, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_statement_in_forInStatement1125 = frozenset([1])
    FOLLOW_statementBlock_in_forInStatement1129 = frozenset([1])
    FOLLOW_leftHandSideExpression_in_forInStatementInitialiserPart1141 = frozenset([1])
    FOLLOW_59_in_forInStatementInitialiserPart1146 = frozenset([22, 23])
    FOLLOW_LT_in_forInStatementInitialiserPart1148 = frozenset([22, 23])
    FOLLOW_variableDeclarationNoIn_in_forInStatementInitialiserPart1152 = frozenset([1])
    FOLLOW_67_in_continueStatement1163 = frozenset([22, 23, 53])
    FOLLOW_Identifier_in_continueStatement1165 = frozenset([22, 53])
    FOLLOW_LT_in_continueStatement1168 = frozenset([22, 53])
    FOLLOW_53_in_continueStatement1172 = frozenset([1])
    FOLLOW_68_in_breakStatement1184 = frozenset([22, 23, 53])
    FOLLOW_Identifier_in_breakStatement1186 = frozenset([22, 53])
    FOLLOW_LT_in_breakStatement1189 = frozenset([22, 53])
    FOLLOW_53_in_breakStatement1193 = frozenset([1])
    FOLLOW_69_in_returnStatement1205 = frozenset([22, 23, 24, 25, 52, 53, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_expression_in_returnStatement1207 = frozenset([22, 53])
    FOLLOW_LT_in_returnStatement1210 = frozenset([22, 53])
    FOLLOW_53_in_returnStatement1214 = frozenset([1])
    FOLLOW_70_in_withStatement1226 = frozenset([22, 54])
    FOLLOW_LT_in_withStatement1228 = frozenset([22, 54])
    FOLLOW_54_in_withStatement1232 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_withStatement1234 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_expression_in_withStatement1238 = frozenset([22, 56])
    FOLLOW_LT_in_withStatement1240 = frozenset([22, 56])
    FOLLOW_56_in_withStatement1244 = frozenset([22, 23, 24, 25, 52, 54, 57, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_withStatement1246 = frozenset([22, 23, 24, 25, 52, 54, 57, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_statement_in_withStatement1251 = frozenset([1])
    FOLLOW_statementBlock_in_withStatement1255 = frozenset([1])
    FOLLOW_Identifier_in_labelledStatement1267 = frozenset([22, 71])
    FOLLOW_LT_in_labelledStatement1269 = frozenset([22, 71])
    FOLLOW_71_in_labelledStatement1273 = frozenset([22, 23, 24, 25, 52, 54, 57, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_labelledStatement1275 = frozenset([22, 23, 24, 25, 52, 54, 57, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_statement_in_labelledStatement1279 = frozenset([1])
    FOLLOW_72_in_switchStatement1290 = frozenset([22, 54])
    FOLLOW_LT_in_switchStatement1292 = frozenset([22, 54])
    FOLLOW_54_in_switchStatement1296 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_switchStatement1298 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_expression_in_switchStatement1302 = frozenset([22, 56])
    FOLLOW_LT_in_switchStatement1304 = frozenset([22, 56])
    FOLLOW_56_in_switchStatement1308 = frozenset([22, 57])
    FOLLOW_LT_in_switchStatement1310 = frozenset([22, 57])
    FOLLOW_caseBlock_in_switchStatement1314 = frozenset([1])
    FOLLOW_57_in_caseBlock1325 = frozenset([22, 58, 73, 74])
    FOLLOW_LT_in_caseBlock1328 = frozenset([22, 73])
    FOLLOW_caseClause_in_caseBlock1332 = frozenset([22, 58, 73, 74])
    FOLLOW_LT_in_caseBlock1337 = frozenset([22, 74])
    FOLLOW_defaultClause_in_caseBlock1341 = frozenset([22, 58, 73])
    FOLLOW_LT_in_caseBlock1344 = frozenset([22, 73])
    FOLLOW_caseClause_in_caseBlock1348 = frozenset([22, 58, 73])
    FOLLOW_LT_in_caseBlock1354 = frozenset([22, 58])
    FOLLOW_58_in_caseBlock1358 = frozenset([1])
    FOLLOW_73_in_caseClause1369 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_caseClause1371 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_expression_in_caseClause1375 = frozenset([22, 71])
    FOLLOW_LT_in_caseClause1377 = frozenset([22, 71])
    FOLLOW_71_in_caseClause1381 = frozenset([1, 22, 23, 24, 25, 52, 54, 57, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_caseClause1383 = frozenset([1, 22, 23, 24, 25, 52, 54, 57, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_statementList_in_caseClause1387 = frozenset([1])
    FOLLOW_74_in_defaultClause1399 = frozenset([22, 71])
    FOLLOW_LT_in_defaultClause1401 = frozenset([22, 71])
    FOLLOW_71_in_defaultClause1405 = frozenset([1, 22, 23, 24, 25, 52, 54, 57, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_defaultClause1407 = frozenset([1, 22, 23, 24, 25, 52, 54, 57, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_statementList_in_defaultClause1411 = frozenset([1])
    FOLLOW_75_in_throwStatement1423 = frozenset([23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_expression_in_throwStatement1425 = frozenset([22, 53])
    FOLLOW_LT_in_throwStatement1427 = frozenset([22, 53])
    FOLLOW_53_in_throwStatement1431 = frozenset([1])
    FOLLOW_76_in_tryStatement1443 = frozenset([22, 23, 24, 25, 52, 54, 57, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_tryStatement1445 = frozenset([22, 23, 24, 25, 52, 54, 57, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_statementBlock_in_tryStatement1449 = frozenset([22, 77, 78])
    FOLLOW_LT_in_tryStatement1451 = frozenset([22, 77, 78])
    FOLLOW_finallyClause_in_tryStatement1456 = frozenset([1])
    FOLLOW_catchClause_in_tryStatement1460 = frozenset([1, 22, 78])
    FOLLOW_LT_in_tryStatement1463 = frozenset([22, 78])
    FOLLOW_finallyClause_in_tryStatement1467 = frozenset([1])
    FOLLOW_77_in_catchClause1481 = frozenset([22, 54])
    FOLLOW_LT_in_catchClause1483 = frozenset([22, 54])
    FOLLOW_54_in_catchClause1487 = frozenset([22, 23])
    FOLLOW_LT_in_catchClause1489 = frozenset([22, 23])
    FOLLOW_Identifier_in_catchClause1493 = frozenset([22, 56])
    FOLLOW_LT_in_catchClause1495 = frozenset([22, 56])
    FOLLOW_56_in_catchClause1499 = frozenset([22, 23, 24, 25, 52, 54, 57, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_catchClause1501 = frozenset([22, 23, 24, 25, 52, 54, 57, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_statementBlock_in_catchClause1505 = frozenset([1])
    FOLLOW_78_in_finallyClause1516 = frozenset([22, 23, 24, 25, 52, 54, 57, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_finallyClause1518 = frozenset([22, 23, 24, 25, 52, 54, 57, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_statementBlock_in_finallyClause1522 = frozenset([1])
    FOLLOW_assignmentExpression_in_expression1534 = frozenset([1, 22, 55])
    FOLLOW_LT_in_expression1537 = frozenset([22, 55])
    FOLLOW_55_in_expression1541 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_expression1543 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_assignmentExpression_in_expression1547 = frozenset([1, 22, 55])
    FOLLOW_assignmentExpressionNoIn_in_expressionNoIn1560 = frozenset([1, 22, 55])
    FOLLOW_LT_in_expressionNoIn1563 = frozenset([22, 55])
    FOLLOW_55_in_expressionNoIn1567 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_expressionNoIn1569 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_assignmentExpressionNoIn_in_expressionNoIn1573 = frozenset([1, 22, 55])
    FOLLOW_callExpression_in_assignmentExpression1594 = frozenset([1])
    FOLLOW_leftHandSideExpression_in_assignmentExpression1612 = frozenset([22, 48, 71, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107])
    FOLLOW_LT_in_assignmentExpression1614 = frozenset([22, 48, 71, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107])
    FOLLOW_nonAssignmentOperator_in_assignmentExpression1617 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_assignmentExpression1619 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_assignmentExpression_in_assignmentExpression1622 = frozenset([1])
    FOLLOW_leftHandSideExpression_in_assignmentExpression1717 = frozenset([22, 60, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93])
    FOLLOW_LT_in_assignmentExpression1719 = frozenset([22, 60, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93])
    FOLLOW_assignmentOperator_in_assignmentExpression1722 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_assignmentExpression1724 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_assignmentExpression_in_assignmentExpression1727 = frozenset([1])
    FOLLOW_unaryExpression_in_assignmentExpression1821 = frozenset([1])
    FOLLOW_newExpression_in_assignmentExpression1829 = frozenset([1])
    FOLLOW_conditionalExpression_in_assignmentExpressionNoIn1852 = frozenset([1])
    FOLLOW_leftHandSideExpression_in_assignmentExpressionNoIn1857 = frozenset([22, 60, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93])
    FOLLOW_LT_in_assignmentExpressionNoIn1859 = frozenset([22, 60, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93])
    FOLLOW_assignmentOperator_in_assignmentExpressionNoIn1863 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_assignmentExpressionNoIn1865 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_assignmentExpressionNoIn_in_assignmentExpressionNoIn1869 = frozenset([1])
    FOLLOW_memberExpression_in_leftHandSideExpression1880 = frozenset([1])
    FOLLOW_memberExpression_in_newExpression1900 = frozenset([1])
    FOLLOW_79_in_newExpression1905 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_newExpression1907 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_newExpression_in_newExpression1911 = frozenset([1])
    FOLLOW_primaryExpression_in_memberExpression1923 = frozenset([1, 22, 80, 82])
    FOLLOW_functionExpression_in_memberExpression1927 = frozenset([1, 22, 80, 82])
    FOLLOW_79_in_memberExpression1931 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_memberExpression1933 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 115, 116, 117, 118, 119])
    FOLLOW_memberExpression_in_memberExpression1937 = frozenset([22, 54])
    FOLLOW_LT_in_memberExpression1939 = frozenset([22, 54])
    FOLLOW_arguments_in_memberExpression1943 = frozenset([1, 22, 80, 82])
    FOLLOW_LT_in_memberExpression1947 = frozenset([22, 80, 82])
    FOLLOW_memberExpressionSuffix_in_memberExpression1951 = frozenset([1, 22, 80, 82])
    FOLLOW_indexSuffix_in_memberExpressionSuffix1964 = frozenset([1])
    FOLLOW_propertyReferenceSuffix_in_memberExpressionSuffix1969 = frozenset([1])
    FOLLOW_memberExpression_in_callExpression1980 = frozenset([22, 54])
    FOLLOW_LT_in_callExpression1982 = frozenset([22, 54])
    FOLLOW_arguments_in_callExpression1985 = frozenset([1, 22, 54, 80, 82])
    FOLLOW_LT_in_callExpression1988 = frozenset([22, 54, 80, 82])
    FOLLOW_callExpressionSuffix_in_callExpression1991 = frozenset([1, 22, 54, 80, 82])
    FOLLOW_arguments_in_callExpressionSuffix2029 = frozenset([1])
    FOLLOW_indexSuffix_in_callExpressionSuffix2034 = frozenset([1])
    FOLLOW_propertyReferenceSuffix_in_callExpressionSuffix2039 = frozenset([1])
    FOLLOW_54_in_arguments2050 = frozenset([22, 23, 24, 25, 52, 54, 56, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_arguments2053 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_assignmentExpression_in_arguments2056 = frozenset([22, 55, 56])
    FOLLOW_LT_in_arguments2059 = frozenset([22, 55])
    FOLLOW_55_in_arguments2062 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_arguments2064 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_assignmentExpression_in_arguments2067 = frozenset([22, 55, 56])
    FOLLOW_LT_in_arguments2074 = frozenset([22, 56])
    FOLLOW_56_in_arguments2077 = frozenset([1])
    FOLLOW_80_in_indexSuffix2106 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_indexSuffix2108 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_expression_in_indexSuffix2111 = frozenset([22, 81])
    FOLLOW_LT_in_indexSuffix2113 = frozenset([22, 81])
    FOLLOW_81_in_indexSuffix2116 = frozenset([1])
    FOLLOW_82_in_propertyReferenceSuffix2136 = frozenset([22, 23])
    FOLLOW_LT_in_propertyReferenceSuffix2138 = frozenset([22, 23])
    FOLLOW_Identifier_in_propertyReferenceSuffix2141 = frozenset([1])
    FOLLOW_set_in_assignmentOperator0 = frozenset([1])
    FOLLOW_operatorExpression_in_conditionalExpression2216 = frozenset([1, 22, 94])
    FOLLOW_LT_in_conditionalExpression2219 = frozenset([22, 94])
    FOLLOW_94_in_conditionalExpression2223 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_conditionalExpression2225 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_operatorExpression_in_conditionalExpression2229 = frozenset([22, 71])
    FOLLOW_LT_in_conditionalExpression2231 = frozenset([22, 71])
    FOLLOW_71_in_conditionalExpression2235 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_conditionalExpression2237 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_operatorExpression_in_conditionalExpression2241 = frozenset([1])
    FOLLOW_leftHandSideExpression_in_operatorExpression2258 = frozenset([22, 48, 71, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107])
    FOLLOW_LT_in_operatorExpression2260 = frozenset([22, 48, 71, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107])
    FOLLOW_nonAssignmentOperator_in_operatorExpression2263 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_operatorExpression2265 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_assignmentExpression_in_operatorExpression2268 = frozenset([1])
    FOLLOW_unaryExpression_in_operatorExpression2362 = frozenset([1])
    FOLLOW_set_in_nonAssignmentOperator0 = frozenset([1])
    FOLLOW_postfixExpression_in_unaryExpression2454 = frozenset([1])
    FOLLOW_set_in_unaryExpression2459 = frozenset([23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_unaryExpression_in_unaryExpression2495 = frozenset([1])
    FOLLOW_leftHandSideExpression_in_postfixExpression2506 = frozenset([1, 111, 112])
    FOLLOW_set_in_postfixExpression2508 = frozenset([1])
    FOLLOW_115_in_primaryExpression2526 = frozenset([1])
    FOLLOW_Identifier_in_primaryExpression2531 = frozenset([1])
    FOLLOW_literal_in_primaryExpression2536 = frozenset([1])
    FOLLOW_arrayLiteral_in_primaryExpression2541 = frozenset([1])
    FOLLOW_objectLiteral_in_primaryExpression2546 = frozenset([1])
    FOLLOW_54_in_primaryExpression2551 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_primaryExpression2553 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_expression_in_primaryExpression2557 = frozenset([22, 56])
    FOLLOW_LT_in_primaryExpression2559 = frozenset([22, 56])
    FOLLOW_56_in_primaryExpression2563 = frozenset([1])
    FOLLOW_80_in_arrayLiteral2575 = frozenset([22, 23, 24, 25, 52, 54, 55, 57, 79, 80, 81, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_arrayLiteral2577 = frozenset([22, 23, 24, 25, 52, 54, 55, 57, 79, 80, 81, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_assignmentExpression_in_arrayLiteral2580 = frozenset([22, 55, 81])
    FOLLOW_LT_in_arrayLiteral2584 = frozenset([22, 55])
    FOLLOW_55_in_arrayLiteral2587 = frozenset([22, 23, 24, 25, 52, 54, 55, 57, 79, 80, 81, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_arrayLiteral2590 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_assignmentExpression_in_arrayLiteral2593 = frozenset([22, 55, 81])
    FOLLOW_LT_in_arrayLiteral2599 = frozenset([22, 81])
    FOLLOW_81_in_arrayLiteral2602 = frozenset([1])
    FOLLOW_57_in_objectLiteral2632 = frozenset([22, 23, 24, 25, 58])
    FOLLOW_LT_in_objectLiteral2634 = frozenset([22, 23, 24, 25, 58])
    FOLLOW_propertyNameAndValue_in_objectLiteral2638 = frozenset([22, 55, 58])
    FOLLOW_LT_in_objectLiteral2641 = frozenset([22, 55])
    FOLLOW_55_in_objectLiteral2644 = frozenset([22, 23, 24, 25])
    FOLLOW_LT_in_objectLiteral2646 = frozenset([22, 23, 24, 25])
    FOLLOW_propertyNameAndValue_in_objectLiteral2649 = frozenset([22, 55, 58])
    FOLLOW_LT_in_objectLiteral2655 = frozenset([22, 58])
    FOLLOW_58_in_objectLiteral2658 = frozenset([1])
    FOLLOW_propertyName_in_propertyNameAndValue2687 = frozenset([22, 71])
    FOLLOW_LT_in_propertyNameAndValue2689 = frozenset([22, 71])
    FOLLOW_71_in_propertyNameAndValue2692 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_propertyNameAndValue2694 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_assignmentExpression_in_propertyNameAndValue2697 = frozenset([1])
    FOLLOW_set_in_propertyName0 = frozenset([1])
    FOLLOW_116_in_literal2749 = frozenset([1])
    FOLLOW_117_in_literal2754 = frozenset([1])
    FOLLOW_118_in_literal2759 = frozenset([1])
    FOLLOW_StringLiteral_in_literal2764 = frozenset([1])
    FOLLOW_NumericLiteral_in_literal2769 = frozenset([1])
    FOLLOW_regexpLiteral_in_literal2777 = frozenset([1])
    FOLLOW_119_in_regexpLiteral2790 = frozenset([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118])
    FOLLOW_set_in_regexpLiteral2792 = frozenset([119])
    FOLLOW_119_in_regexpLiteral2795 = frozenset([1])
    FOLLOW_functionDeclaration_in_synpred5_JavaScript229 = frozenset([1])
    FOLLOW_LT_in_synpred10_JavaScript301 = frozenset([1])
    FOLLOW_LT_in_synpred20_JavaScript402 = frozenset([1])
    FOLLOW_expressionStatement_in_synpred25_JavaScript481 = frozenset([1])
    FOLLOW_labelledStatement_in_synpred32_JavaScript521 = frozenset([1])
    FOLLOW_LT_in_synpred35_JavaScript549 = frozenset([1])
    FOLLOW_LT_in_synpred50_JavaScript693 = frozenset([1])
    FOLLOW_LT_in_synpred51_JavaScript716 = frozenset([1])
    FOLLOW_statement_in_synpred60_JavaScript840 = frozenset([1])
    FOLLOW_statement_in_synpred63_JavaScript859 = frozenset([1])
    FOLLOW_LT_in_synpred64_JavaScript848 = frozenset([22, 62])
    FOLLOW_62_in_synpred64_JavaScript852 = frozenset([22, 23, 24, 25, 52, 54, 57, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_synpred64_JavaScript854 = frozenset([22, 23, 24, 25, 52, 54, 57, 59, 61, 63, 64, 65, 67, 68, 69, 70, 72, 75, 76, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_statement_in_synpred64_JavaScript859 = frozenset([1])
    FOLLOW_statementBlock_in_synpred64_JavaScript863 = frozenset([1])
    FOLLOW_forStatement_in_synpred67_JavaScript887 = frozenset([1])
    FOLLOW_statement_in_synpred69_JavaScript910 = frozenset([1])
    FOLLOW_statement_in_synpred77_JavaScript974 = frozenset([1])
    FOLLOW_statement_in_synpred89_JavaScript1050 = frozenset([1])
    FOLLOW_statement_in_synpred98_JavaScript1125 = frozenset([1])
    FOLLOW_statement_in_synpred111_JavaScript1251 = frozenset([1])
    FOLLOW_LT_in_synpred127_JavaScript1383 = frozenset([1])
    FOLLOW_LT_in_synpred130_JavaScript1407 = frozenset([1])
    FOLLOW_callExpression_in_synpred149_JavaScript1594 = frozenset([1])
    FOLLOW_leftHandSideExpression_in_synpred152_JavaScript1612 = frozenset([22, 48, 71, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107])
    FOLLOW_LT_in_synpred152_JavaScript1614 = frozenset([22, 48, 71, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107])
    FOLLOW_nonAssignmentOperator_in_synpred152_JavaScript1617 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_synpred152_JavaScript1619 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_assignmentExpression_in_synpred152_JavaScript1622 = frozenset([1])
    FOLLOW_leftHandSideExpression_in_synpred155_JavaScript1717 = frozenset([22, 60, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93])
    FOLLOW_LT_in_synpred155_JavaScript1719 = frozenset([22, 60, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93])
    FOLLOW_assignmentOperator_in_synpred155_JavaScript1722 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_synpred155_JavaScript1724 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_assignmentExpression_in_synpred155_JavaScript1727 = frozenset([1])
    FOLLOW_unaryExpression_in_synpred156_JavaScript1821 = frozenset([1])
    FOLLOW_conditionalExpression_in_synpred157_JavaScript1852 = frozenset([1])
    FOLLOW_memberExpression_in_synpred160_JavaScript1900 = frozenset([1])
    FOLLOW_leftHandSideExpression_in_synpred201_JavaScript2258 = frozenset([22, 48, 71, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107])
    FOLLOW_LT_in_synpred201_JavaScript2260 = frozenset([22, 48, 71, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107])
    FOLLOW_nonAssignmentOperator_in_synpred201_JavaScript2263 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_LT_in_synpred201_JavaScript2265 = frozenset([22, 23, 24, 25, 52, 54, 57, 79, 80, 96, 97, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])
    FOLLOW_assignmentExpression_in_synpred201_JavaScript2268 = frozenset([1])
    FOLLOW_LT_in_synpred235_JavaScript2577 = frozenset([1])
    FOLLOW_LT_in_synpred242_JavaScript2634 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("JavaScriptLexer", JavaScriptParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)

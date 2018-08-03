import re
import itertools


def readpuz(filename):
    '''
    Extract Sirs and Claims from file
    '''
    # read paragraph from file
    puz = open(filename, 'r').read()

    # regex op to swap quotation and the punctuation before it if any
    puz = re.sub(r'([,\.!?])"', r'"\1', puz)

    # regex pattern to split paragraph
    pat_sen_sep = re.compile('''([.!?])(?=(?:[^'"]|'[^']*'|"[^"]*")*$)''')

    # Extract all sentences from paragraph
    sentences = [s.strip() for s in pat_sen_sep.split(puz)]
    sentences = [' '.join(s.split()) for s in sentences if s]

    # regex patterns to extract Sirs
    pat_sir = re.compile(r'(?<=Sir) ([A-Z][a-z]+)')
    pat_sirs = re.compile(r'(?<=Sirs )([A-Za-z, ]*? and [A-Z][a-z]+)')
    pat_sirs_sep = re.compile(r', | and ')

    # Extract all Sirs from all sentences
    Sirs = set()
    for s in sentences:
        m = pat_sir.findall(s)
        if m:
            Sirs.update(m)
        m = pat_sirs.findall(s)
        if m:
            Sirs.update(sum((pat_sirs_sep.split(i) for i in m), []))

    # regex patterns to extract claims
    pat_quo = re.compile(r'"([^\"]*)"')

    # Extract all Claims from all sentences
    Claims = {}
    for s in sentences:
        m = pat_quo.search(s)
        if m:
            claim = m.groups()[0]
            s = pat_quo.sub('', s)
            for sir in Sirs:
                if s.find(sir) > -1:
                    if sir not in Claims:
                        Claims[sir] = []
                    Claims[sir].append(claim)
                    break

    return sorted(list(Sirs)), Claims


def evaluable_claim(Sirs, sir, claim):
    '''
    Construct the evaluable claim based on the input
    '''

    # --- I am a Knight/Knave --- #
    # I am a Knight
    if claim == 'I am a Knight':
        return sir + ' is (' + sir + ' is True' + ')'
    # I am a Knave
    elif claim == 'I am a Knave':
        return sir + ' is (' + sir + ' is False' + ')'

    # --- Sir Sir_Name is a Knight/Knave --- #
    # --- Disjunction_of_Sirs is a Knight/Knave --- #
    # --- Conjunction_of_Sirs are Knights/Knaves --- #
    elif claim.startswith('Sir'):
        # --- Sir Sir_Name is a Knight/Knave --- #
        # --- Disjunction_of_Sirs is a Knight/Knave --- #
        if claim.find(' is ') > -1:
            # Sir Sir_Name is a Knight
            # Disjunction_of_Sirs is a Knight
            if claim.endswith('Knight'):
                return sir + ' is (' + \
                    claim.replace('Sir ', '').replace('I', sir).replace(
                        'or', 'is True or').replace(',', ' is True or').replace('is a Knight', 'is True)')
            # Sir Sir_Name is a Knave
            # Disjunction_of_Sirs is a Knave
            else:
                return sir + ' is (' + \
                    claim.replace('Sir ', '').replace('I', sir).replace(
                        'or', 'is False or').replace(',', ' is False or').replace('is a Knave', 'is False)')
        # --- Conjunction_of_Sirs are Knights/Knaves --- #
        else:
            # Conjunction_of_Sirs are Knights
            if claim.endswith('Knights'):
                return sir + ' is (' + \
                    claim.replace('Sir ', '').replace('I', sir).replace(
                        'and', 'is True and').replace(',', ' is True and').replace('are Knights', 'is True)')
            # Conjunction_of_Sirs are Knaves
            else:
                return sir + ' is (' + \
                    claim.replace('Sir ', '').replace('I', sir).replace(
                        'and', 'is False and').replace(',', ' is False and').replace('are Knaves', 'is False)')

    # --- All/all of us are Knights/Knaves --- #
    # --- At/at least one of Conjunction_of_Sirs/us is a Knight/Knave --- #
    # --- At/at most one of Conjunction_of_Sirs/us is a Knight/Knave --- #
    # --- Exactly/exactly one of Conjunction_of_Sirs/us is a Knight/Knave --- #
    else:
        claim = claim[0].lower() + claim[1:]
        # --- All/all of us are Knights/Knaves --- #
        if claim.startswith('all'):
            # All/all of us are Knights
            if claim.endswith('Knights'):
                return sir + ' is (' + \
                    claim.replace('all of us', ' and '.join([sir + ' is True' for sir in Sirs]) + ')').replace(
                        ' are Knights', '')
            # All/all of us are Knaves
            else:
                return sir + ' is (' + \
                    claim.replace('all of us', ' and '.join([sir + ' is False' for sir in Sirs]) + ')').replace(
                        ' are Knaves', '')

        # --- At/at least one of Conjunction_of_Sirs/us is a Knight/Knave --- #
        elif claim.startswith('at least'):
            # At/at least one of Conjunction_of_Sirs/us is a Knight
            if claim.endswith('Knight'):
                # At/at least one of us is a Knight
                if claim.find(' us ') > -1:
                    return sir + ' is not (' + \
                        claim.replace('at least one of us', ' and '.join([sir + ' is False' for sir in Sirs]) + ')').replace(
                            ' is a Knight', '')
                # At/at least one of Conjunction_of_Sirs is a Knight
                else:
                    return sir + ' is not (' + \
                        claim.replace('Sir ', '').replace('at least one of ', '').replace('I', sir).replace(
                            'and', 'is False and').replace(',', ' is False and').replace('is a Knight', 'is False)')
            # At/at least one of Conjunction_of_Sirs/us is a Knave
            else:
                # At/at least one of us is a Knave
                if claim.find(' us ') > -1:
                    return sir + ' is not (' + \
                        claim.replace('at least one of us', ' and '.join([sir + ' is True' for sir in Sirs]) + ')').replace(
                            'is a Knave', '')
                # At/at least one of Conjunction_of_Sirs is a Knave
                else:
                    return sir + ' is not (' + \
                        claim.replace('Sir ', '').replace('at least one of ', '').replace('I', sir).replace(
                            'and', 'is True and').replace(',', ' is True and').replace('is a Knave', 'is True)')

        # --- At/at most one of Conjunction_of_Sirs/us is a Knight/Knave --- #
        elif claim.startswith('at most'):
            # At/at most one of us is a Knight/Knave
            if claim.find(' us ') > -1:
                # At/at most one of us is a Knight
                if claim.endswith('Knight'):
                    return sir + ' is (' + \
                        ' or '.join(['(' + ' and '.join([sir_ + ' is True' if sir == sir_ else sir_ +
                                                         ' is False' for sir_ in Sirs]) + ')' for sir in Sirs]) + \
                        ' or ' + '(' + ' and '.join([sir_ +
                                                     ' is False' for sir_ in Sirs]) + ')' + ')'
                # At/at most one of us is a Knave
                else:
                    return sir + ' is (' + \
                        ' or '.join(['(' + ' and '.join([sir_ + ' is False' if sir == sir_ else sir_ +
                                                         ' is True' for sir_ in Sirs]) + ')' for sir in Sirs]) + \
                        ' or ' + '(' + ' and '.join([sir_ +
                                                     ' is True' for sir_ in Sirs]) + ')' + ')'
            # At/at most one of Conjunction_of_Sirs is a Knight/Knave
            else:
                sirs = []
                if claim.find(' I ') > -1:
                    sirs.append(sir)
                for sir_ in Sirs:
                    if claim.find(sir_) > -1:
                        sirs.append(sir_)
                # At/at most one of Conjunction_of_Sirs is a Knight
                if claim.endswith('Knight'):
                    return sir + ' is (' + \
                        ' or '.join(['(' + ' and '.join([sir_ + ' is True' if sir == sir_ else sir_ +
                                                         ' is False' for sir_ in sirs]) + ')' for sir in sirs]) + \
                        ' or ' + '(' + ' and '.join([sir_ +
                                                     ' is False' for sir_ in sirs]) + ')' + ')'
                # At/at most one of Conjunction_of_Sirs is a Knave
                else:
                    return sir + ' is (' + \
                        ' or '.join(['(' + ' and '.join([sir_ + ' is False' if sir == sir_ else sir_ +
                                                         ' is True' for sir_ in sirs]) + ')' for sir in sirs]) + \
                        ' or ' + '(' + ' and '.join([sir_ +
                                                     ' is True' for sir_ in sirs]) + ')' + ')'

        # --- Exactly/exactly one of Conjunction_of_Sirs/us is a Knight/Knave --- #
        else:
            # Exactly/exactly one of us is a Knight/Knave
            if claim.find(' us ') > -1:
                # Exactly/exactly one of us is a Knight
                if claim.endswith('Knight'):
                    return sir + ' is (' + \
                        ' or '.join(['(' + ' and '.join([sir_ + ' is True' if sir == sir_ else sir_ +
                                                         ' is False' for sir_ in Sirs]) + ')' for sir in Sirs]) + ')'
                # Exactly/exactly one of us is a Knave
                else:
                    return sir + ' is (' + \
                        ' or '.join(['(' + ' and '.join([sir_ + ' is False' if sir == sir_ else sir_ +
                                                         ' is True' for sir_ in Sirs]) + ')' for sir in Sirs]) + ')'
            # Exactly/exactly one of Conjunction_of_Sirs is a Knight/Knave
            else:
                sirs = []
                if claim.find(' I ') > -1:
                    sirs.append(sir)
                for sir_ in Sirs:
                    if claim.find(sir_) > -1:
                        sirs.append(sir_)
                # Exactly/exactly one of Conjunction_of_Sirs is a Knight
                if claim.endswith('Knight'):
                    return sir + ' is (' + \
                        ' or '.join(['(' + ' and '.join([sir_ + ' is True' if sir == sir_ else sir_ +
                                                         ' is False' for sir_ in sirs]) + ')' for sir in sirs]) + ')'
                # Exactly/exactly one of Conjunction_of_Sirs is a Knave
                else:
                    return sir + ' is (' + \
                        ' or '.join(['(' + ' and '.join([sir_ + ' is False' if sir == sir_ else sir_ +
                                                         ' is True' for sir_ in sirs]) + ')' for sir in sirs]) + ')'


def solve(Sirs, Claims):
    '''
    Solve puzzle to get solution(s) if any
    '''

    claims = []

    for sir in Sirs:
        if sir in Claims:
            for claim in Claims[sir]:
                claims.append(evaluable_claim(Sirs, sir, claim))

    # get all possible solutions
    possibleSols = list(map(list, itertools.product(
        [False, True], repeat=len(Sirs))))

    Sols = []

    local_dct = {}
    for sol in possibleSols:  # [brute-force] iterate all possible solutions
        # put possible solution in a local dict so as to be used by eval
        for i, sir in enumerate(Sirs):
            local_dct[sir] = sol[i]
        # eval all evaluable claims
        # if all of them are harmonious logically then the solution is valid
        if all(eval(c, None, local_dct) for c in claims if c):
            Sols.append([local_dct[sir] for sir in Sirs])

    return Sols


def main():
    '''
    Main entry
    '''
    filename = input('Which text file do you want to use for the puzzle? ')

    Sirs, Claims = readpuz(filename)

    print('The Sirs are: ' + ' '.join(Sirs) + ' ')

    Sols = solve(Sirs, Claims)

    if not Sols:
        print('There is no solution.')
    elif len(Sols) == 1:
        print('There is a unique solution:')
        sol = Sols[0]
        for i, sir in enumerate(Sirs):
            if sol[i]:
                print('Sir {} is a Knight.'.format(sir))
            else:
                print('Sir {} is a Knave.'.format(sir))

    else:
        print('There are {} solutions.'.format(len(Sols)))


if __name__ == '__main__':
    main()

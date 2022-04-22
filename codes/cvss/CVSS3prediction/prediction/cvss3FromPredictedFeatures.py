import math

predictedFeatureFile = open('predictedParameters.csv', 'rb')

ActualPredMat = []
deviation = [[],[]]

attack_vector = {"ND": 0.85, "N": 0.85, "A": 0.62, "L": 0.55, "P": 0.20}
attack_complexity = {"ND": 0.77, "L": 0.77, "H": 0.44}
privileges_required = {"ND": 0.85, "N": 0.85, "L": 0.62, "H": 0.27}
user_interaction = {"ND": 0.85, "N": 0.85, "R": 0.62}
cia_impact = {"ND": 0.56, "H": 0.56, "L": 0.22, "N": 0}

def calculate_score(attack_vector_value, attack_complexity_value, privileges_required_value, user_interaction_value, confidentiality_value, integrity_value, availability_value, scope_value):
    # print(attack_vector_value, attack_complexity_value, privileges_required_value, user_interaction_value, confidentiality_value, integrity_value, availability_value, scope_value)
    # exit()

    exploitability_sub_score_value = 8.22 * attack_vector_value * attack_complexity_value * privileges_required_value * user_interaction_value
    # print(exploitability_sub_score_value)

    impact_sub_score_value = 1 - ((1 - confidentiality_value) * (1 - integrity_value) * (1 - availability_value))
    # print(impact_sub_score_value)

    if scope_value == "U":
        impact_value = 6.42 * impact_sub_score_value
        cvss_base_value = min(10, impact_value + exploitability_sub_score_value)
        # print(impact_value, cvss_base_value)
    elif scope_value == "C":
        impact_value = 7.52 * (impact_sub_score_value - 0.029) - 3.25 * math.pow(impact_sub_score_value - 0.02, 15)
        cvss_base_value = min(10, 1.08 * (impact_value + exploitability_sub_score_value))

    if impact_sub_score_value <= 0:
        cvss_base_value = float(0.0)
    else:
        cvss_base_value = math.ceil(cvss_base_value * 10) / 10

    # print(cvss_base_value)
    # exit()
    return cvss_base_value

for line in predictedFeatureFile:
    line = line.decode().replace('\n', '').strip()
    # print(line)

    tkn = line.rsplit(';')
    actualVals, predictedVals = [], []
    for i in range(2,len(tkn)):
        if i%2 == 0:
            predictedVals.append(tkn[i])
        else:
            actualVals.append(tkn[i])

    # print(tkn[2:])
    # print(actualVals)

    exploit_val_actual, exploit_val_pred = actualVals[0], predictedVals[0]
    impact_val_actual, impact_val_pred = actualVals[1], predictedVals[1]
    av_actual, av_pred = actualVals[2], predictedVals[2]
    ac_actual, ac_pred = actualVals[3], predictedVals[3]
    pr_actual, pr_pred = actualVals[4], predictedVals[4]
    ui_actual, ui_pred = actualVals[5], predictedVals[5]
    scope_actual, scope_pred = actualVals[6], predictedVals[6]
    conf_actual, conf_pred = actualVals[7], predictedVals[7]
    integ_actual, integ_pred = actualVals[8], predictedVals[8]
    avail_actual, avail_pred = actualVals[9], predictedVals[9]

    attack_vector_value, attack_complexity_value, privileges_required_value, user_interaction_value, confidentiality_value, integrity_value, availability_value = attack_vector[av_actual], attack_complexity[ac_actual], privileges_required[pr_actual], user_interaction[ui_actual], cia_impact[conf_actual], cia_impact[integ_actual], cia_impact[avail_actual]
    actualScore = calculate_score(attack_vector_value, attack_complexity_value, privileges_required_value, user_interaction_value, confidentiality_value, integrity_value, availability_value, scope_actual)

    attack_vector_value, attack_complexity_value, privileges_required_value, user_interaction_value, confidentiality_value, integrity_value, availability_value = attack_vector[av_actual], attack_complexity[ac_actual], privileges_required[pr_actual], user_interaction[ui_actual], cia_impact[conf_actual], cia_impact[integ_actual], cia_impact[avail_actual]
    predScore = calculate_score(attack_vector_value, attack_complexity_value, privileges_required_value, user_interaction_value, confidentiality_value, integrity_value, availability_value, scope_pred)

    scoresToList = []
    print("Actual || Pred: ", actualScore, predScore, actualScore-predScore)

    deviation[0].append(abs(actualScore-predScore))
    deviation[1].append(abs(actualScore-predScore)/float(actualScore))

    scoresToList.append(actualScore)
    scoresToList.append(predScore)
    ActualPredMat.append(scoresToList)

print(ActualPredMat)
print(deviation[0])
print(deviation[1])
print(sum(deviation[0])/float(len(ActualPredMat)))
print(sum(deviation[1])/float(len(ActualPredMat)))


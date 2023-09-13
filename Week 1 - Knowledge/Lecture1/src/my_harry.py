import logic

rain = logic.Symbol("rain")  # means it is raining
hagrid = logic.Symbol("hagrid")  # Harry visited Hagrid
dum = logic.Symbol("dumbledore")  # Harry visited Dumbledore

sentence = logic.And(rain, hagrid)

print(sentence.formula())

knowledge = logic.And(
    logic.Implication(logic.Not(rain), hagrid),
    logic.Or(hagrid, dum),
    logic.Not(logic.And(hagrid, dum)),
    dum
)

print(knowledge.formula())

print(logic.model_check(knowledge, rain))

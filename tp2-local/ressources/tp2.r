data = read.csv("Tp2.csv", sep="\t", header=FALSE, dec=".")
#data$V2 = 2^data$V2

taille=data$V1
glouton = data$V2
cout_glouton = data$V3
dynamique = data$V4
cout_dynamique = data$V5
recherche_locale = data$V6
Cout_recherche_locale = data$V7

regglouton = lm(log(glouton*1000)~log(taille))
regdynamique = lm(log(dynamique)~log(taille))
regrecherche_locale = lm(log(recherche_locale)~log(taille))

#Test de puissance

plot(log(glouton)~log(taille), main="test de puissance pour glouton")
abline(regglouton, untf=F)

plot(log(dynamique)~log(taille), main="test de puissance pour dynamique")
abline(regdynamique, untf=F)
plot(log(recherche_locale)~log(taille), main="test de puissance pour recherche_locale")
abline(regrecherche_locale, untf=F)
plot( exp(regglouton$coefficients[1] + regglouton$coefficients[2] * seq(0, 20, 0.1)))
points(seq(0, 20, 0.1), exp(regdynamique$coefficients[1] + regdynamique$coefficients[2] * seq(0, 20, 0.1)))
- (regglouton$coefficients[1] - regdynamique$coefficients[1]) / (regglouton$coefficients[2] - regdynamique$coefficients[2])



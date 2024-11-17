from requete_mistral import *
from docx import Document
out_put_path="C:/Users/Utilisateur/Downloads/lettre_jurydique.docx"


def save_letter_to_word(letter_text, output_path):
    document = Document()
    document.add_paragraph(letter_text)
    document.save(output_path)
    print('fichier bien enregistré')


if __name__ == '__main__':

    liste_texte_loi=["""   Art. 1er  (Ord. no 2019-1101 du 30 oct. 2019, art. 2, en vigueur le 1er juin 2020)  «I. — La présente loi régit tout immeuble bâti ou groupe d'immeubles bâtis à usage total ou partiel d'habitation dont la propriété est répartie par lots entre plusieurs personnes.»
  (L. no 2018-1021 du 23 nov. 2018, art. 206)  «Le lot de copropriété comporte obligatoirement une partie privative et une quote-part de parties communes, lesquelles sont indissociables.
 «Ce lot peut être un lot transitoire. Il est alors formé d'une partie privative constituée d'un droit de construire précisément défini quant aux constructions qu'il permet de réaliser et d'une quote-part de parties communes correspondante.
 «La création et la consistance du lot transitoire sont stipulées dans le règlement de copropriété.»
  (Ord. no 2019-1101 du 30 oct. 2019, art. 2, en vigueur le 1er juin 2020)  «II. — A défaut de convention y dérogeant expressément et mettant en place une organisation dotée de la personnalité morale et suffisamment structurée pour assurer la gestion de leurs éléments et services communs, la présente loi est également applicable:
 «1o A tout immeuble ou groupe d'immeubles bâtis à destination totale autre que d'habitation dont la propriété est répartie par lots entre plusieurs personnes;
 «2o A tout ensemble immobilier qui, outre des terrains, des volumes, des aménagements et des services communs, comporte des parcelles ou des volumes, bâtis ou non, faisant l'objet de droits de propriété privatifs.
 «Pour les immeubles, groupes d'immeubles et ensembles immobiliers mentionnés aux deux alinéas ci-dessus et déjà régis par la présente loi, la convention mentionnée au premier alinéa du présent II est adoptée par l'assemblée générale à l'unanimité des voix de tous les copropriétaires composant le syndicat.»
""", """Art. 14-2-1  (L. no 2021-1104 du 22 août 2021, art. 171-I-3o)  I. — Dans les immeubles à destination totale ou partielle d'habitation, le syndicat des copropriétaires constitue un fonds de travaux au terme d'une période de dix ans à compter de la date de la réception des travaux de construction de l'immeuble, pour faire face aux dépenses résultant:
 1o De l'élaboration du projet de plan pluriannuel de travaux mentionné à l'article 14-2 et, le cas échéant, du diagnostic technique global mentionné à l'article L. 731-1  du code de la construction et de l'habitation;
 2o De la réalisation des travaux prévus dans le plan pluriannuel de travaux adopté par l'assemblée générale des copropriétaires;
 3o Des travaux décidés par le syndic en cas d'urgence, dans les conditions prévues au troisième alinéa du I de l'article 18 de la présente loi;
 4o Des travaux nécessaires à la sauvegarde de l'immeuble, à la préservation de la santé et de la sécurité des occupants et à la réalisation d'économies d'énergie, non prévus dans le plan pluriannuel de travaux.
 Ce fonds de travaux est alimenté par une cotisation annuelle obligatoire. Chaque copropriétaire contribue au fonds selon les mêmes modalités que celles décidées par l'assemblée générale pour le versement des provisions du budget prévisionnel.
 L'assemblée générale peut, par un vote à la même majorité que celle applicable aux dépenses concernées, affecter tout ou partie des sommes déposées sur le fonds de travaux au financement des dépenses mentionnées aux 1o à 4o du présent I. Cette affectation doit tenir compte de l'existence de parties communes spéciales ou de clefs de répartition des charges.
 Lorsque l'assemblée générale a adopté le plan pluriannuel de travaux mentionné à l'article 14-2, le montant de la cotisation annuelle ne peut être inférieur à 2,5 % du montant des travaux prévus dans le plan adopté et à 5 % du budget prévisionnel mentionné à l'article 14-1. A défaut d'adoption d'un plan, le montant de la cotisation annuelle ne peut être inférieur à 5 % du budget prévisionnel mentionné au même article 14-1.
 L'assemblée générale, votant à la majorité des voix de tous les copropriétaires, peut décider d'un montant supérieur.
 II. — L'assemblée générale se prononce sur la question de la suspension des cotisations au fonds de travaux lorsque son montant excède le montant du budget prévisionnel mentionné à l'article 14-1. Lorsqu'un plan pluriannuel de travaux a été adopté par l'assemblée générale, celle-ci se prononce sur cette suspension lorsque le montant du fonds de travaux excède, en outre, 50 % du montant des travaux prévus dans le plan adopté.
 III. — Les sommes versées au titre du fonds de travaux sont attachées aux lots et entrent définitivement, dès leur versement, dans le patrimoine du syndicat des copropriétaires. Elles ne donnent pas lieu à un remboursement par le syndicat des copropriétaires à l'occasion de la cession d'un lot. L'acquéreur peut consentir à verser au vendeur un montant équivalent à ces sommes en sus du prix de vente du lot. 
"""]

    pb=" Mon propriétaire indique dans mon contrat de location que le salon fait partie de la partie privée de ma colocataire et qu'il n'y a pas de partie commune"

    texte =make_final_prompt(liste_texte_loi, pb)

    reponse=appel_mistral(texte)

    save_letter_to_word(reponse, out_put_path)
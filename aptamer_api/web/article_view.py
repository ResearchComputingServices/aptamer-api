from flask import request, send_file
from flask import json, jsonify, Response, blueprints
from aptamer_api.models.role import Role, RoleSchema
from aptamer_api.models.article import Article, ArticleSchema
from aptamer_api.extensions import db, ma
from aptamer_api.web.common_view import aptamer_bp
from aptamer_api.decorators.crossorigin import crossdomain
from aptamer_api.decorators.authentication import authentication
from aptamer_api.providers.article_provider import ArticleProvider
from aptamer_api.providers.user_provider import UserProvider
import pandas as pd
import math
from io import BytesIO

article_schema = ArticleSchema(many=False)
article_schema_many = ArticleSchema(many=True)

provider = ArticleProvider()
user_provider = UserProvider()

@aptamer_bp.route("/articles/count", methods=['GET'])
@crossdomain(origin='*')
@authentication
def get_article_count():
    return provider.get_count(Article)


@aptamer_bp.route("/articles", methods=['GET'])
@crossdomain(origin='*')
@authentication
def get_article():
    try:
        id = request.args.get('id')

        #name = request.args.get('name')

        pubmedid = request.args.get('pubmedid')
        doinumber= request.args.get('doinumber')
        yearofpublication= request.args.get('yearofpublication')
        aptamertargettype= request.args.get('aptamertargettype')
        aptamertargetname= request.args.get('aptamertargetname')
        aptamersequence= request.args.get('aptamersequence')
        templatesequence= request.args.get('templatesequence')
        lengthofrandomregion= request.args.get('lengthofrandomregion')
        templatebias= request.args.get('templatebias')
        selexmethod= request.args.get('selexmethod')
        numberofselectionrounds= request.args.get('numberofselectionrounds')
        separationpartitioningmethod= request.args.get('separationpartitioningmethod')
        elutionrecoverymethod= request.args.get('elutionrecoverymethod')
        selectionsolutionbufferingagent= request.args.get('selectionsolutionbufferingagent')

        selectionsolutionph= request.args.get('selectionsolutionph')
        selectionsolutiontemperature= request.args.get('selectionsolutiontemperature')
        concentrationkm= request.args.get('concentrationkm')
        concentrationmgm= request.args.get('concentrationmgm')
        concentrationnam= request.args.get('concentrationnam')
        concentrationznm= request.args.get('concentrationznm')
        concentrationcam= request.args.get('concentrationcam')
        concentrationotherm= request.args.get('concentrationotherm')
        affinitymethod= request.args.get('affinitymethod')
        affinitymethodconditions= request.args.get('affinitymethodconditions')
        aptamertype= request.args.get('aptamertype')
        othermodification= request.args.get('othermodification')
        kdvalueinmolar= request.args.get('kdvalueinmolar')

        kderror= request.args.get('kderror')
        testedapplicationpurpose= request.args.get('testedapplicationpurpose')
        mutationalanalysis= request.args.get('mutationalanalysis')
        minamersyesno= request.args.get('minamersyesno')

        minimeronesequence= request.args.get('minimeronesequence')
        minimeronekd= request.args.get('minimeronekd')
        minimertwosequence= request.args.get('minimertwosequence')
        minimertwokd= request.args.get('minimertwokd')
        minimerthreesequence= request.args.get('minimerthreesequence')
        minimerthreekd= request.args.get('minimerthreekd')
        notes= request.args.get('notes')

        properties = provider.query_all(Article)

        if id:
            properties = Article.query.filter_by(id=id).first()
            result = article_schema.dump(properties)
            return jsonify(result)

        result_list = []

        #if name:
            #name = name.lower()
            #name_ids = []
            #for res_name in properties:
                #if name in res_name.name.lower():
                    #name_ids.append(res_name.id)
            #result_list.append(name_ids)

        if pubmedid:
            pubmedid = pubmedid.lower()
            pubmedid_ids = []
            for res_pubmedid in properties:
                if res_pubmedid.pubmedid is not None and pubmedid in res_pubmedid.pubmedid.lower():
                    pubmedid_ids.append(res_pubmedid.id)
            #print(pubmedid_ids)
            result_list.append(pubmedid_ids)

        if doinumber:
            doinumber = doinumber.lower()
            doinumber_ids = []
            for res_doinumber in properties:
                if doinumber in res_doinumber.doinumber.lower():
                    doinumber_ids.append(res_doinumber.id)
            result_list.append(doinumber_ids)

        if aptamertargettype:
            aptamertargettype = aptamertargettype.lower()
            aptamertargettype_ids = []
            for res_aptamertargettype in properties:
                if aptamertargettype in res_aptamertargettype.aptamertargettype.lower():
                    aptamertargettype_ids.append(res_aptamertargettype.id)
            result_list.append(aptamertargettype_ids)

        if aptamertargetname:
            aptamertargetname = aptamertargetname.lower()
            aptamertargetname_ids = []
            for res_aptamertargetname in properties:
                if aptamertargetname in res_aptamertargetname.aptamertargetname.lower():
                    aptamertargetname_ids.append(res_aptamertargetname.id)
            result_list.append(aptamertargetname_ids)

        if aptamersequence:
            aptamersequence = aptamersequence.lower()
            aptamersequence_ids = []
            for res_aptamersequence in properties:
                if aptamersequence in res_aptamersequence.aptamersequence.lower():
                    aptamersequence_ids.append(res_aptamersequence.id)
            result_list.append(aptamersequence_ids)

        if lengthofrandomregion:
            lengthofrandomregion = lengthofrandomregion.lower()
            lengthofrandomregion_ids = []
            for res_lengthofrandomregion in properties:
                if lengthofrandomregion in res_lengthofrandomregion.lengthofrandomregion.lower():
                    lengthofrandomregion_ids.append(res_lengthofrandomregion.id)
            result_list.append(lengthofrandomregion_ids)

        if templatesequence:
            templatesequence = templatesequence.lower()
            templatesequence_ids = []
            for res_templatesequence in properties:
                if templatesequence in res_templatesequence.templatesequence.lower():
                    templatesequence_ids.append(res_templatesequence.id)
            result_list.append(templatesequence_ids)


        if selexmethod:
            selexmethod = selexmethod.lower()
            selexmethod_ids = []
            for res_selexmethod in properties:
                if selexmethod in res_selexmethod.selexmethod.lower():
                    selexmethod_ids.append(res_selexmethod.id)
            result_list.append(selexmethod_ids)

        if yearofpublication:
            yearofpublication_ids = []
            for res_yearofpublication in properties:
                if yearofpublication in res_yearofpublication.yearofpublication:
                    yearofpublication_ids.append(res_yearofpublication.id)
            result_list.append(yearofpublication_ids)

        if templatebias:
            templatebias = templatebias.lower()
            templatebias_ids = []
            for res_templatebias in properties:
                if templatebias in res_templatebias.templatebias.lower():
                    templatebias_ids.append(res_templatebias.id)
            result_list.append(templatebias_ids)

        if numberofselectionrounds:
            numberofselectionrounds = numberofselectionrounds.lower()
            numberofselectionrounds_ids = []
            for res_numberofselectionrounds in properties:
                if numberofselectionrounds in res_numberofselectionrounds.numberofselectionrounds.lower():
                    numberofselectionrounds_ids.append(res_numberofselectionrounds.id)
            result_list.append(numberofselectionrounds_ids)

        if separationpartitioningmethod:
            separationpartitioningmethod = separationpartitioningmethod.lower()
            separationpartitioningmethod_ids = []
            for res_separationpartitioningmethod in properties:
                if separationpartitioningmethod in res_separationpartitioningmethod.separationpartitioningmethod.lower():
                    separationpartitioningmethod_ids.append(res_separationpartitioningmethod.id)
            result_list.append(separationpartitioningmethod_ids)

        if elutionrecoverymethod:
            elutionrecoverymethod = elutionrecoverymethod.lower()
            elutionrecoverymethod_ids = []
            for res_elutionrecoverymethod in properties:
                if elutionrecoverymethod in res_elutionrecoverymethod.elutionrecoverymethod.lower():
                    elutionrecoverymethod_ids.append(res_elutionrecoverymethod.id)
            result_list.append(elutionrecoverymethod_ids)

        if selectionsolutionbufferingagent:
            selectionsolutionbufferingagent = selectionsolutionbufferingagent.lower()
            selectionsolutionbufferingagent_ids = []
            for res_selectionsolutionbufferingagent in properties:
                if selectionsolutionbufferingagent in res_selectionsolutionbufferingagent.selectionsolutionbufferingagent.lower():
                    selectionsolutionbufferingagent_ids.append(res_selectionsolutionbufferingagent.id)
            result_list.append(selectionsolutionbufferingagent_ids)

        if selectionsolutionph:
            selectionsolutionph = selectionsolutionph.lower()
            selectionsolutionph_ids = []
            for res_selectionsolutionph in properties:
                if selectionsolutionph in res_selectionsolutionph.selectionsolutionph.lower():
                    selectionsolutionph_ids.append(res_selectionsolutionph.id)
            result_list.append(selectionsolutionph_ids)

        if selectionsolutiontemperature:
            selectionsolutiontemperature = selectionsolutiontemperature.lower()
            selectionsolutiontemperature_ids = []
            for res_selectionsolutiontemperature in properties:
                if selectionsolutiontemperature in res_selectionsolutiontemperature.selectionsolutiontemperature.lower():
                    selectionsolutiontemperature_ids.append(res_selectionsolutiontemperature.id)
            result_list.append(selectionsolutiontemperature_ids)

        if concentrationkm:
            concentrationkm = concentrationkm.lower()
            concentrationkm_ids = []
            for res_concentrationkm in properties:
                if concentrationkm in res_concentrationkm.concentrationkm.lower():
                    concentrationkm_ids.append(res_concentrationkm.id)
            result_list.append(concentrationkm_ids)

        if concentrationmgm:
            concentrationmgm = concentrationmgm.lower()
            concentrationmgm_ids = []
            for res_concentrationmgm in properties:
                if concentrationmgm in res_concentrationmgm.concentrationmgm.lower():
                    concentrationmgm_ids.append(res_concentrationmgm.id)
            result_list.append(concentrationmgm_ids)

        if concentrationnam:
            concentrationnam = concentrationnam.lower()
            concentrationnam_ids = []
            for res_concentrationnam in properties:
                if concentrationnam in res_concentrationnam.concentrationnam.lower():
                    concentrationnam_ids.append(res_concentrationnam.id)
            result_list.append(concentrationnam_ids)

        if concentrationznm:
            concentrationznm = concentrationznm.lower()
            concentrationznm_ids = []
            for res_concentrationznm in properties:
                if concentrationznm in res_concentrationznm.concentrationznm.lower():
                    concentrationznm_ids.append(res_concentrationznm.id)
            result_list.append(concentrationznm_ids)

        if concentrationcam:
            concentrationcam = concentrationcam.lower()
            concentrationcam_ids = []
            for res_concentrationcam in properties:
                if concentrationcam in res_concentrationcam.concentrationcam.lower():
                    concentrationcam_ids.append(res_concentrationcam.id)
            result_list.append(concentrationcam_ids)

        if concentrationotherm:
            concentrationotherm = concentrationotherm.lower()
            concentrationotherm_ids = []
            for res_concentrationotherm in properties:
                if concentrationotherm in res_concentrationotherm.concentrationotherm.lower():
                    concentrationotherm_ids.append(res_concentrationotherm.id)
            result_list.append(concentrationotherm_ids)

        if affinitymethod:
            affinitymethod = affinitymethod.lower()
            affinitymethod_ids = []
            for res_affinitymethod in properties:
                if affinitymethod in res_affinitymethod.affinitymethod.lower():
                    affinitymethod_ids.append(res_affinitymethod.id)
            result_list.append(affinitymethod_ids)

        if affinitymethodconditions:
            affinitymethodconditions = affinitymethodconditions.lower()
            affinitymethodconditions_ids = []
            for res_affinitymethodconditions in properties:
                if affinitymethodconditions in res_affinitymethodconditions.affinitymethodconditions.lower():
                    affinitymethodconditions_ids.append(res_affinitymethodconditions.id)
            result_list.append(affinitymethodconditions_ids)

        if aptamertype:
            aptamertype = aptamertype.lower()
            aptamertype_ids = []
            for res_aptamertype in properties:
                if aptamertype in res_aptamertype.aptamertype.lower():
                    aptamertype_ids.append(res_aptamertype.id)
            result_list.append(aptamertype_ids)

        if othermodification:
            othermodification = othermodification.lower()
            othermodification_ids = []
            for res_othermodification in properties:
                if othermodification in res_othermodification.othermodification.lower():
                    othermodification_ids.append(res_othermodification.id)
            result_list.append(othermodification_ids)

        if kdvalueinmolar:
            kdvalueinmolar = kdvalueinmolar.lower()
            kdvalueinmolar_ids = []
            for res_kdvalueinmolar in properties:
                if kdvalueinmolar in res_kdvalueinmolar.kdvalueinmolar.lower():
                    kdvalueinmolar_ids.append(res_kdvalueinmolar.id)
            result_list.append(kdvalueinmolar_ids)

        if kderror:
            kderror = kderror.lower()
            kderror_ids = []
            for res_kderror in properties:
                if kderror in res_kderror.kderror.lower():
                    kderror_ids.append(res_kderror.id)
            result_list.append(kderror_ids)

        if testedapplicationpurpose:
            testedapplicationpurpose = testedapplicationpurpose.lower()
            testedapplicationpurpose_ids = []
            for res_testedapplicationpurpose in properties:
                if testedapplicationpurpose in res_testedapplicationpurpose.testedapplicationpurpose.lower():
                    testedapplicationpurpose_ids.append(res_testedapplicationpurpose.id)
            result_list.append(testedapplicationpurpose_ids)

        if mutationalanalysis:
            mutationalanalysis = mutationalanalysis.lower()
            mutationalanalysis_ids = []
            for res_mutationalanalysis in properties:
                if mutationalanalysis in res_mutationalanalysis.mutationalanalysis.lower():
                    mutationalanalysis_ids.append(res_mutationalanalysis.id)
            result_list.append(mutationalanalysis_ids)

        if minamersyesno:
            minamersyesno = minamersyesno.lower()
            minamersyesno_ids = []
            for res_minamersyesno in properties:
                if minamersyesno in res_minamersyesno.minamersyesno.lower():
                    minamersyesno_ids.append(res_minamersyesno.id)
            result_list.append(minamersyesno_ids)

        if minimeronesequence:
            minimeronesequence = minimeronesequence.lower()
            minimeronesequence_ids = []
            for res_minimeronesequence in properties:
                if minimeronesequence in res_minimeronesequence.minimeronesequence.lower():
                    minimeronesequence_ids.append(res_minimeronesequence.id)
            result_list.append(minimeronesequence_ids)

        if minimeronekd:
            minimeronekd = minimeronekd.lower()
            minimeronekd_ids = []
            for res_minimeronekd in properties:
                if minimeronekd in res_minimeronekd.minimeronekd.lower():
                    minimeronekd_ids.append(res_minimeronekd.id)
            result_list.append(minimeronekd_ids)

        if minimertwosequence:
            minimertwosequence = minimertwosequence.lower()
            minimertwosequence_ids = []
            for res_minimertwosequence in properties:
                if minimertwosequence in res_minimertwosequence.minimertwosequence.lower():
                    minimertwosequence_ids.append(res_minimertwosequence.id)
            result_list.append(minimertwosequence_ids)

        if minimertwokd:
            minimertwokd = minimertwokd.lower()
            minimertwokd_ids = []
            for res_minimertwokd in properties:
                if minimertwokd in res_minimertwokd.minimertwokd.lower():
                    minimertwokd_ids.append(res_minimertwokd.id)
            result_list.append(minimertwokd_ids)

        if minimerthreesequence:
            minimerthreesequence = minimerthreesequence.lower()
            minimerthreesequence_ids = []
            for res_minimerthreesequence in properties:
                if minimerthreesequence in res_minimerthreesequence.minimerthreesequence.lower():
                    minimerthreesequence_ids.append(res_minimerthreesequence.id)
            result_list.append(minimerthreesequence_ids)

        if minimerthreekd:
            minimerthreekd = minimerthreekd.lower()
            minimerthreekd_ids = []
            for res_minimerthreekd in properties:
                if minimerthreekd in res_minimerthreekd.minimerthreekd.lower():
                    minimerthreekd_ids.append(res_minimerthreekd.id)
            result_list.append(minimerthreekd_ids)

        if notes:
            notes = notes.lower()
            notes_ids = []
            for res_notes in properties:
                if notes in res_notes.notes.lower():
                    notes_ids.append(res_notes.id)
            result_list.append(notes_ids)


        if len(result_list) > 2:
            intersection_fields_result_list = list(set(result_list[0]).intersection(set(result_list[1])))
            for i in range(2, len(result_list)):
                intersection_fields_result_list = list(set(intersection_fields_result_list).intersection(set(result_list[i])))
        elif len(result_list) == 2:
            intersection_fields_result_list = list(set(result_list[0]).intersection(set(result_list[1])))
        elif len(result_list) == 1:
            intersection_fields_result_list = result_list[0]
        else:
            result = article_schema_many.dump(properties)
            #result = None
            return jsonify(result)
        result = []
        for specific_id in intersection_fields_result_list:
            specific_properties = Article.query.filter_by(id=int(specific_id)).first()
            specific_result = article_schema.dump(specific_properties)
            result.append(specific_result)
        response = jsonify(result)
    except Exception as e:
        error = {"exception": str(e), "message": "Exception has occurred. Check the format of the request."}
        response = Response(json.dumps(error), 500, mimetype="application/json")

    return response


@aptamer_bp.route("/articles", methods=['POST'])
@crossdomain(origin='*')
@authentication
def add_article():
    try:
        user = user_provider.get_authenticated_user()
        is_researcher_administrator = user_provider.has_role(user, 'Researcher') or user_provider.has_role(user,
                                                                                                           'Administrator')
        if is_researcher_administrator:
            data = request.get_json()
            article = provider.add(data)
            result = article_schema.dump(article)
            response = jsonify(result)
        else:
            error = {"message": "Access Denied"}
            response = Response(json.dumps(error), 403, mimetype="application/json")

    except Exception as e:
        error = {"exception": str(e), "message": "Exception has occurred. Check the format of the request."}
        response = Response(json.dumps(error), 500, mimetype="application/json")

    return response


@aptamer_bp.route("/articles", methods=['PUT'])
@crossdomain(origin='*')
@authentication
def update_article():
    try:
        user = user_provider.get_authenticated_user()
        is_researcher_administrator = user_provider.has_role(user, 'Researcher') or user_provider.has_role(user,
                                                                                                           'Administrator')
        if is_researcher_administrator:
            data = request.get_json()
            article = Article.query.filter_by(id=data.get('id')).first()
            if not article:
                article = Article.query.filter_by(pubmedid=data.get('pubmedid')).first()
            if article:
                if data.get('id') is None:
                    data['id'] = article.id
                provider.update(data, article)
                db.session.commit()
                response = Response(json.dumps(data), 200, mimetype="application/json")
            else:
                response = Response(json.dumps(data), 404, mimetype="application/json")
        else:
            error = {"message": "Access Denied"}
            response = Response(json.dumps(error), 403, mimetype="application/json")
    except Exception as e:
        error = {"exception": str(e), "message": "Exception has occurred. Check the format of the request."}
        response = Response(json.dumps(error), 500, mimetype="application/json")

    return response


@aptamer_bp.route("/articles", methods=['DELETE'])
@crossdomain(origin='*')
@authentication
def delete_article():
    try:
        user = user_provider.get_authenticated_user()
        is_researcher_administrator = user_provider.has_role(user, 'Researcher') or user_provider.has_role(user, 'Administrator')
        if is_researcher_administrator:

            data = request.get_json()
            article = Article.query.filter_by(id=data.get('id')).first()

            if not article:
                article = Article.query.filter_by(pubmedid=data.get('pubmedid')).first()
            if article:
                db.session.delete(article)
                db.session.commit()
                response = Response(json.dumps(data), 200, mimetype="application/json")
            else:
                response = Response(json.dumps(data), 404, mimetype="application/json")
        else:
            error = {"message": "Access Denied"}
            response = Response(json.dumps(error), 403, mimetype="application/json")
    except Exception as e:
        error = {"exception": str(e), "message": "Exception has occurred. Check the format of the request."}
        response = Response(json.dumps(error), 500, mimetype="application/json")
    return response


@aptamer_bp.route("/articles/export", methods=['GET'])
@crossdomain(origin='*')
@authentication
def export_articles():
    try:
        id = request.args.get('id')
        #name = request.args.get('name')

        pubmedid = request.args.get('pubmedid')
        doinumber= request.args.get('doinumber')
        yearofpublication= request.args.get('yearofpublication')
        aptamertargettype= request.args.get('aptamertargettype')
        aptamertargetname= request.args.get('aptamertargetname')
        aptamersequence= request.args.get('aptamersequence')
        templatesequence= request.args.get('templatesequence')
        lengthofrandomregion= request.args.get('lengthofrandomregion')
        templatebias= request.args.get('templatebias')
        selexmethod= request.args.get('selexmethod')
        numberofselectionrounds= request.args.get('numberofselectionrounds')
        separationpartitioningmethod= request.args.get('separationpartitioningmethod')
        elutionrecoverymethod= request.args.get('elutionrecoverymethod')
        selectionsolutionbufferingagent= request.args.get('selectionsolutionbufferingagent')

        selectionsolutionph= request.args.get('selectionsolutionph')
        selectionsolutiontemperature= request.args.get('selectionsolutiontemperature')
        concentrationkm= request.args.get('concentrationkm')
        concentrationmgm= request.args.get('concentrationmgm')
        concentrationnam= request.args.get('concentrationnam')
        concentrationznm= request.args.get('concentrationznm')
        concentrationcam= request.args.get('concentrationcam')
        concentrationotherm= request.args.get('concentrationotherm')
        affinitymethod= request.args.get('affinitymethod')
        affinitymethodconditions= request.args.get('affinitymethodconditions')
        aptamertype= request.args.get('aptamertype')
        othermodification= request.args.get('othermodification')
        kdvalueinmolar= request.args.get('kdvalueinmolar')

        kderror= request.args.get('kderror')
        testedapplicationpurpose= request.args.get('testedapplicationpurpose')
        mutationalanalysis= request.args.get('mutationalanalysis')
        minamersyesno= request.args.get('minamersyesno')

        minimeronesequence= request.args.get('minimeronesequence')
        minimeronekd= request.args.get('minimeronekd')
        minimertwosequence= request.args.get('minimertwosequence')
        minimertwokd= request.args.get('minimertwokd')
        minimerthreesequence= request.args.get('minimerthreesequence')
        minimerthreekd= request.args.get('minimerthreekd')
        notes= request.args.get('notes')

        properties = provider.query_all(Article)

        if id:
            properties = Article.query.filter_by(id=id).first()
            result = article_schema.dump(properties)
            return jsonify(result)

        result_list = []
        if pubmedid:
            pubmedid = pubmedid.lower()
            pubmedid_ids = []
            for res_pubmedid in properties:
                if res_pubmedid.pubmedid is not None and pubmedid in res_pubmedid.pubmedid.lower():
                    pubmedid_ids.append(res_pubmedid.id)
            # print(pubmedid_ids)
            result_list.append(pubmedid_ids)

        if doinumber:
            doinumber = doinumber.lower()
            doinumber_ids = []
            for res_doinumber in properties:
                if doinumber in res_doinumber.doinumber.lower():
                    doinumber_ids.append(res_doinumber.id)
            result_list.append(doinumber_ids)

        if aptamertargettype:
            aptamertargettype = aptamertargettype.lower()
            aptamertargettype_ids = []
            for res_aptamertargettype in properties:
                if aptamertargettype in res_aptamertargettype.aptamertargettype.lower():
                    aptamertargettype_ids.append(res_aptamertargettype.id)
            result_list.append(aptamertargettype_ids)

        if aptamertargetname:
            aptamertargetname = aptamertargetname.lower()
            aptamertargetname_ids = []
            for res_aptamertargetname in properties:
                if aptamertargetname in res_aptamertargetname.aptamertargetname.lower():
                    aptamertargetname_ids.append(res_aptamertargetname.id)
            result_list.append(aptamertargetname_ids)

        if aptamersequence:
            aptamersequence = aptamersequence.lower()
            aptamersequence_ids = []
            for res_aptamersequence in properties:
                if aptamersequence in res_aptamersequence.aptamersequence.lower():
                    aptamersequence_ids.append(res_aptamersequence.id)
            result_list.append(aptamersequence_ids)

        if lengthofrandomregion:
            lengthofrandomregion = lengthofrandomregion.lower()
            lengthofrandomregion_ids = []
            for res_lengthofrandomregion in properties:
                if lengthofrandomregion in res_lengthofrandomregion.lengthofrandomregion.lower():
                    lengthofrandomregion_ids.append(res_lengthofrandomregion.id)
            result_list.append(lengthofrandomregion_ids)

        if templatesequence:
            templatesequence = templatesequence.lower()
            templatesequence_ids = []
            for res_templatesequence in properties:
                if templatesequence in res_templatesequence.templatesequence.lower():
                    templatesequence_ids.append(res_templatesequence.id)
            result_list.append(templatesequence_ids)

        if selexmethod:
            selexmethod = selexmethod.lower()
            selexmethod_ids = []
            for res_selexmethod in properties:
                if selexmethod in res_selexmethod.selexmethod.lower():
                    selexmethod_ids.append(res_selexmethod.id)
            result_list.append(selexmethod_ids)

        if yearofpublication:
            yearofpublication_ids = []
            for res_yearofpublication in properties:
                if yearofpublication in res_yearofpublication.yearofpublication:
                    yearofpublication_ids.append(res_yearofpublication.id)
            result_list.append(yearofpublication_ids)

        if templatebias:
            templatebias = templatebias.lower()
            templatebias_ids = []
            for res_templatebias in properties:
                if templatebias in res_templatebias.templatebias.lower():
                    templatebias_ids.append(res_templatebias.id)
            result_list.append(templatebias_ids)

        if numberofselectionrounds:
            numberofselectionrounds = numberofselectionrounds.lower()
            numberofselectionrounds_ids = []
            for res_numberofselectionrounds in properties:
                if numberofselectionrounds in res_numberofselectionrounds.numberofselectionrounds.lower():
                    numberofselectionrounds_ids.append(res_numberofselectionrounds.id)
            result_list.append(numberofselectionrounds_ids)

        if separationpartitioningmethod:
            separationpartitioningmethod = separationpartitioningmethod.lower()
            separationpartitioningmethod_ids = []
            for res_separationpartitioningmethod in properties:
                if separationpartitioningmethod in res_separationpartitioningmethod.separationpartitioningmethod.lower():
                    separationpartitioningmethod_ids.append(res_separationpartitioningmethod.id)
            result_list.append(separationpartitioningmethod_ids)

        if elutionrecoverymethod:
            elutionrecoverymethod = elutionrecoverymethod.lower()
            elutionrecoverymethod_ids = []
            for res_elutionrecoverymethod in properties:
                if elutionrecoverymethod in res_elutionrecoverymethod.elutionrecoverymethod.lower():
                    elutionrecoverymethod_ids.append(res_elutionrecoverymethod.id)
            result_list.append(elutionrecoverymethod_ids)

        if selectionsolutionbufferingagent:
            selectionsolutionbufferingagent = selectionsolutionbufferingagent.lower()
            selectionsolutionbufferingagent_ids = []
            for res_selectionsolutionbufferingagent in properties:
                if selectionsolutionbufferingagent in res_selectionsolutionbufferingagent.selectionsolutionbufferingagent.lower():
                    selectionsolutionbufferingagent_ids.append(res_selectionsolutionbufferingagent.id)
            result_list.append(selectionsolutionbufferingagent_ids)

        if selectionsolutionph:
            selectionsolutionph = selectionsolutionph.lower()
            selectionsolutionph_ids = []
            for res_selectionsolutionph in properties:
                if selectionsolutionph in res_selectionsolutionph.selectionsolutionph.lower():
                    selectionsolutionph_ids.append(res_selectionsolutionph.id)
            result_list.append(selectionsolutionph_ids)

        if selectionsolutiontemperature:
            selectionsolutiontemperature = selectionsolutiontemperature.lower()
            selectionsolutiontemperature_ids = []
            for res_selectionsolutiontemperature in properties:
                if selectionsolutiontemperature in res_selectionsolutiontemperature.selectionsolutiontemperature.lower():
                    selectionsolutiontemperature_ids.append(res_selectionsolutiontemperature.id)
            result_list.append(selectionsolutiontemperature_ids)

        if concentrationkm:
            concentrationkm = concentrationkm.lower()
            concentrationkm_ids = []
            for res_concentrationkm in properties:
                if concentrationkm in res_concentrationkm.concentrationkm.lower():
                    concentrationkm_ids.append(res_concentrationkm.id)
            result_list.append(concentrationkm_ids)

        if concentrationmgm:
            concentrationmgm = concentrationmgm.lower()
            concentrationmgm_ids = []
            for res_concentrationmgm in properties:
                if concentrationmgm in res_concentrationmgm.concentrationmgm.lower():
                    concentrationmgm_ids.append(res_concentrationmgm.id)
            result_list.append(concentrationmgm_ids)

        if concentrationnam:
            concentrationnam = concentrationnam.lower()
            concentrationnam_ids = []
            for res_concentrationnam in properties:
                if concentrationnam in res_concentrationnam.concentrationnam.lower():
                    concentrationnam_ids.append(res_concentrationnam.id)
            result_list.append(concentrationnam_ids)

        if concentrationznm:
            concentrationznm = concentrationznm.lower()
            concentrationznm_ids = []
            for res_concentrationznm in properties:
                if concentrationznm in res_concentrationznm.concentrationznm.lower():
                    concentrationznm_ids.append(res_concentrationznm.id)
            result_list.append(concentrationznm_ids)

        if concentrationcam:
            concentrationcam = concentrationcam.lower()
            concentrationcam_ids = []
            for res_concentrationcam in properties:
                if concentrationcam in res_concentrationcam.concentrationcam.lower():
                    concentrationcam_ids.append(res_concentrationcam.id)
            result_list.append(concentrationcam_ids)

        if concentrationotherm:
            concentrationotherm = concentrationotherm.lower()
            concentrationotherm_ids = []
            for res_concentrationotherm in properties:
                if concentrationotherm in res_concentrationotherm.concentrationotherm.lower():
                    concentrationotherm_ids.append(res_concentrationotherm.id)
            result_list.append(concentrationotherm_ids)

        if affinitymethod:
            affinitymethod = affinitymethod.lower()
            affinitymethod_ids = []
            for res_affinitymethod in properties:
                if affinitymethod in res_affinitymethod.affinitymethod.lower():
                    affinitymethod_ids.append(res_affinitymethod.id)
            result_list.append(affinitymethod_ids)

        if affinitymethodconditions:
            affinitymethodconditions = affinitymethodconditions.lower()
            affinitymethodconditions_ids = []
            for res_affinitymethodconditions in properties:
                if affinitymethodconditions in res_affinitymethodconditions.affinitymethodconditions.lower():
                    affinitymethodconditions_ids.append(res_affinitymethodconditions.id)
            result_list.append(affinitymethodconditions_ids)

        if aptamertype:
            aptamertype = aptamertype.lower()
            aptamertype_ids = []
            for res_aptamertype in properties:
                if aptamertype in res_aptamertype.aptamertype.lower():
                    aptamertype_ids.append(res_aptamertype.id)
            result_list.append(aptamertype_ids)

        if othermodification:
            othermodification = othermodification.lower()
            othermodification_ids = []
            for res_othermodification in properties:
                if othermodification in res_othermodification.othermodification.lower():
                    othermodification_ids.append(res_othermodification.id)
            result_list.append(othermodification_ids)

        if kdvalueinmolar:
            kdvalueinmolar = kdvalueinmolar.lower()
            kdvalueinmolar_ids = []
            for res_kdvalueinmolar in properties:
                if kdvalueinmolar in res_kdvalueinmolar.kdvalueinmolar.lower():
                    kdvalueinmolar_ids.append(res_kdvalueinmolar.id)
            result_list.append(kdvalueinmolar_ids)

        if kderror:
            kderror = kderror.lower()
            kderror_ids = []
            for res_kderror in properties:
                if kderror in res_kderror.kderror.lower():
                    kderror_ids.append(res_kderror.id)
            result_list.append(kderror_ids)

        if testedapplicationpurpose:
            testedapplicationpurpose = testedapplicationpurpose.lower()
            testedapplicationpurpose_ids = []
            for res_testedapplicationpurpose in properties:
                if testedapplicationpurpose in res_testedapplicationpurpose.testedapplicationpurpose.lower():
                    testedapplicationpurpose_ids.append(res_testedapplicationpurpose.id)
            result_list.append(testedapplicationpurpose_ids)

        if mutationalanalysis:
            mutationalanalysis = mutationalanalysis.lower()
            mutationalanalysis_ids = []
            for res_mutationalanalysis in properties:
                if mutationalanalysis in res_mutationalanalysis.mutationalanalysis.lower():
                    mutationalanalysis_ids.append(res_mutationalanalysis.id)
            result_list.append(mutationalanalysis_ids)

        if minamersyesno:
            minamersyesno = minamersyesno.lower()
            minamersyesno_ids = []
            for res_minamersyesno in properties:
                if minamersyesno in res_minamersyesno.minamersyesno.lower():
                    minamersyesno_ids.append(res_minamersyesno.id)
            result_list.append(minamersyesno_ids)

        if minimeronesequence:
            minimeronesequence = minimeronesequence.lower()
            minimeronesequence_ids = []
            for res_minimeronesequence in properties:
                if minimeronesequence in res_minimeronesequence.minimeronesequence.lower():
                    minimeronesequence_ids.append(res_minimeronesequence.id)
            result_list.append(minimeronesequence_ids)

        if minimeronekd:
            minimeronekd = minimeronekd.lower()
            minimeronekd_ids = []
            for res_minimeronekd in properties:
                if minimeronekd in res_minimeronekd.minimeronekd.lower():
                    minimeronekd_ids.append(res_minimeronekd.id)
            result_list.append(minimeronekd_ids)

        if minimertwosequence:
            minimertwosequence = minimertwosequence.lower()
            minimertwosequence_ids = []
            for res_minimertwosequence in properties:
                if minimertwosequence in res_minimertwosequence.minimertwosequence.lower():
                    minimertwosequence_ids.append(res_minimertwosequence.id)
            result_list.append(minimertwosequence_ids)

        if minimertwokd:
            minimertwokd = minimertwokd.lower()
            minimertwokd_ids = []
            for res_minimertwokd in properties:
                if minimertwokd in res_minimertwokd.minimertwokd.lower():
                    minimertwokd_ids.append(res_minimertwokd.id)
            result_list.append(minimertwokd_ids)

        if minimerthreesequence:
            minimerthreesequence = minimerthreesequence.lower()
            minimerthreesequence_ids = []
            for res_minimerthreesequence in properties:
                if minimerthreesequence in res_minimerthreesequence.minimerthreesequence.lower():
                    minimerthreesequence_ids.append(res_minimerthreesequence.id)
            result_list.append(minimerthreesequence_ids)

        if minimerthreekd:
            minimerthreekd = minimerthreekd.lower()
            minimerthreekd_ids = []
            for res_minimerthreekd in properties:
                if minimerthreekd in res_minimerthreekd.minimerthreekd.lower():
                    minimerthreekd_ids.append(res_minimerthreekd.id)
            result_list.append(minimerthreekd_ids)

        if notes:
            notes = notes.lower()
            notes_ids = []
            for res_notes in properties:
                if notes in res_notes.notes.lower():
                    notes_ids.append(res_notes.id)
            result_list.append(notes_ids)

        if len(result_list) > 2:
            intersection_fields_result_list = list(set(result_list[0]).intersection(set(result_list[1])))
            for i in range(2, len(result_list)):
                intersection_fields_result_list = list(
                    set(intersection_fields_result_list).intersection(set(result_list[i])))
        elif len(result_list) == 2:
            intersection_fields_result_list = list(set(result_list[0]).intersection(set(result_list[1])))
        elif len(result_list) == 1:
            intersection_fields_result_list = result_list[0]
        else:
            intersection_fields_result_list = get_all_article_ids()
        specific_users_info = []

        for specific_id in intersection_fields_result_list:
            s_a = Article.query.filter_by(id=specific_id).first()
            specific_users_info.append({
                #"ID": s_a.id,

                "PubMed ID": s_a.pubmedid,
                "DOI number": s_a.doinumber,
                "Year of publication": s_a.yearofpublication,
                "Aptamer Target Type": s_a.aptamertargettype,
                "Aptamer Target Name": s_a.aptamertargetname,
                "Aptamer Sequence": s_a.aptamersequence,
                "Template sequence: e.g., GCAATGGTACGGTACTGTC-N40-AATCAGTGCACGCTACTTTGCTAA": s_a.templatesequence,
                "Length of random region": s_a.lengthofrandomregion,
                "Template Bias": s_a.templatebias,
                "SELEX Method": s_a.selexmethod,
                "Number of Selection Rounds": s_a.numberofselectionrounds,
                "Separation (Partitioning) Method": s_a.separationpartitioningmethod,
                "Elution/Recovery method": s_a.elutionrecoverymethod,
                "Selection Solution Buffering Agent": s_a.selectionsolutionbufferingagent,
                "Selection Solution pH": s_a.selectionsolutionph,
                "Selection Solution Temperature °C": s_a.selectionsolutiontemperature,
                "Concentration K (M)": s_a.concentrationkm,
                "Concentration Mg (M)": s_a.concentrationmgm,
                "Concentration Na (M)": s_a.concentrationnam,
                "Concentration Zn (M)": s_a.concentrationznm,
                "Concentration Ca (M)": s_a.concentrationcam,
                "Concentration Other (M)": s_a.concentrationotherm,
                "Affinity Method": s_a.affinitymethod,
                "Affinity Method Conditions": s_a.affinitymethodconditions,
                "Aptamer Type": s_a.aptamertype,
                "Other modification": s_a.othermodification,
                "KD Value (in Molar)": s_a.kdvalueinmolar,
                "KD Error": s_a.kderror,
                "Tested application/ purpose": s_a.testedapplicationpurpose,
                "Mutational Analysis": s_a.mutationalanalysis,
                "Minamers  (yes/no)": s_a.minamersyesno,
                "Minimer 1 sequence": s_a.minimeronesequence,
                "Minimer 1 Kd": s_a.minimeronekd,
                "Minimer 2 sequence": s_a.minimertwosequence,
                "Minimer 2 Kd": s_a.minimertwokd,
                "Minimer 3 sequence": s_a.minimerthreesequence,
                "Minimer 3 Kd": s_a.minimerthreekd,
                "Notes": s_a.notes
            })

        output = BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            pd.DataFrame(specific_users_info).to_excel(writer,
                                           sheet_name="articles",
                                           index=False)
            workbook = writer.book
            worksheet = writer.sheets["articles"]
            format = workbook.add_format()
            format.set_align('center')
            format.set_align('vcenter')
            worksheet.set_column('A:A', 12, format)
            worksheet.set_column('B:B', 38, format)
            worksheet.set_column('C:C', 22, format)
            worksheet.set_column('D:D', 38, format)
            worksheet.set_column('E:E', 15, format)
            worksheet.set_column('F:AL', 18, format)
            writer.save()
        output.seek(0)
        return send_file(output,
                         attachment_filename="Articles" + '.xlsx',
                         mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                         as_attachment=True, cache_timeout=-1)
    except Exception as e:
        error = {"exception": str(e), "message": "Exception has occurred. Check the format of the request."}
        response = Response(json.dumps(error), 404, mimetype="application/json")
        return response



@aptamer_bp.route("/articles/citation", methods=['GET'])
@crossdomain(origin='*')
@authentication
def generate_citation_articles():
    specific_ids = request.args.get('id')
    if specific_ids is not None:
        try:
            name = request.args.get('name')
            if name is None:
                article_id = request.args.get('id')
                s_a = Article.query.filter_by(id=article_id).first()
                name = s_a.name
                s_a = Article.query.filter_by(name=name).first()
            else:
                article_id = request.args.get('id')
            author_last_name = s_a.aptamertargetname.split(" ")[1]
            author_first_name_ini = s_a.aptamertargetname.split(" ")[0][0]
            citation = f"{author_last_name}, {author_first_name_ini}. ({s_a.yearofpublication}). {s_a.name}. {s_a.templatesequence}: {s_a.lengthofrandomregion}."
            #txt = BytesIO()
            #txt.write(citation.encode("utf8"))
            output = BytesIO()
            output.write(citation.encode("utf8"))
            output.seek(0)
            #txt.seek(0)
            return send_file(output,
                             attachment_filename='citation.txt',
                             as_attachment=True, cache_timeout=-1)
        except Exception as e:
            response = Response(json.dumps(e), 404, mimetype="application/json")
            return response


@aptamer_bp.route("/articles/upload", methods=['POST'])
@crossdomain(origin='*')
@authentication
def upload_articles():
    raw_data = request.get_data()
    data = pd.read_excel(raw_data, engine="openpyxl")
    try:
        user = user_provider.get_authenticated_user()
        is_researcher_administrator = user_provider.has_role(user, 'Researcher') or user_provider.has_role(user, 'Administrator')
        if is_researcher_administrator:
            for _, row in data.iterrows():
                d = dict(row)
                if type(d["PubMed ID"]) == int or type(d["Year of publication"]) == int:
                    article = {
                        "id": provider.generate_id(field=Article.id),
                        "name": "test",
                        "pubmedid": "" if str(d["PubMed ID"]) == "nan" else str(int(d["PubMed ID"])),
                        "doinumber": "" if type(d["DOI number"]) == float else str(d["DOI number"]),
                        "yearofpublication": "" if type(d["Year of publication"]) == float else str(
                            d["Year of publication"]),
                        "aptamertargettype": "" if type(d["Aptamer Target Type"]) == float else str(
                            d["Aptamer Target Type"]),
                        "aptamertargetname": "" if type(d["Aptamer Target Name"]) == float else str(
                            d["Aptamer Target Name"]),
                        "aptamersequence": "" if type(d["Aptamer Sequence"]) == float else str(d["Aptamer Sequence"]),
                        #"aptamersequence": "CATCCATGGG",
                        "templatesequence": "" if type(d[
                                                           "Template sequence: e.g., GCAATGGTACGGTACTGTC-N40-AATCAGTGCACGCTACTTTGCTAA"]) == float else str(
                            d["Template sequence: e.g., GCAATGGTACGGTACTGTC-N40-AATCAGTGCACGCTACTTTGCTAA"]),
                        "lengthofrandomregion": "" if str(d["Length of random region"]) == 'nan' else str(
                            d["Length of random region"]),
                        "templatebias": "" if type(d["Template Bias"]) == float else str(d["Template Bias"]),
                        "selexmethod": "" if type(d["SELEX Method"]) == float else str(d["SELEX Method"]),
                        "numberofselectionrounds": "" if str(d["Number of Selection Rounds"]) == "nan" else str(
                            d["Number of Selection Rounds"]),
                        "separationpartitioningmethod": "" if type(
                            d["Separation (Partitioning) Method"]) == float else str(
                            d["Separation (Partitioning) Method"]),
                        "elutionrecoverymethod": "" if type(d["Elution/Recovery method"]) == float else str(
                            d["Elution/Recovery method"]),
                        "selectionsolutionbufferingagent": "" if type(
                            d["Selection Solution Buffering Agent"]) == float else str(
                            d["Selection Solution Buffering Agent"]),
                        "selectionsolutionph": "" if str(d["Selection Solution pH"]) == "nan" else str(
                            round(d["Selection Solution pH"], 1)),
                        "selectionsolutiontemperature": "" if str(
                            d["Selection Solution Temperature °C"]) == "nan" else str(
                            d["Selection Solution Temperature °C"]),
                        "concentrationkm": "" if str(d["Concentration K (M)"]) == "nan" else str(
                            d["Concentration K (M)"]),
                        "concentrationmgm": "" if str(d["Concentration Mg (M)"]) == "nan" else str(
                            d["Concentration Mg (M)"]),
                        "concentrationnam": "" if str(d["Concentration Na (M)"]) == "nan" else str(
                            d["Concentration Na (M)"]),
                        "concentrationznm": "" if str(d["Concentration Zn (M)"]) == "nan" else str(
                            d["Concentration Zn (M)"]),
                        "concentrationcam": "" if str(d["Concentration Ca (M)"]) == "nan" else str(
                            d["Concentration Ca (M)"]),
                        "concentrationotherm": "" if str(d["Concentration Other (M)"]) == "nan" else str(
                            d["Concentration Other (M)"]),
                        "affinitymethod": "" if type(d["Affinity Method"]) == float else str(d["Affinity Method"]),
                        "affinitymethodconditions": "" if type(d["Affinity Method Conditions"]) == float else str(
                            d["Affinity Method Conditions"]),
                        "aptamertype": "" if type(d["Aptamer Type"]) == float else str(d["Aptamer Type"]),
                        "othermodification": "" if type(d["Other modification"]) == float else str(
                            d["Other modification"]),
                        "kdvalueinmolar": "" if str(d["KD Value (in Molar)"]) == "nan" else str(
                            d["KD Value (in Molar)"]),
                        "kderror": "" if str(d["KD Error"]) == "nan" else str(d["KD Error"]),
                        "testedapplicationpurpose": "" if type(d["Tested application/ purpose"]) == float else str(
                            d["Tested application/ purpose"]),
                        "mutationalanalysis": "" if type(d["Mutational Analysis"]) == float else str(
                            d["Mutational Analysis"]),
                        "minamersyesno": "" if type(d["Minamers  (yes/no)"]) == float else str(d["Minamers  (yes/no)"]),
                        "minimeronesequence": "n/a" if str(d["Minimer 1 sequence"]) == "nan" else str(
                            d["Minimer 1 sequence"]),
                        "minimeronekd": "n/a" if str(d["Minimer 1 Kd"]) == "nan" else str(d["Minimer 1 Kd"]),
                        "minimertwosequence": "n/a" if str(d["Minimer 2 sequence"]) == "nan" else str(
                            d["Minimer 2 sequence"]),
                        "minimertwokd": "n/a" if str(d["Minimer 2 Kd"]) == "nan" else str(d["Minimer 2 Kd"]),
                        "minimerthreesequence": "n/a" if str(d["Minimer 3 sequence"]) == "nan" else str(
                            d["Minimer 3 sequence"]),
                        "minimerthreekd": "n/a" if str(d["Minimer 3 Kd"]) == "nan" else str(d["Minimer 3 Kd"]),
                        "notes": "" if type(d["Notes"]) == float else str(d["Notes"]),
                        "status": "Approved",
                        "operator": user_provider.get_authenticated_user().name
                    }

                    articles = Article(article)
                    db.session.add(articles)
                    db.session.commit()
            response = Response(json.dumps({"success": True}), 200, mimetype="application/json")
        else:
            error = {"message": "Access Denied"}
            response = Response(json.dumps(error), 403, mimetype="application/json")
    except Exception as e:
        error = {"exception": str(e), "message": "Exception has occurred. Check the format of the request."}
        response = Response(json.dumps(error), 500, mimetype="application/json")

    return response

def get_all_article_ids():
    articles = Article.query.all()
    result = article_schema_many.dump(articles)
    article_ids = []
    for article in result:
        article_ids.append(article['id'])
    return article_ids



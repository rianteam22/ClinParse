from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Identificacao(BaseModel):
    nome: str = Field(description="Nome completo da paciente")
    registro: str = Field(description="Número de registro da paciente")
    local: str = Field(description="Local (IMIP, ISEA, MDER)")
    data_nascimento: datetime = Field(description="Data de nascimento da paciente")
    endereco: str = Field(description="Endereço completo")
    telefone1: str = Field(description="Primeiro número de telefone da paciente")
    telefone2: str = Field(description="Segundo número de telefone da paciente(caso haja)")
    data_admissao: datetime = Field(description="Data de admissão no hospital")

class DadosGerais(BaseModel):
    idade: int = Field(description="Idade da paciente em anos")
    gesta: int = Field(description="Número de gestações")
    para: int = Field(description="Número de partos")
    aborto: int = Field(description="Número de abortos")
    cor_autorreferida: str = Field(description="Cor autorreferida da paciente")
    escolaridade: str = Field(description="Escolaridade da paciente")
    ocupacao_descritiva: str = Field(description="Ocupação descritiva da paciente")
    ocupacao_categorizada: str = Field(description="Ocupação categorizada da paciente(publico/privado/dona de casa/autônoma/desempregada)")
    renda_familiar_descritiva: float = Field(description="Renda familiar descritiva da paciente")
    renda_familiar_categorizada: str = Field(description="Renda familiar da paciente (<meio SM/ meio a 1 SM/ >1 a 5 SM/ >5 a 10 SM/ >10 SM)")
    peso: float = Field(description="Peso da paciente em kg")
    estatura: float = Field(description="Altura da paciente em cm")
    imc: float = Field(description="Índice de massa corporal")
    procedencia: str = Field(description="Procedência da paciente")
    cidade_origem: str = Field(description="Cidade de origem da paciente(Recife e região metropolitana, Teresina e região metropolitana, Campina Grande e região metropolitana, Interior do Pernambuco, Interior do Piauí, Interior da Paraíba, Outros Estados)")

class Comorbidades(BaseModel):
    comorbidades: bool = Field(description="Presença de comorbidades")
    has: bool = Field(description="Presença de hipertensão arterial")
    dm: bool = Field(description="Presença de diabetes mellitus")
    doenca_renal_cronica: bool = Field(description="Presença de doença renal crônica")
    doenca_hepatica_cronica: bool = Field(description="Presença de doença hepática crônica")
    cardiopatia: bool = Field(description="Presença de cardiopatia")
    hiv: bool = Field(description="Presença de HIV")
    les: bool = Field(description="Presença de lúpus eritematoso sistêmico")
    anemia_falciforme: bool = Field(description="Presença de anemia falciforme")
    outras_comorbidades: bool = Field(description="Presença de outras comorbidades")
    descricao_outras_comorbidades: str = Field(description="Descrição de outras comorbidades", default="")

class HabitosDeVida(BaseModel):
    etilismo: bool = Field(description="Presença de etilismo")
    tabagismo: bool = Field(description="Presença de tabagismo")
    drogas_ilicitas: bool = Field(description="Uso de drogas ilícitas")

class DadosObstetricos(BaseModel):
    admissao: str = Field(description="Período de admissão (anteparto, intraparto, pós-parto, ou pós-aborto)")
    idade_gestacional_admissao: int = Field(description="Idade gestacional na admissão em semanas")
    idade_gestacional_parto: Optional[int] = Field(description="Idade gestacional no parto em semanas", default="null")
    idade_gestacional_diagnostico_infeccao: Optional[int] = Field(description="Idade gestacional no diagnóstico da infecção em semanas", default="null")
    
    via_de_parto: str = Field(description="Via de parto (vaginal, vaginal instrumental, cesárea eletiva, cesárea intraparto)")
    desfecho_gestacao: str = Field(description="Desfecho da gestação (aborto, parto vaginal, parto vaginal instrumental, cesárea eletiva, cesárea intraparto, alta grávida, óbito grávida)")

class ComplicacoesObstetricas(BaseModel):
    pre_eclampsia: bool = Field(description="Presença de pré-eclâmpsia")
    eclampsia: bool = Field(description="Presença de eclâmpsia")
    sindrome_hellp: bool = Field(description="Presença da Síndrome HELLP")
    dmg: bool = Field(description="Presença de DMG (Diabetes Mellitus Gestacional)")
    hemorragia_pos_parto: bool = Field(description="Presença de hemorragia pós-parto")
    rpmo: bool = Field(description="Presença de RPMO (Ruptura Prematura de Membranas Ovais)")
    tpp: bool = Field(description="Presença de TPP (Trabalho de Parto Prematuro)")
    outras_complicacoes: bool = Field(description="Presença de outras complicações")
    descricao_outras_complicacoes: Optional[str] = Field(description="Descrição de outras complicações", default="")

class DadosInfeccao(BaseModel):
    estagio_infeccao_admissao: str = Field(description="Estágio da infecção no momento da admissão (sem infecção, infecção sem sepse, sepse, choque séptico)")
    estagio_gravidez_diagnostico_infeccao: str = Field(description="Estágio da gravidez no momento do diagnóstico da infecção (grávida, parturiente, puérpera, pós-aborto)")
    tipo_infeccao: str = Field(description="Tipo de infecção (obstétrica, nÃO obstétrica, mista)")
    descricao_infeccao: Optional[str] = Field(description="Descrição da infecção", default="")
    
    foco_infeccao: str = Field(description="Foco da infecção (respiratório, urinário, abdominal, uterino, sítio cirúrgico, outros)")
    descricao_foco_outros: Optional[str] = Field(description="Descrição do foco da infecção se 'Outros'", default="")
    
    realizou_cultura: bool = Field(description="Se a cultura foi realizada (SIM/NÃO)")
    cultura_positiva: bool = Field(description="Se a cultura foi positiva (SIM/NÃO)")
    resultado_cultura: Optional[str] = Field(description="Resultado da cultura", default="")
    
    patogeno_envolvido: Optional[str] = Field(description="Patógeno envolvido (gram positivo, gram negativo, anaeróbio, fungo, nÃO informado, cultura negativa)", default="")

class ParametrosClinicos(BaseModel):
    # Parâmetros para Infecção
    classificacao_infeccao: str = Field(description="Classificação da infecção")
    tax_infeccao: Optional[float] = Field(description="Temperatura axilar (TAX) - Infecção", default="null")
    fc_infeccao: Optional[int] = Field(description="Frequência cardíaca (FC) - Infecção", default="null")
    fr_infeccao: Optional[int] = Field(description="Frequência respiratória (FR) - Infecção", default="null")
    sat_o2_infeccao: Optional[float] = Field(description="Saturação de oxigênio (Sat O2) - Infecção", default="null")
    glasgow_infeccao: Optional[int] = Field(description="Escala de Glasgow - Infecção", default="null")
    pas_infeccao: Optional[int] = Field(description="Pressão arterial sistólica (PAS) - Infecção", default="null")
    pad_infeccao: Optional[int] = Field(description="Pressão arterial diastólica (PAD) - Infecção", default="null")
    pam_infeccao: Optional[int] = Field(description="Pressão arterial média (PAM) - Infecção", default="null")
    pvc_infeccao: Optional[float] = Field(description="Pressão venosa central (PVC) - Infecção", default="null")
    diurese_infeccao: Optional[str] = Field(description="Diurese - Infecção", default="null")
    tempo_inicio_atb_infeccao: Optional[str] = Field(description="Tempo de início do antibiótico - Infecção", default="null")
    
    # Parâmetros laboratoriais - Infecção
    tgo_infeccao: Optional[float] = Field(description="TGO - Infecção", default="null")
    tgp_infeccao: Optional[float] = Field(description="TGP - Infecção", default="null")
    bt_infeccao: Optional[float] = Field(description="Bilirrubina total - Infecção", default="null")
    bi_infeccao: Optional[float] = Field(description="Bilirrubina indireta - Infecção", default="null")
    bd_infeccao: Optional[float] = Field(description="Bilirrubina direta - Infecção", default="null")
    ur_infeccao: Optional[float] = Field(description="Ureia - Infecção", default="null")
    cr_infeccao: Optional[float] = Field(description="Creatinina - Infecção", default="null")
    na_infeccao: Optional[float] = Field(description="Sódio - Infecção", default="null")
    k_infeccao: Optional[float] = Field(description="Potássio - Infecção", default="null")
    hb_infeccao: Optional[float] = Field(description="Hemoglobina - Infecção", default="null")
    ht_infeccao: Optional[float] = Field(description="Hematócrito - Infecção", default="null")
    leucocitos_infeccao: Optional[int] = Field(description="Contagem de leucócitos - Infecção", default="null")
    plaquetas_infeccao: Optional[int] = Field(description="Contagem de plaquetas - Infecção", default="null")
    desvio_esquerda_infeccao: bool = Field(description="Desvio à esquerda - Infecção")
    lactato_infeccao: Optional[float] = Field(description="Lactato - Infecção", default="null")

    # Parâmetros para Sepse
    classificacao_sepse: str = Field(description="Classificação da sepse")
    tax_sepse: Optional[float] = Field(description="Temperatura axilar (TAX) - Sepse", default="null")
    fc_sepse: Optional[int] = Field(description="Frequência cardíaca (FC) - Sepse", default="null")
    fr_sepse: Optional[int] = Field(description="Frequência respiratória (FR) - Sepse", default="null")
    sat_o2_sepse: Optional[float] = Field(description="Saturação de oxigênio (Sat O2) - Sepse", default="null")
    glasgow_sepse: Optional[int] = Field(description="Escala de Glasgow - Sepse", default="null")
    pas_sepse: Optional[int] = Field(description="Pressão arterial sistólica (PAS) - Sepse", default="null")
    pad_sepse: Optional[int] = Field(description="Pressão arterial diastólica (PAD) - Sepse", default="null")
    pam_sepse: Optional[int] = Field(description="Pressão arterial média (PAM) - Sepse", default="null")
    pvc_sepse: Optional[float] = Field(description="Pressão venosa central (PVC) - Sepse", default="null")
    diurese_sepse: Optional[str] = Field(description="Diurese - Sepse", default="null")
    tempo_inicio_atb_sepse: Optional[str] = Field(description="Tempo de início do antibiótico - Sepse", default="null")

    # Parâmetros laboratoriais - Sepse
    tgo_sepse: Optional[float] = Field(description="TGO - Sepse", default=None)
    tgp_sepse: Optional[float] = Field(description="TGP - Sepse", default=None)
    bt_sepse: Optional[float] = Field(description="Bilirrubina total - Sepse", default=None)
    bi_sepse: Optional[float] = Field(description="Bilirrubina indireta - Sepse", default=None)
    bd_sepse: Optional[float] = Field(description="Bilirrubina direta - Sepse", default=None)
    ur_sepse: Optional[float] = Field(description="Ureia - Sepse", default=None)
    cr_sepse: Optional[float] = Field(description="Creatinina - Sepse", default=None)
    na_sepse: Optional[float] = Field(description="Sódio - Sepse", default=None)
    k_sepse: Optional[float] = Field(description="Potássio - Sepse", default=None)
    hb_sepse: Optional[float] = Field(description="Hemoglobina - Sepse", default=None)
    ht_sepse: Optional[float] = Field(description="Hematócrito - Sepse", default=None)
    leucocitos_sepse: Optional[int] = Field(description="Contagem de leucócitos - Sepse", default=0)
    plaquetas_sepse: Optional[int] = Field(description="Contagem de plaquetas - Sepse", default=0)
    desvio_esquerda_sepse: bool = Field(description="Desvio à esquerda - Sepse")
    lactato_sepse: Optional[float] = Field(description="Lactato - Sepse", default=None)
    
    # Outros parâmetros - Infecção e Sepse
    oliguria_infeccao: bool = Field(description="Oligúria - Infecção")
    oxigenoterapia_infeccao: bool = Field(description="Oxigenoterapia - Infecção")
    drogas_vasoativas_infeccao: bool = Field(description="Drogas vasoativas - Infecção")
    ventilacao_mecanica_infeccao: bool = Field(description="Ventilação mecânica - Infecção")
    realizacao_culturas_infeccao: bool = Field(description="Realização de culturas - Infecção")

    oliguria_sepse: bool = Field(description="Oligúria - Sepse")
    oxigenoterapia_sepse: bool = Field(description="Oxigenoterapia - Sepse")
    drogas_vasoativas_sepse: bool = Field(description="Drogas vasoativas - Sepse")
    ventilacao_mecanica_sepse: bool = Field(description="Ventilação mecânica - Sepse")
    realizacao_culturas_sepse: bool = Field(description="Realização de culturas - Sepse")

class ComplicacoesClinicas(BaseModel):
    # Complicações e disfunções orgânicas durante a internação
    insuficiencia_cardiaca: bool = Field(description="Insuficiência cardíaca (SIM/NÃO)")
    insuficiencia_hepatica: bool = Field(description="Insuficiência hepática (SIM/NÃO)")
    lesao_renal_aguda: bool = Field(description="Lesão renal aguda (SIM/NÃO)")
    oliguria: bool = Field(description="Oligúria (SIM/NÃO)")
    insuficiencia_respiratoria: bool = Field(description="Insuficiência respiratória (SIM/NÃO)")
    coagulopatia_civd: bool = Field(description="Coagulação intravascular disseminada/Coagulopatia (SIM/NÃO)")
    alteracao_nivel_consciencia: bool = Field(description="Alteração no nível de consciência (SIM/NÃO)")
    
    # Complicações adicionais
    tromboembolismo_pulmonar: bool = Field(description="Tromboembolismo pulmonar (SIM/NÃO)")
    uso_hemoderivados: bool = Field(description="Uso de hemoderivados (SIM/NÃO)")
    necessidade_uti: bool = Field(description="Necessidade de internação em UTI (SIM/NÃO)")
    drogas_vasoativas: bool = Field(description="Uso de drogas vasoativas (SIM/NÃO)")
    ventilacao_mecanica: bool = Field(description="Ventilação mecânica (SIM/NÃO)")
    choque_septico: bool = Field(description="Choque séptico (SIM/NÃO)")
    
    # Descrição de outras complicações
    outra_complicacao_descritiva: Optional[str] = Field(description="Descrição de outra complicação/disfunção orgânica", default="null")

class DesfechosNeonatais(BaseModel):
    # Desfechos neonatais adversos (SIM/NÃO)
    desfechos_neonatais_adversos: bool = Field(description="Desfechos neonatais adversos (SIM/NÃO)")
    
    # Detalhes dos desfechos
    obito_fetal_intrautero: bool = Field(description="Óbito fetal intraútero (SIM/NÃO)")
    obito_neonatal: bool = Field(description="Óbito neonatal (SIM/NÃO)")
    internacao_uti_neonatal: bool = Field(description="Internação em UTI neonatal (SIM/NÃO)")
    apgar_menor_7_5min: bool = Field(description="Apgar menor que 7 no 5º minuto (SIM/NÃO)")
    near_miss_neonatal: bool = Field(description="Near miss neonatal (SIM/NÃO)")
    
    # Critérios de near miss neonatal
    peso_nascimento_menor_1500g: bool = Field(description="Peso ao nascer menor que 1500g (SIM/NÃO)")
    idade_gestacional_menor_30s: bool = Field(description="IG ao nascer menor que 30 semanas (SIM/NÃO)")
    apgar_menor_7_5min_near_miss: bool = Field(description="Apgar menor que 7 no 5º minuto no critério de near miss (SIM/NÃO)")
    
    # Outros campos adicionais
    outra_complicacao_neonatal: Optional[str] = Field(description="Descrição de outra complicação neonatal", default="null")

class CriteriosNearMissMaterno(BaseModel):
    nmm_disfuncao_cardiovascular: bool = Field (description="Disfunção cardiovascular: SIM ou NÃO")
    nmm_disfuncao_respiratoria: bool = Field (description="Disfunção respiratória: SIM ou NÃO")
    nmm_disfuncao_renal: bool = Field (description="Disfunção renal: SIM ou NÃO")
    nmm_disfuncao_hematologica: bool = Field (description="Disfunção hematológica: SIM ou NÃO")
    nmm_disfuncao_hepatica: bool = Field (description="Disfunção hepática: SIM ou NÃO")
    nmm_disfuncao_neurologica: bool = Field (description="Disfunção neurológica: SIM ou NÃO")
    nmm_disfuncao_uterina: bool = Field (description="Disfunção uterina: SIM ou NÃO")

class EscoresInfec(BaseModel):
    SIRS: int = Field( description="Pontuação SIRS no diagnóstico da infecção", default=0)
    SOFA: int = Field( description="Pontuação SOFA no diagnóstico da infecção", default=0)
    qSOFA: int = Field( description="Pontuação qSOFA no diagnóstico da infecção", default=0)
    omSOFA: int = Field( description="Pontuação omSOFA no diagnóstico da infecção", default=0)
    omqSOFA: int = Field( description="Pontuação omqSOFA no diagnóstico da infecção", default=0)
    SOS: int = Field( description="Pontuação SOS no diagnóstico da infecção", default=0)
    MEWS: int = Field( description="Pontuação MEWS no diagnóstico da infecção", default=0)
    APACHE2: int = Field( description="Pontuação APACHE2 no diagnóstico da infecção", default=0)
    SAPS3: int = Field( description="Pontuação SAPS3 no diagnóstico da infecção", default=0)
    MODS: int = Field( description="Pontuação MODS no diagnóstico da infecção", default=0)
    
class EscoresSepse(BaseModel):
    SIRS: int = Field( description="Pontuação SIRS observada na sepse", default=0)
    SOFA: int = Field( description="Pontuação SOFA observada na sepse", default=0)
    qSOFA: int = Field( description="Pontuação qSOFA observada na sepse", default=0)
    omSOFA: int = Field( description="Pontuação omSOFA observada na sepse", default=0)
    omqSOFA: int = Field( description="Pontuação omqSOFA observada na sepse", default=0)
    SOS: int = Field( description="Pontuação SOS observada na sepse", default=0)
    MEWS: int = Field( description="Pontuação MEWS observada na sepse", default=0)
    APACHE2: int = Field( description="Pontuação APACHE2 observada na sepse", default=0)
    SAPS3: int = Field( description="Pontuação SAPS3 observada na sepse", default=0)
    MODS: int = Field( description="Pontuação MODS observada na sepse", default=0)
    
class PatienteData(BaseModel):
    hospital_stay_days: int = Field( description="Dias de internação no hospital")
    icu_stay_days: int = Field( description="Dias de internação na UTI")

class Desfechos(BaseModel):
    diagnóstico_sepse_desfecho: bool = Field( description="Diagnóstico de sepse no desfecho")
    Internação_UTI_desfecho: bool = Field( description="Internação em UTI no desfecho")
    Choque_septico_desfecho: bool = Field( description="Choque séptico no desfecho")
    Desfecho_materno_adverso_desfecho: bool = Field( description="Desfecho materno adverso no desfecho")
    Desfecho_neonatal_adverso_desfecho: bool = Field( description="Desfecho neonatal adverso no desfecho")
    Algum_near_miss_materno_desfecho: bool = Field( description="Algum near miss materno no desfecho")
    Óbito_materno_desfecho: bool = Field( description="Óbito materno no desfecho")
    Causa_do_óbito_descritivo: str = Field( description="Causa do óbito descritiva")
    Causa_do_óbito_categorizada: str = Field( description="Causa do óbito categorizada")
    Data_alta_óbito: str = Field( description="Data de alta ou óbito")
    Resposável_iniciar_coleta: str = Field( description="Responsável por iniciar a coleta")
    Responsável_finalizar_coleta: str = Field( description="Responsável por finalizar a coleta")
    Responsável_1_digitação: str = Field( description="Responsável pela primeira digitação")
    Responsável_2_digitação: str = Field( description="Responsável pela segunda digitação")
    Data_1_digitação: str = Field( description="Data da primeira digitação")
    Data_2_digitação: str = Field( description="Data da segunda digitação")

class FormDoc(BaseModel):
    identificacao: Identificacao = Field(description="1. DADOS DA PESQUISA/IDENTIFICAÇÃO")
    dados_gerais: DadosGerais = Field(description="2. DADOS GERAIS")
    comorbidades: Comorbidades = Field(description="COMORBIDADES")
    habitos_de_vida: HabitosDeVida = Field(description="HÁBITOS DE VIDA")
    dados_obstetricos: DadosObstetricos = Field(description="3. DADOS OBSTÉTRICOS")
    complicacoes_obstetricas: ComplicacoesObstetricas = Field(description="complicações obstetricas:")
    dados_infeccao: DadosInfeccao = Field(description="4. DADOS RELACIONADOS A INFECÇÃO")
    parametros_clinicos: ParametrosClinicos = Field(description="5. PARÂMETROS CLÍNICOS E LABORATORIAIS NO MOMENTO DA ADMISSÃO OU DIAGNÓSTICO DA INFECCAO E NO MOMENTO DO DIAGNOSTICO")
    complicacoes_clinicas: ComplicacoesClinicas = Field (description="6. COMPLICAÇÕES CLÍNICAS E/OU DISFUNÇÕES ORGÂNICAS DURANTE A INTERNACAO")
    desfechos_neonatais: DesfechosNeonatais = Field(description="7. DESFECHOS NEONATAIS")
    criterios_near_miss_materno: CriteriosNearMissMaterno = Field(description="8. CRITÉRIOS DE NEAR MISS MATERNO")
    escores_infec: EscoresInfec = Field(description="(DIREITA)9. ESCORES DE DIAGNOSTICO E/OU PROGNOSTICO EM PACIEENTES COM SEPSE, CALCULADOS A PARTIR DOS DADOS CLINICOS E LABORATORIAIS NA INTERNAÇÃO (OU PRIMEIRAS 24 HORAS) E NO DIAGNOSTICO DE SEPSE")
    escores_sepse: EscoresSepse = Field(description="(ESQUERDA)9. ESCORES DE DIAGNOSTICO E/OU PROGNOSTICO EM PACIEENTES COM SEPSE, CALCULADOS A PARTIR DOS DADOS CLINICOS E LABORATORIAIS NA INTERNAÇÃO (OU PRIMEIRAS 24 HORAS) E NO DIAGNOSTICO DE SEPSE") 
    patiente_data: PatienteData = Field(description="TEMPO DE INTERNAÇÃO EM HOSPITAL E UTI")
    desfechos: Desfechos = Field(description="DESFECHOS")

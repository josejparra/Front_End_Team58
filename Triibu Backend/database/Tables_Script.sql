    -- Table: public.tb_ICA_declara

-- DROP TABLE public."tb_ICA_declara";

CREATE TABLE IF NOT EXISTS public."tb_ICA_declara"
(
    cod_establecimiento integer NOT NULL,
    cc_nit bigint,
    des_propietario character varying(300) COLLATE pg_catalog."default",
    des_establecimiento character varying(300) COLLATE pg_catalog."default",
    cod_clase character varying(3) COLLATE pg_catalog."default",
    cod_act_economica integer,
    des_act_economica character varying(300) COLLATE pg_catalog."default",
    cod_naturaleza character varying(3) COLLATE pg_catalog."default",
    vlr_ingreso_gravable bigint,
    vlr_ica bigint,
    vlr_avisos bigint,
    vlr_retenciones bigint,
    vlr_autoretenciones bigint,
    vlr_sancion bigint,
    vlr_intereses bigint,
    vlr_generacion_energia bigint,
    vlr_sucursales bigint,
    vlr_exoneraciones bigint,
    vlr_anticipo_anio_anterior bigint,
    vlr_anticipo_anio_siguiente bigint,
    vlr_saldo_a_favor bigint,
    vlr_ingresos_brutos bigint,
    vlr_ingresos_brutos_fuera bigint,
    vlr_devoluciones bigint,
    vlr_exportaciones bigint,
    vlr_activos_fijos bigint,
    vlr_act_excluidas bigint,
    vlr_ingreso_act_exenta bigint,
    anio character varying(5) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "tb_ICA_declara_pkey" PRIMARY KEY (anio, cod_establecimiento)
)

TABLESPACE pg_default;

-- Table: public.tb_ICA_pagos

-- DROP TABLE public."tb_ICA_pagos";

CREATE TABLE IF NOT EXISTS public."tb_ICA_pagos"
(
    cod_establecimiento integer NOT NULL,
    cc_nit bigint,
    des_nombre character varying(300) COLLATE pg_catalog."default",
    cod_factura bigint,
    vlr_factura bigint,
    fecha_ingreso_pago timestamp without time zone,
    periodo_ultimo_pago character varying(10) COLLATE pg_catalog."default",
    periodo_liquido character varying(10) COLLATE pg_catalog."default",
    cod_estado character varying(3) COLLATE pg_catalog."default",
    anio character varying(5) COLLATE pg_catalog."default" NOT NULL
)

TABLESPACE pg_default;

-- Table: public.tb_predial_facturas

-- DROP TABLE public.tb_predial_facturas;

CREATE TABLE IF NOT EXISTS public.tb_predial_facturas
(
    id_catastral character varying(100) COLLATE pg_catalog."default",
    tarifa smallint,
    cod_estrato smallint,
    cod_predial integer,
    cod_clase smallint,
    cod_corregimiento smallint,
    cod_barrio smallint,
    cod_manzana smallint,
    cod_predio smallint,
    cod_edificio smallint,
    cod_mejora smallint,
    cod_ficha bigint,
    cod_circulo character varying(10) COLLATE pg_catalog."default",
    cod_matricula character varying(10) COLLATE pg_catalog."default",
    direccion character varying(300) COLLATE pg_catalog."default",
    area_terr real,
    area_terr_comun real,
    area_const real,
    area_const_comun real,
    cod_destinacion smallint,
    vlr_terr bigint,
    vlr_terr_comun bigint,
    vlr_const bigint,
    vlr_const_comun bigint,
    vlr_tot_avaluo bigint,
    id_doc_catastral character varying(300) COLLATE pg_catalog."default",
    des_nombre character varying(300) COLLATE pg_catalog."default",
    des_primer_apellido character varying(300) COLLATE pg_catalog."default",
    des_segundo_apellido character varying(300) COLLATE pg_catalog."default",
    proindiviso real,
    cons_pred integer,
    periodo_ultimo_pago character varying(10) COLLATE pg_catalog."default",
    anio character varying(5) COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

-- Table: public.tb_predial_facturas_2016_2020

-- DROP TABLE public.tb_predial_facturas_2016_2020;

CREATE TABLE IF NOT EXISTS public.tb_predial_facturas_2016_2020
(
    tarifa smallint,
    cod_estrato smallint,
    cod_barrio smallint,
    cod_ficha bigint,
    cod_matricula character varying(10) COLLATE pg_catalog."default",
    area_terr real,
    area_terr_comun real,
    area_const real,
    area_const_comun real,
    vlr_terr bigint,
    vlr_terr_comun bigint,
    vlr_const bigint,
    vlr_const_comun bigint,
    vlr_tot_avaluo bigint,
    id_doc_catastral character varying(300) COLLATE pg_catalog."default",
    des_nombre character varying(300) COLLATE pg_catalog."default",
    proindiviso real,
    vlr_aval_proindiviso bigint,
    vlr_impuesto bigint,
    vlr_imp_ambiental bigint,
    vlr_imp_bomberil bigint,
    vlr_total bigint,
    anio character varying(5) COLLATE pg_catalog."default",
    periodo_ultimo_pago character varying(10) COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

-- Table: public.tb_predial_pagos

-- DROP TABLE public.tb_predial_pagos;

CREATE TABLE IF NOT EXISTS public.tb_predial_pagos
(
    anio character varying(5) COLLATE pg_catalog."default",
    cons_pred integer,
    tipo_factura character varying(5) COLLATE pg_catalog."default",
    nudos character varying(5) COLLATE pg_catalog."default",
    cons_modulo integer,
    vlr_factura bigint,
    fecha_ingreso_pago timestamp without time zone,
    sitio_pago character varying(30) COLLATE pg_catalog."default",
    cod_estado character varying(5) COLLATE pg_catalog."default",
    cc_nit character varying(30) COLLATE pg_catalog."default",
    des_nombre character varying(300) COLLATE pg_catalog."default",
    id_catastral character varying(30) COLLATE pg_catalog."default",
    proindiviso real,
    periodo_liquidado character varying(10) COLLATE pg_catalog."default",
    periodo_ultimo_pago character varying(10) COLLATE pg_catalog."default",
    acuerdo_pago character varying(5) COLLATE pg_catalog."default",
    vlr_otro_concepto bigint,
    nvc smallint,
    usuario character varying(30) COLLATE pg_catalog."default",
    cod_factura bigint
)

TABLESPACE pg_default;
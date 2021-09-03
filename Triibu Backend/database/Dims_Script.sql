-- Table: public.dim_estructura_CIIU

-- DROP TABLE public."dim_estructura_CIIU";

CREATE TABLE IF NOT EXISTS public."dim_estructura_CIIU"
(
    id integer NOT NULL DEFAULT nextval('"dim_estructura_CIIU_id_seq"'::regclass),
    cod_seccion character varying COLLATE pg_catalog."default" NOT NULL,
    cod_division smallint,
    cod_grupo smallint,
    cod_clase smallint,
    descripcion character varying(300) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "dim_estructura_CIIU_pkey" PRIMARY KEY (id)
)

TABLESPACE pg_default;

-- Table: public.ica_clase

-- DROP TABLE public.ica_clase;

CREATE TABLE IF NOT EXISTS public.ica_clase
(
    cod_clase character varying COLLATE pg_catalog."default" NOT NULL,
    des_clase character varying COLLATE pg_catalog."default",
    CONSTRAINT ica_clase_pkey PRIMARY KEY (cod_clase)
)

TABLESPACE pg_default;

-- Table: public.predial_barrios

-- DROP TABLE public.predial_barrios;

CREATE TABLE IF NOT EXISTS public.predial_barrios
(
    cod_barrio smallint NOT NULL,
    des_barrio character varying COLLATE pg_catalog."default",
    des_sub_barrios character varying COLLATE pg_catalog."default",
    CONSTRAINT predial_barrios_pkey PRIMARY KEY (cod_barrio)
)

TABLESPACE pg_default;

-- Table: public.predial_destinaciones

-- DROP TABLE public.predial_destinaciones;

CREATE TABLE IF NOT EXISTS public.predial_destinaciones
(
    cod_destinacion smallint NOT NULL,
    des_destinacion character varying COLLATE pg_catalog."default",
    CONSTRAINT predial_destinaciones_pkey PRIMARY KEY (cod_destinacion)
)

TABLESPACE pg_default;

-- Table: public.predial_veredas

-- DROP TABLE public.predial_veredas;

CREATE TABLE IF NOT EXISTS public.predial_veredas
(
    cod_veredas smallint NOT NULL,
    des_veredas character varying COLLATE pg_catalog."default",
    CONSTRAINT predial_veredas_pkey PRIMARY KEY (cod_veredas)
)

TABLESPACE pg_default;
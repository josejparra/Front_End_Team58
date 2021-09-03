-- View: public.vw_ica_declara

-- DROP MATERIALIZED VIEW public.vw_ica_declara;

CREATE MATERIALIZED VIEW public.vw_ica_declara
TABLESPACE pg_default
AS
 SELECT a.cc_nit,
    a.des_establecimiento,
    a.vlr_ingreso_gravable,
        CASE
            WHEN a.cod_naturaleza::text = 'N'::text THEN 'Persona Natural'::character varying
            WHEN a.cod_naturaleza::text = 'J'::text THEN 'Persona Juridica'::character varying
            ELSE a.cod_naturaleza
        END AS des_naturaleza,
    COALESCE(b.cod_seccion, '0'::character varying) AS cod_seccion,
    upper(COALESCE(d.descripcion, 'NO DISPONIBLE'::character varying)::text) AS des_act_economica,
    c.des_clase,
    a.vlr_ica,
    a.anio
   FROM "tb_ICA_declara" a
     LEFT JOIN "dim_estructura_CIIU" b ON a.cod_act_economica = b.cod_clase
     LEFT JOIN "dim_estructura_CIIU" d ON b.cod_seccion::text = d.cod_seccion::text AND d.cod_division IS NULL
     LEFT JOIN ica_clase c ON a.cod_clase::text = c.cod_clase::text
WITH DATA;

-- View: public.vw_predial_declara

-- DROP MATERIALIZED VIEW public.vw_predial_declara;

CREATE MATERIALIZED VIEW public.vw_predial_declara
TABLESPACE pg_default
AS
 SELECT tb_predial_facturas_2016_2020.tarifa,
    tb_predial_facturas_2016_2020.cod_estrato,
    tb_predial_facturas_2016_2020.des_nombre AS des_propietario,
    tb_predial_facturas_2016_2020.area_terr,
    tb_predial_facturas_2016_2020.area_const,
    tb_predial_facturas_2016_2020.vlr_tot_avaluo,
    tb_predial_facturas_2016_2020.vlr_total,
    tb_predial_facturas_2016_2020.id_doc_catastral AS id_doc,
    tb_predial_facturas_2016_2020.anio::integer AS anio
   FROM tb_predial_facturas_2016_2020
  GROUP BY tb_predial_facturas_2016_2020.tarifa, tb_predial_facturas_2016_2020.cod_estrato, tb_predial_facturas_2016_2020.des_nombre, tb_predial_facturas_2016_2020.area_terr, tb_predial_facturas_2016_2020.area_const, tb_predial_facturas_2016_2020.vlr_tot_avaluo, tb_predial_facturas_2016_2020.vlr_total, tb_predial_facturas_2016_2020.id_doc_catastral, tb_predial_facturas_2016_2020.anio
WITH DATA;

-- View: public.vw_value_predial_ica

-- DROP MATERIALIZED VIEW public.vw_value_predial_ica;

CREATE MATERIALIZED VIEW public.vw_value_predial_ica
TABLESPACE pg_default
AS
 SELECT a.anio,
    a.predial,
    b.ica
   FROM ( SELECT tb_predial_pagos.anio,
            sum(tb_predial_pagos.vlr_factura) AS predial
           FROM tb_predial_pagos
          GROUP BY tb_predial_pagos.anio) a
     LEFT JOIN ( SELECT "tb_ICA_pagos".anio,
            sum("tb_ICA_pagos".vlr_factura) AS ica
           FROM "tb_ICA_pagos"
          GROUP BY "tb_ICA_pagos".anio) b ON a.anio::text = b.anio::text
  WHERE a.anio::integer >= (((( SELECT max(tb_predial_pagos.anio::text) AS max
           FROM tb_predial_pagos))::integer) - 5)
WITH DATA;
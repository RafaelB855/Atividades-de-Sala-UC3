PGDMP                         {            ClickMed    15.2    15.2 (    /           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            0           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            1           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            2           1262    49570    ClickMed    DATABASE     �   CREATE DATABASE "ClickMed" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Portuguese_Brazil.1252';
    DROP DATABASE "ClickMed";
                postgres    false            �            1259    49633    Atendimento    TABLE     �  CREATE TABLE public."Atendimento" (
    "ID" integer NOT NULL,
    "ID_Paciente" integer NOT NULL,
    "Sintomas1" integer NOT NULL,
    "Intensidade1" integer DEFAULT 1,
    "Sintomas2" integer,
    "Intensidade2" integer DEFAULT 0,
    "Sintomas3" integer,
    "Intensidade3" integer DEFAULT 0,
    "Sintomas4" integer,
    "Intensidade4" integer DEFAULT 0,
    "Doença" integer
);
 !   DROP TABLE public."Atendimento";
       public         heap    postgres    false            �            1259    49632    Atendimento_ID_seq    SEQUENCE     �   ALTER TABLE public."Atendimento" ALTER COLUMN "ID" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Atendimento_ID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    223            �            1259    49602    Doenças    TABLE     '  CREATE TABLE public."Doenças" (
    "ID" integer NOT NULL,
    "Nome" character varying(255) NOT NULL,
    "Sintomas1" integer NOT NULL,
    "Sintomas2" integer,
    "Sintomas3" integer,
    "Sintomas4" integer,
    "Remédio" character varying(255),
    "Tratamento" character varying(255)
);
    DROP TABLE public."Doenças";
       public         heap    postgres    false            �            1259    49601    Doenças_ID_seq    SEQUENCE     �   ALTER TABLE public."Doenças" ALTER COLUMN "ID" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Doenças_ID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    221            �            1259    49583    Login    TABLE     �   CREATE TABLE public."Login" (
    "ID" integer NOT NULL,
    "Username" character varying(255) NOT NULL,
    "Password" character varying(255) NOT NULL,
    "Email" character varying(255) NOT NULL,
    "ID_Paciente" integer NOT NULL
);
    DROP TABLE public."Login";
       public         heap    postgres    false            �            1259    49582    Login_ID_seq    SEQUENCE     �   ALTER TABLE public."Login" ALTER COLUMN "ID" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Login_ID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    217            �            1259    49572 	   Pacientes    TABLE     j  CREATE TABLE public."Pacientes" (
    "ID" integer NOT NULL,
    "Nome" character varying(255) NOT NULL,
    "CPF" integer NOT NULL,
    "Nascimento" character varying(255) DEFAULT 'Não Informado'::character varying NOT NULL,
    "Cep" integer DEFAULT 0 NOT NULL,
    "Complemento" character varying(255) DEFAULT 'Não Informado'::character varying NOT NULL
);
    DROP TABLE public."Pacientes";
       public         heap    postgres    false            �            1259    49571    Pacientes_ID_seq    SEQUENCE     �   ALTER TABLE public."Pacientes" ALTER COLUMN "ID" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Pacientes_ID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    215            �            1259    49596    Sintomas    TABLE     j   CREATE TABLE public."Sintomas" (
    "ID" integer NOT NULL,
    "Nome" character varying(255) NOT NULL
);
    DROP TABLE public."Sintomas";
       public         heap    postgres    false            �            1259    49595    Sintomas_ID_seq    SEQUENCE     �   ALTER TABLE public."Sintomas" ALTER COLUMN "ID" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Sintomas_ID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    219            ,          0    49633    Atendimento 
   TABLE DATA           �   COPY public."Atendimento" ("ID", "ID_Paciente", "Sintomas1", "Intensidade1", "Sintomas2", "Intensidade2", "Sintomas3", "Intensidade3", "Sintomas4", "Intensidade4", "Doença") FROM stdin;
    public          postgres    false    223   !2       *          0    49602    Doenças 
   TABLE DATA           �   COPY public."Doenças" ("ID", "Nome", "Sintomas1", "Sintomas2", "Sintomas3", "Sintomas4", "Remédio", "Tratamento") FROM stdin;
    public          postgres    false    221   K2       &          0    49583    Login 
   TABLE DATA           W   COPY public."Login" ("ID", "Username", "Password", "Email", "ID_Paciente") FROM stdin;
    public          postgres    false    217   �2       $          0    49572 	   Pacientes 
   TABLE DATA           ^   COPY public."Pacientes" ("ID", "Nome", "CPF", "Nascimento", "Cep", "Complemento") FROM stdin;
    public          postgres    false    215   �2       (          0    49596    Sintomas 
   TABLE DATA           2   COPY public."Sintomas" ("ID", "Nome") FROM stdin;
    public          postgres    false    219   '3       3           0    0    Atendimento_ID_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public."Atendimento_ID_seq"', 13, true);
          public          postgres    false    222            4           0    0    Doenças_ID_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public."Doenças_ID_seq"', 4, true);
          public          postgres    false    220            5           0    0    Login_ID_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public."Login_ID_seq"', 2, true);
          public          postgres    false    216            6           0    0    Pacientes_ID_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public."Pacientes_ID_seq"', 2, true);
          public          postgres    false    214            7           0    0    Sintomas_ID_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public."Sintomas_ID_seq"', 7, true);
          public          postgres    false    218            �           2606    49644    Atendimento Atendimento_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public."Atendimento"
    ADD CONSTRAINT "Atendimento_pkey" PRIMARY KEY ("ID");
 J   ALTER TABLE ONLY public."Atendimento" DROP CONSTRAINT "Atendimento_pkey";
       public            postgres    false    223            �           2606    49611    Doenças Doenças_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public."Doenças"
    ADD CONSTRAINT "Doenças_pkey" PRIMARY KEY ("ID");
 D   ALTER TABLE ONLY public."Doenças" DROP CONSTRAINT "Doenças_pkey";
       public            postgres    false    221            �           2606    49589    Login Login_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public."Login"
    ADD CONSTRAINT "Login_pkey" PRIMARY KEY ("ID");
 >   ALTER TABLE ONLY public."Login" DROP CONSTRAINT "Login_pkey";
       public            postgres    false    217            �           2606    49581    Pacientes Pacientes_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public."Pacientes"
    ADD CONSTRAINT "Pacientes_pkey" PRIMARY KEY ("ID");
 F   ALTER TABLE ONLY public."Pacientes" DROP CONSTRAINT "Pacientes_pkey";
       public            postgres    false    215            �           2606    49600    Sintomas Sintomas_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public."Sintomas"
    ADD CONSTRAINT "Sintomas_pkey" PRIMARY KEY ("ID");
 D   ALTER TABLE ONLY public."Sintomas" DROP CONSTRAINT "Sintomas_pkey";
       public            postgres    false    219            �           2606    49670    Atendimento fk_doença    FK CONSTRAINT     �   ALTER TABLE ONLY public."Atendimento"
    ADD CONSTRAINT "fk_doença" FOREIGN KEY ("Doença") REFERENCES public."Doenças"("ID");
 D   ALTER TABLE ONLY public."Atendimento" DROP CONSTRAINT "fk_doença";
       public          postgres    false    3207    221    223            �           2606    49590    Login fk_id_paciente    FK CONSTRAINT     �   ALTER TABLE ONLY public."Login"
    ADD CONSTRAINT fk_id_paciente FOREIGN KEY ("ID_Paciente") REFERENCES public."Pacientes"("ID");
 @   ALTER TABLE ONLY public."Login" DROP CONSTRAINT fk_id_paciente;
       public          postgres    false    3201    215    217            �           2606    49645    Atendimento fk_id_paciente    FK CONSTRAINT     �   ALTER TABLE ONLY public."Atendimento"
    ADD CONSTRAINT fk_id_paciente FOREIGN KEY ("ID_Paciente") REFERENCES public."Pacientes"("ID");
 F   ALTER TABLE ONLY public."Atendimento" DROP CONSTRAINT fk_id_paciente;
       public          postgres    false    223    3201    215            �           2606    49612    Doenças fk_sintomas1    FK CONSTRAINT     �   ALTER TABLE ONLY public."Doenças"
    ADD CONSTRAINT fk_sintomas1 FOREIGN KEY ("Sintomas1") REFERENCES public."Sintomas"("ID");
 A   ALTER TABLE ONLY public."Doenças" DROP CONSTRAINT fk_sintomas1;
       public          postgres    false    3205    221    219            �           2606    49650    Atendimento fk_sintomas1    FK CONSTRAINT     �   ALTER TABLE ONLY public."Atendimento"
    ADD CONSTRAINT fk_sintomas1 FOREIGN KEY ("Sintomas1") REFERENCES public."Sintomas"("ID");
 D   ALTER TABLE ONLY public."Atendimento" DROP CONSTRAINT fk_sintomas1;
       public          postgres    false    3205    219    223            �           2606    49617    Doenças fk_sintomas2    FK CONSTRAINT     �   ALTER TABLE ONLY public."Doenças"
    ADD CONSTRAINT fk_sintomas2 FOREIGN KEY ("Sintomas2") REFERENCES public."Sintomas"("ID");
 A   ALTER TABLE ONLY public."Doenças" DROP CONSTRAINT fk_sintomas2;
       public          postgres    false    219    221    3205            �           2606    49655    Atendimento fk_sintomas2    FK CONSTRAINT     �   ALTER TABLE ONLY public."Atendimento"
    ADD CONSTRAINT fk_sintomas2 FOREIGN KEY ("Sintomas2") REFERENCES public."Sintomas"("ID");
 D   ALTER TABLE ONLY public."Atendimento" DROP CONSTRAINT fk_sintomas2;
       public          postgres    false    223    3205    219            �           2606    49622    Doenças fk_sintomas3    FK CONSTRAINT     �   ALTER TABLE ONLY public."Doenças"
    ADD CONSTRAINT fk_sintomas3 FOREIGN KEY ("Sintomas3") REFERENCES public."Sintomas"("ID");
 A   ALTER TABLE ONLY public."Doenças" DROP CONSTRAINT fk_sintomas3;
       public          postgres    false    3205    221    219            �           2606    49660    Atendimento fk_sintomas3    FK CONSTRAINT     �   ALTER TABLE ONLY public."Atendimento"
    ADD CONSTRAINT fk_sintomas3 FOREIGN KEY ("Sintomas3") REFERENCES public."Sintomas"("ID");
 D   ALTER TABLE ONLY public."Atendimento" DROP CONSTRAINT fk_sintomas3;
       public          postgres    false    223    3205    219            �           2606    49627    Doenças fk_sintomas4    FK CONSTRAINT     �   ALTER TABLE ONLY public."Doenças"
    ADD CONSTRAINT fk_sintomas4 FOREIGN KEY ("Sintomas4") REFERENCES public."Sintomas"("ID");
 A   ALTER TABLE ONLY public."Doenças" DROP CONSTRAINT fk_sintomas4;
       public          postgres    false    219    3205    221            �           2606    49665    Atendimento fk_sintomas4    FK CONSTRAINT     �   ALTER TABLE ONLY public."Atendimento"
    ADD CONSTRAINT fk_sintomas4 FOREIGN KEY ("Sintomas4") REFERENCES public."Sintomas"("ID");
 D   ALTER TABLE ONLY public."Atendimento" DROP CONSTRAINT fk_sintomas4;
       public          postgres    false    219    3205    223            ,      x�34�4�?N$+F��� N��      *   -   x�3�t/�,H�4�4�4�4��".�t��!P, G\1z\\\ A��      &   4   x�3�,JLK4@&�s3s���s9��8�SJ��kJbq
��W� ��      $   K   x��)�@@=y9H�6��1[(,������=�4���S-4�@'��TK`���Lx�������&�""���      (   X   x�3�t�/RHIUpNLJ=�<�ˈ3$��8��&��X���W��e�閘����e�閚T��e��wxaiqj"�9�KfbQQjf"W� ��      
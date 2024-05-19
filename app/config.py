class Settings:
    EMBRAPA_URLS = {
        "production": "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02",
        "processing": "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03",
        "commercialization": "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04",
        "importation": "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05",
        "exportation": "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06",
    }
    JWT_SECRET_KEY = "fiap_secret_key_challenge_1"
settings = Settings()

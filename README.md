# TPP - como levantar la arquitectura base
1. Compilar y levantar todo el stack
```bash
docker compose up -d --build
```

2. Verificar que los contenedores estén activos
```bash
docker compose ps
```

3. Monitorear los registros de ejecución
```bash
# Ver el estado general de todos los servicios
docker compose logs -f

# Ver únicamente los logs del backend o frontend
docker compose logs -f backend
```

4. Probar los componentes en el navegador

- **App Web Principal (React + Nginx + FastAPI):** http://localhost:3000 (Al recargar la página, verás incrementar el contador de visitas guardado en Redis y la conexión exitosa a Postgres).
- **API Backend (Swagger Docs):** http://localhost:8000/docs
- **Prometheus:** http://localhost:9090
- **cAdvisor:** http://localhost:8080
- **Grafana:** http://localhost:3001 (Usuario: admin | Password: admin)
- **SonarQube:** http://localhost:9000 (Usuario: admin | Password: admin — suele demorar ~60 segundos en iniciar).

5. Detener el entorno
```bash
# Apaga los servicios manteniendo los datos persistidos en PostgreSQL
docker compose down

# Apaga los servicios y limpia completamente los volúmenes de datos
docker compose down -v
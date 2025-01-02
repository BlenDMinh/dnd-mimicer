# Mimicer - DnD Utility Bot for Discord
## How to run?
For now the **API Server** and its **Database** can be deployed using Docker
```bash
docker compose up -d
```
**Admin Client** is using Vitejs and can be run by `yarn run dev` for develop or `yarn run build` and `yarn run start` to run in production mode.

**Discord Bot Server** is currently not implemented in Docker Compose, run it by calling `main.py` file: `py main.py`

import axios from 'axios';
import loadConfig from '../config/env.config';

loadConfig();

const discordAxios = axios.create({
  baseURL: process.env.DISCORD_API_URL,
  headers: {
    Authorization: `Bot ${process.env.DISCORD_BOT_TOKEN}`,
    'Content-Type': 'application/json',
  },
});

export default discordAxios;

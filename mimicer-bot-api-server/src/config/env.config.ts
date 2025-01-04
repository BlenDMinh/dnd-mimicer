import path from 'path';
import Joi from 'joi';
import dotenv from 'dotenv';

export default function loadConfig(): void {
  const envPath = path.join(__dirname, '..', '..', '.env');

  const result = dotenv.config({ path: envPath });

  if (result.error) {
    throw new Error(
      `Failed to load .env file from path ${envPath}: ${result.error.message}`,
    );
  }

  const schema = Joi.object({
    NODE_ENV: Joi.string()
      .valid('development', 'testing', 'production')
      .required(),
    LOG_LEVEL: Joi.string()
      .valid('debug', 'info', 'warn', 'error', 'fatal')
      .required(),
    API_PORT: Joi.number().required(),
    API_HOST: Joi.string().required(),
    DISCORD_BOT_TOKEN: Joi.string().required(),
    DISCORD_API_URL: Joi.string().required(),
    ANNOUCEMENT_CHANNEL_ID: Joi.string().required(),
    CAMPAIGN_CHANNEL_ID: Joi.string().required(),
  }).unknown(true);

  const { error } = schema.validate(process.env, { abortEarly: false });

  if (error) {
    throw new Error(`Config validation error: ${error.message}`);
  }
}

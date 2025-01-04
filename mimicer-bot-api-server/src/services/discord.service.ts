import discordAxios from '../axios/discord.axios';
import loadConfig from '../config/env.config';

loadConfig();

const discordService = {
  async sendMessage(
    channelId: string,
    content?: string,
    embeds?: Record<string, unknown>,
    messageId = null,
  ): Promise<void> {
    if (messageId) {
      return discordAxios.patch(`channels/${channelId}/messages/${messageId}`, {
        content: content ?? '',
        embeds: embeds ?? [],
      });
    }
    return discordAxios.post(`channels/${channelId}/messages`, {
      content: content ?? '',
      embeds: embeds ?? [],
    });
  },
  async sendAnnoucementMessage(
    content?: string,
    embeds?: Record<string, unknown>,
    messageId = null,
  ): Promise<void> {
    return this.sendMessage(
      process.env.ANNOUCEMENT_CHANNEL_ID,
      content,
      embeds,
      messageId,
    );
  },

  async sendCampaignMessage(
    content?: string,
    embeds?: Record<string, unknown>,
    messageId = null,
  ): Promise<void> {
    return this.sendMessage(
      process.env.CAMPAIGN_CHANNEL_ID,
      content,
      embeds,
      messageId,
    );
  },
};

export default discordService;

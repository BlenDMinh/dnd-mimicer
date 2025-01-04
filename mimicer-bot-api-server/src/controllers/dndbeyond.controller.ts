import { FastifyReply, FastifyRequest } from 'fastify';
import discordService from '../services/discord.service'; // Ensure to import your discord service

interface DiceRollData {
  id: string;
  name: string;
  action: string;
  roll: string;
}

// In-memory storage for roll history
let rollHistory: { name: string; action: string; roll: string }[] = [];

const dndbeyondController = {
  trackDiceRoll(
    request: FastifyRequest<{ Body: DiceRollData }>,
    reply: FastifyReply,
  ) {
    const { name, action, roll } = request.body;

    // Add the roll to history, limit to the latest 5 rolls
    rollHistory.push({ name, action, roll });
    if (rollHistory.length > 5) {
      rollHistory.shift(); // Remove the oldest roll if history exceeds 5
    }

    // If the action is Initiative: roll, update the initiative value for each character
    if (action === 'Initiative: roll') {
      // Here, you might want to update your initiative display accordingly
      // For example, you can store the initiative rolls in an object
      const initiativeRolls = rollHistory.filter(
        (r) => r.action === 'Initiative: roll',
      );

      // Construct a message for initiative display
      let initiativeMessage = 'Initiative Rolls:\n';
      initiativeRolls.forEach((rollEntry) => {
        initiativeMessage += `${rollEntry.name}: ${rollEntry.roll}\n`;
      });

      // Send the initiative message if required
      discordService.sendCampaignMessage('DnD Beyond', {
        title: 'Initiative Rolls',
        description: initiativeMessage,
        color: 0x00ff00, // Green color
      });
    }

    // Construct the roll history message for the last 5 rolls
    let historyMessage = 'Dice Roll History:\n';
    rollHistory.forEach((entry) => {
      historyMessage += `[${entry.name}] ${entry.action}: ${entry.roll}\n`;
    });

    // Send the roll history message to Discord
    discordService.sendCampaignMessage('DnD Beyond', {
      title: 'Recent Rolls',
      description: historyMessage,
      color: 0x0099ff, // Blue color
    });

    reply.status(200).send();
  },
};

export default dndbeyondController;

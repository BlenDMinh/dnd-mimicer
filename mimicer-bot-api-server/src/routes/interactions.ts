import { FastifyInstance } from 'fastify';

async function interactions(fastify: FastifyInstance) {
  fastify.post('/interactions', async (request, reply) => {
    // Discord Interaction request (you'll need to handle verification in production)
    const interaction = request.body;

    // Log the interaction for debugging
    fastify.log.info(interaction);

    // Acknowledge the interaction with type 1 (simple ACK)
    return {
      type: 1,
    };
  });
}

export default interactions;

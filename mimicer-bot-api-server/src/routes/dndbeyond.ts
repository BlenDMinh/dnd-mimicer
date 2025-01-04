import dndbeyondController from '../controllers/dndbeyond.controller';

async function dndbeyond(fastify) {
  fastify.post('/dndbeyond', async (request, reply) =>
    dndbeyondController.trackDiceRoll(request, reply),
  );
}

export default dndbeyond;

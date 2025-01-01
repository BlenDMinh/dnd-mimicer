export interface CronJob {
  id: number; // Unique identifier for each cron job
  expression: string; // The cron expression (e.g., "0 0 * * *")
  functionName: string; // The function to be triggered by the cron job
}

import React, { useEffect, useState } from "react";
import CreateCronJobModal from "../components/CreateCronJobModal";
import EditCronJobModal from "../components/EditCronJobModal";
import { CronJob } from "../models/CronJob";

const CronJobs: React.FC = () => {
  const [cronJobs, setCronJobs] = useState<CronJob[]>([]);

  const [isCreateModalOpen, setIsCreateModalOpen] = useState(false);
  const [isEditModalOpen, setIsEditModalOpen] = useState(false);
  const [newJob, setNewJob] = useState<Omit<CronJob, "id">>({
    expression: "",
    functionName: "",
  });
  const [editingJob, setEditingJob] = useState<CronJob | null>(null);

  const handleCreate = () => {
    fetch(
      `${import.meta.env.VITE_API_HOST}/cronjobs?api_key=${
        import.meta.env.VITE_API_KEY
      }`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          cron_expression: newJob.expression,
          function: newJob.functionName,
        }),
      }
    )
      .then((res) => res.json())
      .then((data) => ({ ...newJob, id: data.id }))
      .then((newJob) => {
        setCronJobs([...cronJobs, newJob]);
        setNewJob({ expression: "", functionName: "" });
        setIsCreateModalOpen(false);
      });
  };

  const handleEdit = (job: CronJob) => {
    setEditingJob(job);
    setIsEditModalOpen(true);
  };

  const handleUpdate = () => {
    if (editingJob) {
      fetch(
        `${import.meta.env.VITE_API_HOST}/cronjobs/${editingJob.id}?api_key=${
          import.meta.env.VITE_API_KEY
        }`,
        {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            id: editingJob.id,
            cron_expression: editingJob.expression,
            function: editingJob.functionName,
          }),
        }
      )
        .then((res) => res.json())
        .then((editingJob) => {
          setCronJobs(
            cronJobs.map((job) => (job.id === editingJob.id ? editingJob : job))
          );
          setEditingJob(null);
          setIsEditModalOpen(false);
        });
    }
  };

  const handleDelete = (id: number) => {
    fetch(
      `${import.meta.env.VITE_API_HOST}/cronjobs/${id}?api_key=${
        import.meta.env.VITE_API_KEY
      }`,
      {
        method: "DELETE",
      }
    ).then(() => setCronJobs(cronJobs.filter((job) => job.id !== id)));
  };

  useEffect(() => {
    fetch(
      `${import.meta.env.VITE_API_HOST}/cronjobs?api_key=${
        import.meta.env.VITE_API_KEY
      }`
    )
      .then((res) => res.json())
      .then((data) =>
        data.map((job) => ({
          id: job.id,
          expression: job.cron_expression,
          functionName: job.function,
        }))
      )
      .then((jobs) => setCronJobs(jobs));
  }, []);

  return (
    <>
      <div className="space-y-8">
        <div className="flex justify-between items-center">
          <h1 className="text-3xl font-bold">CronJobs</h1>
          <button
            className="btn btn-primary"
            onClick={() => setIsCreateModalOpen(true)}
          >
            Create New CronJob
          </button>
        </div>

        {cronJobs.length > 0 && (
          <div className="overflow-x-auto">
            <table className="table w-full">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Cron Expression</th>
                  <th>Function Name</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                {cronJobs.map((job) => (
                  <tr key={job.id}>
                    <td>{job.id}</td>
                    <td>{job.expression}</td>
                    <td>{job.functionName}</td>
                    <td>
                      <button
                        className="btn btn-sm btn-info mr-2"
                        onClick={() => handleEdit(job)}
                      >
                        Edit
                      </button>
                      <button
                        className="btn btn-sm btn-error"
                        onClick={() => handleDelete(job.id)}
                      >
                        Delete
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
      <CreateCronJobModal
        isOpen={isCreateModalOpen}
        newJob={newJob}
        setNewJob={setNewJob}
        handleCreate={handleCreate}
        closeModal={() => setIsCreateModalOpen(false)}
      />
      <EditCronJobModal
        isOpen={isEditModalOpen}
        editingJob={editingJob}
        setEditingJob={setEditingJob}
        handleUpdate={handleUpdate}
        closeModal={() => setIsEditModalOpen(false)}
      />
    </>
  );
};

export default CronJobs;

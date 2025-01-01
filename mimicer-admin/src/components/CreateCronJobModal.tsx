import React from "react";

interface CreateCronJobModalProps {
  isOpen: boolean;
  newJob: { expression: string; functionName: string };
  setNewJob: React.Dispatch<
    React.SetStateAction<{ expression: string; functionName: string }>
  >;
  handleCreate: () => void;
  closeModal: () => void;
}

const CreateCronJobModal: React.FC<CreateCronJobModalProps> = ({
  isOpen,
  newJob,
  setNewJob,
  handleCreate,
  closeModal,
}) => {
  return (
    <>
      <input
        type="checkbox"
        id="create-modal"
        className="modal-toggle"
        checked={isOpen}
        onChange={() => closeModal()}
      />
      <div className="modal">
        <div className="modal-box">
          <h3 className="font-bold text-lg">Create New CronJob</h3>
          <div className="form-control w-full">
            <label className="label">
              <span className="label-text">Cron Expression</span>
            </label>
            <input
              type="text"
              placeholder="Enter cron expression"
              className="input input-bordered w-full"
              value={newJob.expression}
              onChange={(e) =>
                setNewJob({ ...newJob, expression: e.target.value })
              }
            />
          </div>
          <div className="form-control w-full">
            <label className="label">
              <span className="label-text">Function Name</span>
            </label>
            <input
              type="text"
              placeholder="Enter function name"
              className="input input-bordered w-full"
              value={newJob.functionName}
              onChange={(e) =>
                setNewJob({ ...newJob, functionName: e.target.value })
              }
            />
          </div>
          <div className="modal-action">
            <button className="btn btn-primary" onClick={handleCreate}>
              Create
            </button>
            <button className="btn" onClick={closeModal}>
              Cancel
            </button>
          </div>
        </div>
      </div>
    </>
  );
};

export default CreateCronJobModal;

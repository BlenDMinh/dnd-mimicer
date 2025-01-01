import React from "react";
import { CronJob } from "../models/CronJob";

interface EditCronJobModalProps {
  isOpen: boolean;
  editingJob: CronJob | null;
  setEditingJob: React.Dispatch<React.SetStateAction<CronJob | null>>;
  handleUpdate: () => void;
  closeModal: () => void;
}

const EditCronJobModal: React.FC<EditCronJobModalProps> = ({
  isOpen,
  editingJob,
  setEditingJob,
  handleUpdate,
  closeModal,
}) => {
  return (
    <>
      <input
        type="checkbox"
        id="edit-modal"
        className="modal-toggle"
        checked={isOpen}
        onChange={() => closeModal()}
      />
      <div className="modal">
        <div className="modal-box">
          <h3 className="font-bold text-lg">Edit CronJob</h3>
          <span>
            Not implemented yet. Please implement the edit functionality.
          </span>
          {/* {editingJob && (
            <>
              <div className="form-control w-full">
                <label className="label">
                  <span className="label-text">Cron Expression</span>
                </label>
                <input
                  type="text"
                  placeholder="Enter cron expression"
                  className="input input-bordered w-full"
                  value={editingJob.expression}
                  onChange={(e) =>
                    setEditingJob({ ...editingJob, expression: e.target.value })
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
                  value={editingJob.functionName}
                  onChange={(e) =>
                    setEditingJob({
                      ...editingJob,
                      functionName: e.target.value,
                    })
                  }
                />
              </div>
            </>
          )} */}
          <div className="modal-action">
            <button className="btn btn-primary" onClick={handleUpdate}>
              Update
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

export default EditCronJobModal;

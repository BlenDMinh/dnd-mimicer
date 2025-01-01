import React from "react";
import { Link } from "react-router";

const Channels: React.FC = () => {
  // Placeholder data
  const channels = [
    { id: 1, name: "general", type: "text", members: 50 },
    { id: 2, name: "voice-chat", type: "voice", members: 20 },
    { id: 3, name: "announcements", type: "text", members: 100 },
  ];

  return (
    <div className="space-y-4">
      <h1 className="text-3xl font-bold">Channels</h1>
      <div className="overflow-x-auto">
        <table className="table w-full">
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Type</th>
              <th>Members</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {channels.map((channel) => (
              <tr key={channel.id}>
                <td>{channel.id}</td>
                <td>{channel.name}</td>
                <td>{channel.type}</td>
                <td>{channel.members}</td>
                <td>
                  <Link
                    to={`/channels/edit/${channel.id}`}
                    className="btn btn-sm btn-info mr-2"
                  >
                    Edit
                  </Link>
                  <button className="btn btn-sm btn-error">Delete</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Channels;

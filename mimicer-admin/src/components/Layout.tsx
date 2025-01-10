import React from "react";
import TopBar from "./TopBar";

interface LayoutProps {
  children: React.ReactNode;
}

const Layout: React.FC<LayoutProps> = ({ children }) => {
  return (
    <div className="flex flex-col min-h-screen">
      <TopBar />
      <main className="flex-grow container mx-auto px-4 py-8">{children}</main>
      <footer className="bg-neutral text-neutral-content p-4">
        <div className="container mx-auto text-center">
          <p>&copy; 2025 Mimicer Admin. All rights reserved.</p>
        </div>
      </footer>
    </div>
  );
};

export default Layout;

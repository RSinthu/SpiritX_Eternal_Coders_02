import { createBrowserRouter } from "react-router-dom";
import AdminPage from "./pages/AdminPage";
import UserPage from "./pages/UserPage";
import ChatBotPage from "./pages/ChatBotPage";

const router = createBrowserRouter([
  {
    index: true,
    element: <UserPage />,
  },
  {
    path: "admin",
    element: <AdminPage />,
  },
  {
    path: "chatbot",  
    element: <ChatBotPage />,
  },
]);

export default router;

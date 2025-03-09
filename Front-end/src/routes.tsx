import { createBrowserRouter } from "react-router-dom";
import AdminPage from "./pages/AdminPage";
import UserPage from "./pages/UserPage";

const router = createBrowserRouter([
  {
    index: true,
    element: <UserPage />,
  },
  {
    path: "admin",
    element: <AdminPage />,
  },
]);

export default router;

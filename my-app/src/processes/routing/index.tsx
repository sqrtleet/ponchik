import React from "react";
import { Routes, Route } from "react-router-dom";
import { MainPage } from "../../pages/main";
import { ClassesPage } from "../../pages/classes";
import { SubscriptionsPage } from "../../pages/subscriptions";

export const AppRouter = () => {
  return (
    <Routes>
      <Route path="/" element={<MainPage />} />
      <Route path="/classes" element={<ClassesPage />} />
      <Route path="/subscriptions" element={<SubscriptionsPage />} />
    </Routes>
  );
};

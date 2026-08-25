import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { Toaster as Sonner } from "@/components/ui/sonner";
import { Toaster } from "@/components/ui/toaster";
import { TooltipProvider } from "@/components/ui/tooltip";
import { LanguageProvider } from "@/contexts/LanguageContext";
import { ThemeProvider } from "next-themes";
import Navbar from "@/components/Navbar";
import BottomNav from "@/components/BottomNav";
import Sidebar from "@/components/Sidebar";
import Index from "./pages/Index.tsx";
import Home from "./pages/Home.tsx";
import Articles from "./pages/Articles.tsx";
import ArticleEditor from "./pages/ArticleEditor.tsx";
import Auth from "./pages/Auth.tsx";
import Instructions from "./pages/Instructions.tsx";
import ArticleView from "./pages/ArticleView.tsx";
import Catalog from "./pages/Catalog.tsx";
import Collection from "./pages/Collection.tsx";
import CourseView from "./pages/CourseView.tsx";
import CourseLessons from "./pages/CourseLessons.tsx";
import Profile from "./pages/Profile.tsx";
import BrandResources from "./pages/BrandResources.tsx";
import NotFound from "./pages/NotFound.tsx";

const queryClient = new QueryClient();

const App = () => (
  <QueryClientProvider client={queryClient}>
    <ThemeProvider attribute="class" defaultTheme="light" enableSystem={false}>
      <LanguageProvider>
        <TooltipProvider>
          <Toaster />
          <Sonner />
          <BrowserRouter>
            <div className="flex h-screen">
              <Sidebar />
              <div className="flex-1 min-w-0 flex flex-col">
                {/* Шапка лежит внутри области прокрутки: так при скрытии она
                    не оставляет за собой пустую полосу в разметке */}
                <main className="flex-1 min-w-0 overflow-auto pb-28 md:pb-0">
                  <Navbar />
                  <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/catalog" element={<Catalog />} />
                    <Route path="/collection/:id" element={<Collection />} />
                    <Route path="/my-courses" element={<Index />} />
                    <Route path="/articles" element={<Articles />} />
                    <Route path="/articles/new" element={<ArticleEditor />} />
                    <Route path="/articles/:id" element={<ArticleEditor />} />
                    <Route path="/auth" element={<Auth />} />
                    <Route path="/course/:id" element={<CourseView />} />
                    <Route path="/course/:id/lessons" element={<Index />} />
                    <Route path="/instructions" element={<Instructions />} />
                    <Route path="/instructions/:id" element={<ArticleView />} />
                    <Route path="/profile" element={<Profile />} />
                    <Route path="/brand" element={<BrandResources />} />
                    <Route path="*" element={<NotFound />} />
                  </Routes>
                </main>
              </div>
            </div>
            <BottomNav />
          </BrowserRouter>
        </TooltipProvider>
      </LanguageProvider>
    </ThemeProvider>
  </QueryClientProvider>
);

export default App;

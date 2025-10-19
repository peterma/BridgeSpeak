import React, { useState } from 'react';
import { Button } from './ui/button';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './ui/card';
import { Input } from './ui/input';
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle, DialogTrigger } from './ui/dialog';

export default function ShadcnDemo() {
  const [isDark, setIsDark] = useState(false);

  const toggleTheme = () => {
    setIsDark(!isDark);
    document.documentElement.classList.toggle('dark');
  };

  return (
    <div className={`min-h-screen p-4 ${isDark ? 'dark' : ''}`}>
      <div className="max-w-4xl mx-auto space-y-8">
        
        {/* Header with Theme Toggle */}
        <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
          <div>
            <h1 className="text-2xl md:text-3xl lg:text-4xl font-bold">
              shadcn/ui Demo
            </h1>
            <p className="text-muted-foreground text-sm md:text-base">
              Responsive design with light/dark theme support
            </p>
          </div>
          <Button onClick={toggleTheme} variant="outline" size="sm">
            {isDark ? '☀️ Light' : '🌙 Dark'} Mode
          </Button>
        </div>

        {/* Responsive Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 md:gap-6">
          
          {/* Card 1 - Mobile First */}
          <Card className="col-span-1">
            <CardHeader>
              <CardTitle className="text-lg md:text-xl">Mobile First</CardTitle>
              <CardDescription>
                This card adapts to all screen sizes
              </CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
              <Input placeholder="Responsive input" className="w-full" />
              <Button className="w-full sm:w-auto">
                Full width on mobile
              </Button>
            </CardContent>
          </Card>

          {/* Card 2 - Breakpoint Demo */}
          <Card className="col-span-1 md:col-span-2 lg:col-span-1">
            <CardHeader>
              <CardTitle className="text-base sm:text-lg md:text-xl">
                Breakpoints
              </CardTitle>
              <CardDescription className="text-xs sm:text-sm">
                Text sizes change across devices
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-2 text-xs sm:text-sm md:text-base">
                <p className="font-medium">Current breakpoints:</p>
                <ul className="space-y-1 text-muted-foreground">
                  <li className="block sm:hidden">📱 Mobile (&lt; 640px)</li>
                  <li className="hidden sm:block md:hidden">📋 Small (640px+)</li>
                  <li className="hidden md:block lg:hidden">💻 Medium (768px+)</li>
                  <li className="hidden lg:block xl:hidden">🖥️ Large (1024px+)</li>
                  <li className="hidden xl:block">🖥️ XL (1280px+)</li>
                </ul>
              </div>
            </CardContent>
          </Card>

          {/* Card 3 - Interactive Dialog */}
          <Card className="col-span-1 md:col-span-2 lg:col-span-1">
            <CardHeader>
              <CardTitle>Interactive Demo</CardTitle>
              <CardDescription>
                Accessible components with proper focus management
              </CardDescription>
            </CardHeader>
            <CardContent>
              <Dialog>
                <DialogTrigger asChild>
                  <Button variant="default" className="w-full">
                    Open Dialog
                  </Button>
                </DialogTrigger>
                <DialogContent className="max-w-md mx-4 sm:mx-0">
                  <DialogHeader>
                    <DialogTitle>Responsive Dialog</DialogTitle>
                    <DialogDescription>
                      This dialog adapts to mobile and desktop screens.
                      It includes proper ARIA attributes and keyboard navigation.
                    </DialogDescription>
                  </DialogHeader>
                  <div className="space-y-4 pt-4">
                    <Input placeholder="Enter your name" />
                    <div className="flex flex-col sm:flex-row gap-2">
                      <Button className="flex-1">Save</Button>
                      <DialogTrigger asChild>
                        <Button variant="outline" className="flex-1">Cancel</Button>
                      </DialogTrigger>
                    </div>
                  </div>
                </DialogContent>
              </Dialog>
            </CardContent>
          </Card>
        </div>

        {/* Feature Showcase */}
        <Card>
          <CardHeader>
            <CardTitle className="text-xl md:text-2xl">
              🎉 shadcn/ui Features
            </CardTitle>
            <CardDescription>
              Everything you need for modern React applications
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
              <div className="space-y-2">
                <h4 className="font-medium text-primary">📱 Responsive</h4>
                <p className="text-sm text-muted-foreground">
                  Mobile-first design with Tailwind breakpoints
                </p>
              </div>
              <div className="space-y-2">
                <h4 className="font-medium text-primary">🎨 Themeable</h4>
                <p className="text-sm text-muted-foreground">
                  CSS variables for easy customization
                </p>
              </div>
              <div className="space-y-2">
                <h4 className="font-medium text-primary">♿ Accessible</h4>
                <p className="text-sm text-muted-foreground">
                  Built on Radix UI primitives
                </p>
              </div>
              <div className="space-y-2">
                <h4 className="font-medium text-primary">🚀 Fast</h4>
                <p className="text-sm text-muted-foreground">
                  Copy-paste, no dependencies
                </p>
              </div>
            </div>
          </CardContent>
        </Card>

        {/* Button Variants Showcase */}
        <Card>
          <CardHeader>
            <CardTitle>Button Variants</CardTitle>
            <CardDescription>
              All button styles adapt to your theme
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div className="flex flex-wrap gap-2">
              <Button variant="default">Default</Button>
              <Button variant="secondary">Secondary</Button>
              <Button variant="destructive">Destructive</Button>
              <Button variant="outline">Outline</Button>
              <Button variant="ghost">Ghost</Button>
              <Button variant="link">Link</Button>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
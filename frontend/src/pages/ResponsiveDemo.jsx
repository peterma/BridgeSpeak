import React from 'react';
import { ResponsiveGrid, ResponsiveContainer, ResponsiveCard, ResponsiveText } from '../components/ResponsiveGrid';

export default function ResponsiveDemo() {
  return (
    <ResponsiveContainer className="py-8">
      {/* Header */}
      <div className="text-center mb-12">
        <h1 className="text-2xl sm:text-3xl lg:text-4xl font-bold text-gray-900 mb-4">
          Responsive Design Demo
        </h1>
        <ResponsiveText 
          size="lg xl:xl" 
          color="gray-600"
          className="max-w-3xl mx-auto"
        >
          This page demonstrates mobile-first responsive design patterns using Tailwind CSS breakpoints.
          Resize your browser window to see the layout adapt to different screen sizes.
        </ResponsiveText>
      </div>

      {/* Breakpoint Indicators */}
      <ResponsiveCard className="mb-8">
        <h2 className="text-xl font-semibold mb-4">Current Screen Size</h2>
        <div className="space-y-2">
          <div className="block sm:hidden text-red-600 font-medium">📱 Mobile (&lt; 640px)</div>
          <div className="hidden sm:block md:hidden text-orange-600 font-medium">📋 Small (640px - 768px)</div>
          <div className="hidden md:block lg:hidden text-yellow-600 font-medium">💻 Medium (768px - 1024px)</div>
          <div className="hidden lg:block xl:hidden text-green-600 font-medium">🖥️ Large (1024px - 1280px)</div>
          <div className="hidden xl:block text-blue-600 font-medium">🖥️ Extra Large (1280px+)</div>
        </div>
      </ResponsiveCard>

      {/* Grid Examples */}
      <div className="space-y-12">
        
        {/* Single to Multi-column Grid */}
        <section>
          <h2 className="text-2xl font-bold mb-6">Responsive Grid Layouts</h2>
          
          <div className="mb-8">
            <h3 className="text-lg font-semibold mb-4">1→2→3→4 Column Grid</h3>
            <ResponsiveGrid cols="1 sm:2 lg:3 xl:4">
              {[1, 2, 3, 4, 5, 6, 7, 8].map(num => (
                <ResponsiveCard key={num} className="text-center">
                  <div className="text-2xl font-bold text-blue-600 mb-2">{num}</div>
                  <ResponsiveText size="sm">Grid Item {num}</ResponsiveText>
                </ResponsiveCard>
              ))}
            </ResponsiveGrid>
          </div>

          <div className="mb-8">
            <h3 className="text-lg font-semibold mb-4">1→2→3 Column Grid (Scenarios Layout)</h3>
            <ResponsiveGrid cols="1 sm:2 lg:3">
              {['Math Practice', 'Reading Stories', 'Science Experiments', 'Art Projects', 'Music Lessons', 'Physical Education'].map(scenario => (
                <ResponsiveCard key={scenario} className="hover:shadow-lg cursor-pointer">
                  <div className="text-4xl mb-3">🎭</div>
                  <h4 className="font-semibold text-gray-900 mb-2">{scenario}</h4>
                  <ResponsiveText size="sm" color="gray-600">
                    Practice {scenario.toLowerCase()} with interactive exercises.
                  </ResponsiveText>
                  <div className="mt-4">
                    <span className="inline-block bg-blue-100 text-blue-800 text-xs px-2 py-1 rounded-full">
                      Interactive
                    </span>
                  </div>
                </ResponsiveCard>
              ))}
            </ResponsiveGrid>
          </div>
        </section>

        {/* Typography Examples */}
        <section>
          <h2 className="text-2xl font-bold mb-6">Responsive Typography</h2>
          <ResponsiveCard>
            <ResponsiveText 
              as="h1" 
              size="xl sm:2xl lg:3xl xl:4xl" 
              weight="bold" 
              className="mb-4"
            >
              Responsive Heading (xl→2xl→3xl→4xl)
            </ResponsiveText>
            <ResponsiveText 
              size="sm md:base lg:lg" 
              color="gray-600" 
              className="mb-4"
            >
              This paragraph text scales from small on mobile (sm) to base on medium screens (md:base) 
              to large on large screens (lg:lg). The text becomes more readable as screen size increases.
            </ResponsiveText>
            <ResponsiveText 
              size="xs sm:sm md:base" 
              color="gray-500"
            >
              Smaller text that grows: xs → sm → base
            </ResponsiveText>
          </ResponsiveCard>
        </section>

        {/* Spacing Examples */}
        <section>
          <h2 className="text-2xl font-bold mb-6">Responsive Spacing</h2>
          <div className="space-y-4 md:space-y-6 lg:space-y-8">
            <ResponsiveCard padding="3 md:4 lg:6">
              <h3 className="font-semibold mb-2">Responsive Padding</h3>
              <ResponsiveText>
                This card has padding that increases with screen size: p-3 → md:p-4 → lg:p-6
              </ResponsiveText>
            </ResponsiveCard>
            
            <ResponsiveCard>
              <h3 className="font-semibold mb-2">Responsive Margins</h3>
              <ResponsiveText>
                The space between these cards increases: space-y-4 → md:space-y-6 → lg:space-y-8
              </ResponsiveText>
            </ResponsiveCard>
          </div>
        </section>

        {/* Component Visibility */}
        <section>
          <h2 className="text-2xl font-bold mb-6">Responsive Visibility</h2>
          <ResponsiveCard>
            <div className="space-y-4">
              <div className="block sm:hidden p-4 bg-red-100 rounded-lg">
                <strong>Mobile Only:</strong> This content only shows on screens smaller than 640px
              </div>
              
              <div className="hidden sm:block md:hidden p-4 bg-orange-100 rounded-lg">
                <strong>Small Screens Only:</strong> Visible on 640px-768px screens
              </div>
              
              <div className="hidden md:block lg:hidden p-4 bg-yellow-100 rounded-lg">
                <strong>Medium Screens Only:</strong> Visible on 768px-1024px screens
              </div>
              
              <div className="hidden lg:block p-4 bg-green-100 rounded-lg">
                <strong>Large Screens+:</strong> Visible on screens 1024px and larger
              </div>

              <div className="p-4 bg-blue-100 rounded-lg">
                <strong>Always Visible:</strong> This content is visible on all screen sizes
              </div>
            </div>
          </ResponsiveCard>
        </section>

        {/* Best Practices */}
        <section>
          <h2 className="text-2xl font-bold mb-6">Responsive Design Best Practices</h2>
          <ResponsiveGrid cols="1 lg:2">
            <ResponsiveCard>
              <h3 className="font-semibold text-green-600 mb-3">✅ Do's</h3>
              <ul className="space-y-2 text-sm">
                <li>• Use mobile-first approach (base styles for mobile)</li>
                <li>• Use relative units (rem, %, vw) over fixed pixels</li>
                <li>• Test on real devices, not just browser resize</li>
                <li>• Optimize images for different screen densities</li>
                <li>• Use consistent breakpoints across components</li>
                <li>• Focus on touch-friendly interactions on mobile</li>
              </ul>
            </ResponsiveCard>
            
            <ResponsiveCard>
              <h3 className="font-semibold text-red-600 mb-3">❌ Don'ts</h3>
              <ul className="space-y-2 text-sm">
                <li>• Don't use fixed widths for main content areas</li>
                <li>• Don't assume mouse hover states on mobile</li>
                <li>• Don't make text too small on mobile screens</li>
                <li>• Don't use horizontal scrolling for main content</li>
                <li>• Don't ignore landscape orientation on tablets</li>
                <li>• Don't forget about accessibility on small screens</li>
              </ul>
            </ResponsiveCard>
          </ResponsiveGrid>
        </section>

        {/* Tailwind Breakpoints Reference */}
        <section>
          <h2 className="text-2xl font-bold mb-6">Tailwind CSS Breakpoints Reference</h2>
          <ResponsiveCard>
            <div className="overflow-x-auto">
              <table className="w-full text-sm">
                <thead>
                  <tr className="border-b">
                    <th className="text-left py-2">Breakpoint</th>
                    <th className="text-left py-2">Prefix</th>
                    <th className="text-left py-2">Min Width</th>
                    <th className="text-left py-2">Example Usage</th>
                  </tr>
                </thead>
                <tbody className="space-y-2">
                  <tr className="border-b">
                    <td className="py-2 font-medium">Small</td>
                    <td className="py-2"><code className="bg-gray-100 px-1 rounded">sm:</code></td>
                    <td className="py-2">640px</td>
                    <td className="py-2"><code className="bg-gray-100 px-1 rounded">sm:grid-cols-2</code></td>
                  </tr>
                  <tr className="border-b">
                    <td className="py-2 font-medium">Medium</td>
                    <td className="py-2"><code className="bg-gray-100 px-1 rounded">md:</code></td>
                    <td className="py-2">768px</td>
                    <td className="py-2"><code className="bg-gray-100 px-1 rounded">md:text-lg</code></td>
                  </tr>
                  <tr className="border-b">
                    <td className="py-2 font-medium">Large</td>
                    <td className="py-2"><code className="bg-gray-100 px-1 rounded">lg:</code></td>
                    <td className="py-2">1024px</td>
                    <td className="py-2"><code className="bg-gray-100 px-1 rounded">lg:grid-cols-3</code></td>
                  </tr>
                  <tr className="border-b">
                    <td className="py-2 font-medium">Extra Large</td>
                    <td className="py-2"><code className="bg-gray-100 px-1 rounded">xl:</code></td>
                    <td className="py-2">1280px</td>
                    <td className="py-2"><code className="bg-gray-100 px-1 rounded">xl:grid-cols-4</code></td>
                  </tr>
                  <tr>
                    <td className="py-2 font-medium">2X Large</td>
                    <td className="py-2"><code className="bg-gray-100 px-1 rounded">2xl:</code></td>
                    <td className="py-2">1536px</td>
                    <td className="py-2"><code className="bg-gray-100 px-1 rounded">2xl:text-6xl</code></td>
                  </tr>
                </tbody>
              </table>
            </div>
          </ResponsiveCard>
        </section>
      </div>
    </ResponsiveContainer>
  );
}
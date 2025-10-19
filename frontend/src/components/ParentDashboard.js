/**
 * Parent Dashboard Component for Trauma-Informed Sensitivity Controls
 * 
 * Provides parent interface for adjusting platform sensitivity settings
 * based on their child's anxiety levels and learning needs.
 */

import React, { useState, useEffect } from 'react';
import './ParentDashboard.css';

const ParentDashboard = ({ parentId, onSettingsChange }) => {
  const [children, setChildren] = useState([]);
  const [selectedChild, setSelectedChild] = useState(null);
  const [settings, setSettings] = useState(null);
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [message, setMessage] = useState('');

  useEffect(() => {
    loadParentData();
  }, [parentId]);

  const loadParentData = async () => {
    try {
      setLoading(true);
      const response = await fetch(`http://localhost:8081/api/v1/parents/${parentId}/dashboard`);
      const data = await response.json();
      
      if (data.children) {
        setChildren(data.children);
        if (data.children.length > 0) {
          setSelectedChild(data.children[0].child_id);
        }
      }
    } catch (error) {
      console.error('Error loading parent data:', error);
      setMessage('Error loading dashboard data');
    } finally {
      setLoading(false);
    }
  };

  const loadChildSettings = async (childId) => {
    try {
      const response = await fetch(`http://localhost:8081/api/v1/children/${childId}/sensitivity-settings`);
      const data = await response.json();
      setSettings(data);
    } catch (error) {
      console.error('Error loading child settings:', error);
      setMessage('Error loading child settings');
    }
  };

  useEffect(() => {
    if (selectedChild) {
      loadChildSettings(selectedChild);
    }
  }, [selectedChild]);

  const handleSettingsChange = async (field, value) => {
    if (!selectedChild || !settings) return;

    const updatedSettings = { ...settings, [field]: value };
    setSettings(updatedSettings);

    try {
      setSaving(true);
      const response = await fetch(`http://localhost:8081/api/v1/children/${selectedChild}/sensitivity-settings`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ [field]: value }),
      });

      if (response.ok) {
        setMessage('Settings saved successfully');
        if (onSettingsChange) {
          onSettingsChange(selectedChild, updatedSettings);
        }
      } else {
        setMessage('Error saving settings');
      }
    } catch (error) {
      console.error('Error saving settings:', error);
      setMessage('Error saving settings');
    } finally {
      setSaving(false);
    }
  };

  const applyAnxietyOverride = async () => {
    if (!selectedChild) return;

    try {
      setSaving(true);
      const response = await fetch(`http://localhost:8081/api/v1/children/${selectedChild}/anxiety-override`, {
        method: 'POST',
      });

      if (response.ok) {
        await loadChildSettings(selectedChild);
        setMessage('Anxiety-specific settings applied');
      } else {
        setMessage('Error applying anxiety settings');
      }
    } catch (error) {
      console.error('Error applying anxiety override:', error);
      setMessage('Error applying anxiety settings');
    } finally {
      setSaving(false);
    }
  };

  const applyConfidenceSettings = async () => {
    if (!selectedChild) return;

    try {
      setSaving(true);
      const response = await fetch(`http://localhost:8081/api/v1/children/${selectedChild}/confidence-settings`, {
        method: 'POST',
      });

      if (response.ok) {
        await loadChildSettings(selectedChild);
        setMessage('Confidence-optimized settings applied');
      } else {
        setMessage('Error applying confidence settings');
      }
    } catch (error) {
      console.error('Error applying confidence settings:', error);
      setMessage('Error applying confidence settings');
    } finally {
      setSaving(false);
    }
  };

  if (loading) {
    return (
      <div className="parent-dashboard">
        <div className="loading">Loading parent dashboard...</div>
      </div>
    );
  }

  return (
    <div className="parent-dashboard">
      <div className="dashboard-header">
        <h2>Parent Sensitivity Controls</h2>
        <p>Adjust platform behavior based on your child's needs and anxiety levels</p>
      </div>

      {message && (
        <div className={`message ${message.includes('Error') ? 'error' : 'success'}`}>
          {message}
        </div>
      )}

      <div className="child-selector">
        <label htmlFor="child-select">Select Child:</label>
        <select
          id="child-select"
          value={selectedChild || ''}
          onChange={(e) => setSelectedChild(e.target.value)}
        >
          <option value="">Choose a child...</option>
          {children.map((child) => (
            <option key={child.child_id} value={child.child_id}>
              {child.child_id}
            </option>
          ))}
        </select>
      </div>

      {settings && (
        <div className="sensitivity-settings">
          <h3>Sensitivity Settings</h3>

          <div className="setting-group">
            <label htmlFor="interaction-pacing">Interaction Pacing:</label>
            <select
              id="interaction-pacing"
              value={settings.interaction_pacing}
              onChange={(e) => handleSettingsChange('interaction_pacing', e.target.value)}
              disabled={saving}
            >
              <option value="extra_patient">Extra Patient (for anxious children)</option>
              <option value="standard">Standard (default trauma-informed)</option>
              <option value="responsive">Responsive (for confident children)</option>
            </select>
            <p className="setting-description">
              Controls how patient Xiao Mei is when waiting for responses
            </p>
          </div>

          <div className="setting-group">
            <label htmlFor="encouragement-frequency">Encouragement Frequency (seconds):</label>
            <input
              id="encouragement-frequency"
              type="number"
              min="30"
              max="120"
              value={settings.encouragement_frequency}
              onChange={(e) => handleSettingsChange('encouragement_frequency', parseInt(e.target.value))}
              disabled={saving}
            />
            <p className="setting-description">
              How often Xiao Mei offers gentle encouragement (30-120 seconds)
            </p>
          </div>

          <div className="setting-group">
            <label htmlFor="celebration-intensity">Celebration Intensity:</label>
            <select
              id="celebration-intensity"
              value={settings.celebration_intensity}
              onChange={(e) => handleSettingsChange('celebration_intensity', e.target.value)}
              disabled={saving}
            >
              <option value="gentle">Gentle (calming, subtle)</option>
              <option value="moderate">Moderate (balanced)</option>
              <option value="enthusiastic">Enthusiastic (more expressive)</option>
            </select>
            <p className="setting-description">
              How expressive Xiao Mei's celebrations are
            </p>
          </div>

          <div className="setting-group">
            <label htmlFor="exit-reminder-frequency">Break Reminder Frequency (seconds):</label>
            <input
              id="exit-reminder-frequency"
              type="number"
              min="60"
              max="600"
              value={settings.exit_reminder_frequency}
              onChange={(e) => handleSettingsChange('exit_reminder_frequency', parseInt(e.target.value))}
              disabled={saving}
            />
            <p className="setting-description">
              How often to remind child they can take a break (60-600 seconds)
            </p>
          </div>

          <div className="setting-group">
            <label>
              <input
                type="checkbox"
                checked={settings.cultural_comfort_emphasis}
                onChange={(e) => handleSettingsChange('cultural_comfort_emphasis', e.target.checked)}
                disabled={saving}
              />
              Emphasize Chinese Comfort Phase
            </label>
            <p className="setting-description">
              Prioritize Chinese language comfort before English practice
            </p>
          </div>

          <div className="setting-group">
            <label>
              <input
                type="checkbox"
                checked={settings.anxiety_override}
                onChange={(e) => handleSettingsChange('anxiety_override', e.target.checked)}
                disabled={saving}
              />
              Anxiety-Specific Override
            </label>
            <p className="setting-description">
              Apply special settings for highly anxious children
            </p>
          </div>

          <div className="setting-group">
            <label htmlFor="parent-notes">Parent Notes:</label>
            <textarea
              id="parent-notes"
              value={settings.parent_notes || ''}
              onChange={(e) => handleSettingsChange('parent_notes', e.target.value)}
              disabled={saving}
              placeholder="Add notes about your child's specific needs..."
              rows="3"
            />
          </div>

          <div className="quick-actions">
            <h4>Quick Actions</h4>
            <button
              onClick={applyAnxietyOverride}
              disabled={saving}
              className="anxiety-button"
            >
              Apply Anxiety-Specific Settings
            </button>
            <button
              onClick={applyConfidenceSettings}
              disabled={saving}
              className="confidence-button"
            >
              Apply Confidence Settings
            </button>
          </div>

          {saving && (
            <div className="saving-indicator">Saving settings...</div>
          )}
        </div>
      )}

      <div className="trauma-informed-info">
        <h4>Trauma-Informed Design</h4>
        <p>
          These settings ensure your child's emotional safety is prioritized over learning efficiency.
          The platform never uses negative feedback, time pressure, or competitive elements.
        </p>
        <ul>
          <li>✅ Zero failure states - all attempts are celebrated</li>
          <li>✅ No time pressure or countdown timers</li>
          <li>✅ Patient waiting with gentle encouragement</li>
          <li>✅ Bilingual praise and cultural sensitivity</li>
          <li>✅ Seamless exit without penalty</li>
        </ul>
      </div>
    </div>
  );
};

export default ParentDashboard;

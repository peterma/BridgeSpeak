/**
 * WebRTC Client using Pipecat RTVI SDK
 * 
 * This class wraps the Pipecat RTVI client to provide a simple interface for
 * connecting to a Pipecat bot server. The RTVI (Real-Time Voice Interaction) protocol
 * ensures proper coordination between the client and server, preventing issues like
 * dropped first turns and providing better audio quality.
 * 
 * Key Features:
 * - Automatic client-server coordination via RTVI events
 * - Built-in echo cancellation and noise suppression
 * - Support for both audio and video tracks
 * - Event-based callbacks for connection state changes
 * 
 * Based on simple-chatbot example from pipecat-examples
 */
import { RTVIEvent, PipecatClient } from '@pipecat-ai/client-js';
import { SmallWebRTCTransport } from '@pipecat-ai/small-webrtc-transport';

export class WebRTCClient {
  /**
   * Creates a new WebRTC client instance
   * @param {string} serverUrl - The URL of the backend proxy (default: http://localhost:8081)
   */
  constructor(serverUrl = 'http://localhost:8080') {
    this.serverUrl = serverUrl;
    
    // The main Pipecat RTVI client instance
    this.pcClient = null;
    
    // MediaStream that accumulates the bot's audio + video tracks
    // This stream is passed to the UI when tracks are received
    this.botStream = null;
    
    // Callback functions that can be set by the UI component
    this.callbacks = {
      onTrack: null,                    // Called when a new media track is received from the bot
      onConnectionStateChange: null,    // Called when the connection state changes
      onError: null,                    // Called when an error occurs
      onBotReady: null,                 // Called when the bot signals it's ready to start
      onConnected: null,                // Called when successfully connected to the server
    };
  }

  /**
   * Initialize and connect to the Pipecat bot using RTVI protocol
   * 
   * This method:
   * 1. Creates a PipecatClient with SmallWebRTCTransport
   * 2. Sets up event listeners for connection state changes and incoming tracks
   * 3. Connects to the Pipecat server's WebRTC endpoint
   * 
   * The RTVI protocol handles the client-ready/bot-ready handshake automatically,
   * ensuring that the bot's first turn is never dropped.
   * 
   * @param {Object} options - Connection options
   * @param {string} options.scenario - The scenario ID to use for the conversation
   * @returns {Promise<boolean>} True if connection was successful
   * @throws {Error} If connection fails
   */
  async connect(options = {}) {
    try {
      // Create transport with simple configuration
      const transport = new SmallWebRTCTransport();
      
      // Create PipecatClient with SmallWebRTCTransport
      const clientConfig = {
        transport: transport,
        
        // Media initialization
        enableMic: true,
        enableCam: false, // Will be overridden based on options.enableCam
        enableScreenShare: false,
      };

      // Allow caller to override initial camera state
      if (typeof options.enableCam === 'boolean') {
        clientConfig.enableCam = options.enableCam;
        console.log('WebRTC Client: Setting enableCam to', options.enableCam);
      }

      // Build params for scenario data if needed
      let requestParams = {};
      if (options.scenario) {
        requestParams = {
          scenario: options.scenario,
          scenarioDetails: options.scenarioDetails || undefined,
          enableVideo: typeof options.enableCam === 'boolean' ? options.enableCam : true,
        };
        console.log('WebRTC Client: Setting requestData:', requestParams);
        console.log('WebRTC Client: Setting params.scenario:', requestParams.scenario);
      }

      // Set up callbacks for various connection events
      // These are called by the PipecatClient at different stages
      clientConfig.callbacks = {
          // Called when WebRTC connection is established
          onConnected: () => {
            console.log('WebRTC connection established');
            if (this.callbacks.onConnected) {
              this.callbacks.onConnected();
            }
            if (this.callbacks.onConnectionStateChange) {
              this.callbacks.onConnectionStateChange('connected');
            }
          },
          
          // Called when WebRTC connection is closed
          onDisconnected: () => {
            console.log('WebRTC connection closed');
            if (this.callbacks.onConnectionStateChange) {
              this.callbacks.onConnectionStateChange('disconnected');
            }
          },
          
          // Called when the transport state changes (connecting, connected, disconnected, etc.)
          onTransportStateChanged: (state) => {
            console.log('Transport state changed:', state);
            if (this.callbacks.onConnectionStateChange) {
              this.callbacks.onConnectionStateChange(state);
            }
          },
          
          // Called when the bot connects to the pipeline
          onBotConnected: () => {
            console.log('Bot connected to pipeline');
          },
          
          // Called when the bot disconnects from the pipeline
          onBotDisconnected: () => {
            console.log('Bot disconnected from pipeline');
          },
          
          // Called when the bot signals it's ready to start the conversation
          // This is part of the RTVI protocol handshake
          onBotReady: () => {
            console.log('Bot is ready to start conversation');
            if (this.callbacks.onBotReady) {
              this.callbacks.onBotReady();
            }
          },
          
          // Called when an error occurs in the client or transport
          onError: (error) => {
            console.error('Pipecat error:', error);
            if (this.callbacks.onError) {
              this.callbacks.onError(error);
            }
          },
        };

      console.log('WebRTC Client: Final client config:', {
        enableMic: clientConfig.enableMic,
        enableCam: clientConfig.enableCam,
        enableScreenShare: clientConfig.enableScreenShare
      });
      
      this.pcClient = new PipecatClient(clientConfig);

      // Set up event listener for incoming media tracks using RTVI events
      // This is called whenever a new audio or video track is received from the bot
      this.pcClient.on(RTVIEvent.TrackStarted, (track, participant) => {
        console.log('Track started:', track.kind, 'from participant:', participant);
        
        // Skip local tracks (user's own audio/video)
        // We only want to handle tracks coming from the bot
        if (participant?.local === true) {
          return;
        }
        
        // Initialize bot stream if this is the first track we're receiving
        if (!this.botStream) {
          this.botStream = new MediaStream();
        }
        
        // Add the track (audio or video) to the bot's media stream
        // This allows both audio and video to be played in a single <video> element
        this.botStream.addTrack(track);
        
        // Notify the UI that we have a new track (or updated stream)
        // The UI can use this stream to display the bot's video/audio
        if (this.callbacks.onTrack) {
          this.callbacks.onTrack(this.botStream);
        }
      });

      // Connect to the Pipecat WebRTC server
      // The /api/offer endpoint is provided by Pipecat's WebRTC transport
      console.log('Connecting to Pipecat server at:', this.serverUrl);
      if (options.scenario) {
        console.log('Using scenario:', options.scenario);
      }
      
      // Connect to the Pipecat server with the endpoint URL
      console.log('Connecting to Pipecat server at:', this.serverUrl);
      if (options.scenario) {
        console.log('Using scenario:', options.scenario);
      }
      
      await this.pcClient.connect({
        webrtcUrl: `${this.serverUrl}/api/offer`,
      });
      
      // After connection, send scenario data if available
      if (Object.keys(requestParams).length > 0) {
        console.log('WebRTC Client: Sending scenario data after connection:', requestParams);
        try {
          this.pcClient.sendClientMessage('scenario', requestParams);
        } catch (error) {
          console.warn('WebRTC Client: Failed to send scenario data:', error);
        }
      }
      
      // If camera was disabled, try to disable it after connection
      if (typeof options.enableCam === 'boolean' && !options.enableCam) {
        console.log('WebRTC Client: Attempting to disable camera after connection');
        try {
          if (typeof this.pcClient.enableCam === 'function') {
            await this.pcClient.enableCam(false);
            console.log('WebRTC Client: Camera disabled after connection');
          }
        } catch (error) {
          console.warn('WebRTC Client: Failed to disable camera after connection:', error);
        }
      }
      
      console.log('Successfully connected to Pipecat server');
      return true;
    } catch (error) {
      console.error('Connection error:', error);
      if (this.callbacks.onError) {
        this.callbacks.onError(error);
      }
      throw error;
    }
  }

  /**
   * Disconnect from the Pipecat server and cleanup resources
   * 
   * This method safely closes the WebRTC connection and cleans up all resources.
   * It's important to call this when the user leaves the call to prevent memory leaks.
   */
  async disconnect() {
    if (this.pcClient) {
      try {
        console.log('Disconnecting from Pipecat server');
        await this.pcClient.disconnect();
      } catch (error) {
        console.error('Error disconnecting:', error);
      }
      this.pcClient = null;
    }
    
    // Clear the bot stream reference
    this.botStream = null;
  }

  /**
   * Toggle the microphone on or off
   * 
   * This allows the user to mute/unmute their microphone during the call.
   * When muted, the bot won't receive any audio from the user.
   * 
   * @param {boolean} enabled - True to enable the microphone, false to disable
   * @returns {Promise<boolean>} The new state of the microphone
   */
  async toggleMicrophone(enabled) {
    if (this.pcClient) {
      try {
        if (enabled) {
          console.log('Enabling microphone');
          await this.pcClient.enableMic();
        } else {
          console.log('Disabling microphone');
          await this.pcClient.disableMic();
        }
        return enabled;
      } catch (error) {
        console.error('Error toggling microphone:', error);
      }
    }
    return false;
  }

  /**
   * Toggle the camera on or off
   * 
   * This allows the user to show/hide their camera during the call.
   * When disabled, the bot won't receive video from the user.
   * 
   * @param {boolean} enabled - True to enable the camera, false to disable
   * @returns {Promise<boolean>} The new state of the camera
   */
  async toggleCamera(enabled) {
    if (this.pcClient) {
      try {
        // Use official Pipecat API method: https://docs.pipecat.ai/client/js/api-reference/client-methods
        if (typeof this.pcClient.enableCam === 'function') {
          console.log(enabled ? 'Enabling camera' : 'Disabling camera');
          await this.pcClient.enableCam(enabled);
        } else {
          // Fallback for older API versions
          if (enabled) {
            console.log('Enabling camera (fallback)');
            if (typeof this.pcClient.enableVideo === 'function') {
              await this.pcClient.enableVideo();
            } else if (typeof this.pcClient.setCamEnabled === 'function') {
              await this.pcClient.setCamEnabled(true);
            } else {
              // Fallback: toggle local video track enabled flag
              const tracks = this.pcClient.tracks?.();
              const localVideo = tracks?.local?.video;
              if (localVideo) localVideo.enabled = true;
            }
          } else {
            console.log('Disabling camera (fallback)');
            if (typeof this.pcClient.disableCam === 'function') {
              await this.pcClient.disableCam();
            } else if (typeof this.pcClient.disableVideo === 'function') {
              await this.pcClient.disableVideo();
            } else if (typeof this.pcClient.setCamEnabled === 'function') {
              await this.pcClient.setCamEnabled(false);
            } else {
              // Fallback: toggle local video track enabled flag
              const tracks = this.pcClient.tracks?.();
              const localVideo = tracks?.local?.video;
              if (localVideo) localVideo.enabled = false;
            }
          }
        }
        return enabled;
      } catch (error) {
        console.error('Error toggling camera:', error);
      }
    }
    return false;
  }

  /**
   * Get the local media stream (user's camera and microphone)
   * 
   * This method retrieves the user's own audio and video tracks and combines
   * them into a single MediaStream that can be displayed in a video element.
   * 
   * @returns {MediaStream|null} The local media stream, or null if not available
   */
  getLocalStream() {
    if (this.pcClient) {
      try {
        // Get all tracks from the client
        const tracks = this.pcClient.tracks();
        const localTracks = tracks?.local;
        
        if (localTracks) {
          // Create a new MediaStream and add the local audio/video tracks
          const stream = new MediaStream();
          if (localTracks.audio) stream.addTrack(localTracks.audio);
          if (localTracks.video) stream.addTrack(localTracks.video);
          return stream;
        }
      } catch (error) {
        console.error('Error getting local stream:', error);
      }
    }
    return null;
  }

  /**
   * Get the remote media stream (bot's audio and video)
   * 
   * This method retrieves the bot's audio and video tracks and combines
   * them into a single MediaStream that can be displayed in a video element.
   * 
   * @returns {MediaStream|null} The remote media stream, or null if not available
   */
  getRemoteStream() {
    if (this.pcClient) {
      try {
        // Get all tracks from the client
        const tracks = this.pcClient.tracks();
        const botTracks = tracks?.bot;
        
        if (botTracks) {
          // Create a new MediaStream and add the bot's audio/video tracks
          const stream = new MediaStream();
          if (botTracks.audio) stream.addTrack(botTracks.audio);
          if (botTracks.video) stream.addTrack(botTracks.video);
          return stream;
        }
      } catch (error) {
        console.error('Error getting remote stream:', error);
      }
    }
    return null;
  }

  /**
   * Register a callback function for a specific event
   * 
   * Available events:
   * - 'track': Called when a new media track is received from the bot
   * - 'connectionStateChange': Called when the connection state changes
   * - 'error': Called when an error occurs
   * - 'botReady': Called when the bot signals it's ready to start
   * - 'connected': Called when successfully connected to the server
   * 
   * @param {string} event - The event name (without the 'on' prefix)
   * @param {Function} callback - The callback function to call when the event occurs
   */
  on(event, callback) {
    // Convert event name to callback key (e.g., 'track' -> 'onTrack')
    const eventKey = `on${event.charAt(0).toUpperCase() + event.slice(1)}`;
    if (this.callbacks.hasOwnProperty(eventKey)) {
      this.callbacks[eventKey] = callback;
    }
  }

  /**
   * Check if the client is currently connected to the server
   * 
   * @returns {boolean} True if connected, false otherwise
   */
  isConnected() {
    return this.pcClient && this.pcClient.state === 'connected';
  }
}

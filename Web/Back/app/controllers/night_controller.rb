# frozen_string_literal: true

# Controller that connects to:
# - Redis to get the last night information.
# - Cassandra to get the historical nights infomarmation.
class NightController < ApplicationController
  def last; end

  def historical; end

  def last_payload; end

  def historical_payload; end
end
